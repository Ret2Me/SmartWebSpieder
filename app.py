import multiprocessing
from threading import Thread
from flask import Flask, render_template, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from dataclasses import dataclass
from datetime import datetime
import scanner
import json
import config
import scheduler

# flask server app
manager = multiprocessing.Manager()
vulnerable_websites = manager.list()
app = Flask(__name__)
auth = HTTPBasicAuth()
processes = []


@auth.verify_password
def verify_password(username, password):
    """ Verify given user and password with list stored in config file. """
    if username in config.USERS and \
            check_password_hash(config.USERS.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    """ Render index.html with basic auth. """

    # get data for table
    result = scanner.session.query(scanner.Server)\
        .join(scanner.Vulnerabilities, scanner.Server.vulnerability_id == scanner.Vulnerabilities.id)\
        .order_by(scanner.Server.timestamp.desc())\
        .limit(8)

    records = []
    for record in result:
        records.append({
            'id': record.id,
            'url': record.url,
            'vulnerability_name': record.vulnerability.name,
            'severity': record.vulnerability.severity_level,
            'timestamp': record.timestamp,
            'confidence': record.confidence,
            'description': record.vulnerability.description})
    return render_template('index.html.j2', records=records)


@auth.login_required
@app.route('/api/hardware_monitor')
def hardware_monitor():
    """ Endpoint for frontend with information about CPU, RAM and disk usage """
    file = open('./logs/hardware/hardware.json', 'r')
    statistics = json.load(file)
    file.close()
    return '{ \"STATISTICS\": ' + str(statistics).replace('\'', '"') + '}'


# @auth.login_required
@app.route('/api/get_servers', methods=['GET'])
def servers_dump():
    """ Page with all results """

    vulnerability_id = request.args.get('vulnerability_id')  # int
    if vulnerability_id is None:
        vulnerability_id = scanner.Server.vulnerability_id

    lowest_severity_level = request.args.get('lowest_severity_level')  # int
    highest_severity_level = request.args.get('highest_severity_level')  # int

    if lowest_severity_level is None:
        lowest_severity_level = 0
    if highest_severity_level is None:
        highest_severity_level = 10

    lowest_confidence = request.args.get('lowest_confidence')  # int
    highest_confidence = request.args.get('highest_confidence')  # int

    if lowest_confidence is None:
        lowest_confidence = 0
    if highest_confidence is None:
        highest_confidence = 10

    beginning_time_period = request.args.get('beginning_time_period')  # int
    ending_time_period = request.args.get('ending_time_period')  # int

    if beginning_time_period is None:
        beginning_time_period = '01-01-0001_00:00:00'
    if ending_time_period is None:
        ending_time_period = str(datetime.now().strftime('%d-%m-%Y_%H:%M:%S'))

    limit = request.args.get('limit')
    count = request.args.get('count')  # bool


    result = scanner.session.query(scanner.Server)

    try:
        result = result.join(scanner.Vulnerabilities) \
            .filter((int(lowest_severity_level) <= scanner.Vulnerabilities.severity_level)
                    & (scanner.Vulnerabilities.severity_level <= int(highest_severity_level))
                    & (datetime.strptime(beginning_time_period, '%d-%m-%Y_%H:%M:%S') <= scanner.Server.timestamp)
                    & (scanner.Server.timestamp <= datetime.strptime(ending_time_period, '%d-%m-%Y_%H:%M:%S'))
                    & (lowest_confidence <= scanner.Server.confidence)
                    & (scanner.Server.confidence <= highest_confidence)
                    & (scanner.Server.vulnerability_id == vulnerability_id))
    except ValueError:
        return 'Probably incorrect datetime format, should be %d-%m-%Y_%H:%M:%S', 400

    if count:
        result = result.count()
        return str(result.real)

    serialized_list = []
    if limit is None:
        for record in result.order_by(scanner.Server.timestamp.desc()).all():
            serialized_list.append(record.serialize())
    else:
        try:
            for record in result.order_by(scanner.Server.timestamp.desc()).limit(limit):
                    serialized_list.append(record.serialize())
        except ValueError:
            return 'Probably incorrect datetime format, should be %d-%m-%Y_%H:%M:%S', 400

    return json.dumps(serialized_list)


def run_workers():
    """ Start new threads with web_crawlers """
    for i in range(0, len(config.URL_QUEUE)):
        crawler_obj = scanner.WebsiteCrawler([config.URL_QUEUE[i]],
                                             False,
                                             config.BLACK_LIST,
                                             vulnerable_websites)

        process = multiprocessing.Process(target=crawler_obj.run)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

Thread(target=run_workers).start()

""" Load all extensions and create connection to local database """

# import config
import config

# import SQLAlchemy
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# Import scanner engine class
import scanner
from scanner.scanner import WebsiteCrawler

# Load extensions
# Load extensions > URL obtaining
from scanner.extensions.url_dump.url_dump import url_dump

# Load extensions > vulnerability scanners
from scanner.extensions.env.env import env
from scanner.extensions.git.git import git
from scanner.extensions.svn.svn import svn


# Add extensions to scanner engine
WebsiteCrawler.url_dump = url_dump
WebsiteCrawler.env = env
WebsiteCrawler.git = git
WebsiteCrawler.svn = git

# Init database
engine = create_engine(config.DATABASE_URL, echo=True)
if not database_exists(config.DATABASE_URL):
    create_database(config.DATABASE_URL)
else:
    engine.connect()
Base = declarative_base()

# Import all tables
from scanner.sqlalchemy.vulnerabilities import Vulnerabilities as Vulnerabilities
from scanner.sqlalchemy.servers import Servers as Server
Base.metadata.create_all(engine)

# Create engine handler
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Vulnerabilities).count()
if query == 0:
    git_vulnerability = Vulnerabilities(id=1,
                                        name='GIT exposure',
                                        severity_level=9,
                                        endpoint='/.git/',
                                        description=('When .git folder is also deployed along with the web ',
                                                     'application, the attacker could exploit this ',
                                                     'misconfiguration to download the entire source code ',
                                                     'along with other sensitive ',
                                                     'data.  More info at:',
                                                     'https://iosentrix.com/blog/git-source-code-disclosure-vulnerability/'))
    svn_vulnerability = Vulnerabilities(id=2,
                                        name='SVN exposure',
                                        severity_level=9,
                                        endpoint='/.svn/',
                                        description=('When .svn folder is also deployed along with the web ',
                                                     'application, the attacker could exploit this misconfiguration ',
                                                     'to download the entire source code along with other sensitive ',
                                                     'data. More info at: ',
                                                     'https://medium.com/@ghostlulzhacks/exposed-source-code-c16fac0032ffd'))

    env_vulnerability = Vulnerabilities(id=3,
                                        name='ENV exposure',
                                        severity_level=9,
                                        endpoint='/.env/',
                                        description=('When .env file is also deployed along with the web ',
                                                     'application, the attacker could exploit this misconfiguration ',
                                                     'to download the entire environment variables file with ',
                                                     'sensitive data like database credentials. More info at: ',
                                                     'https://www.acunetix.com/vulnerabilities/web/dotenv-env-file/'))

    session.add_all([git_vulnerability, svn_vulnerability, env_vulnerability])
    session.commit()

""" Load all extensions and create connection to local database """

# import config
import config

# import SQLAlchemy
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Import scanner engine class
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
Base = declarative_base()

# Import all tables
from scanner.sqlalchemy.vulnerabilities import Vulnerabilities as Vulnerabilities
from scanner.sqlalchemy.servers import Servers as Server
Base.metadata.create_all(engine)

# Create engine handler
Session = sessionmaker(bind=engine)
session = Session()

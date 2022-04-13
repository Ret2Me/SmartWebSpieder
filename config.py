""" Configuration file """
from werkzeug.security import generate_password_hash

# --------- crawler engine settings --------
BLACK_LIST = ["<enter your black list here>"]
URL_QUEUE = ["<enter your black list here>"]
# ------------------------------------------


# ----------- SQLAlchemy settings ----------
DATABASE_URL = 'postgresql://postgres@localhost:5432/targets'
# ------------------------------------------


# -------- hardware usage monitoring -------
HARDWARE_SCAN_INTERVAL = 1  # in minutes
MONITORING_LOGS_LENGTH = 24  # in records
DISK_MONITORING_PATH = '/'
# ------------------------------------------


# ------------ website settings ------------
USERS = {
    "user": generate_password_hash("change_me"),
}
# ------------------------------------------

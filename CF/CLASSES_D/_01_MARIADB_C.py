

from mysql import connector as SQL
from CF.SUBM_D import _00_TIME_DT as CFTDT


LOG_FILENAME = f"""/storage/logs/CF/{CFTDT.nowStr()}.myMariaDB.log"""


class myMariaDB(object):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  def __init__(self, *,
      user_,
      password_,
      host_,
      database_,
      loggingOn_=True,
      logFilename_=LOG_FILENAME,
      logMode_="tw",
  ):
    # fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
    self.SQL_CONFIG = {
      'user': user_,
      'password': password_,
      'host': host_,
      'database': database_,
    }
    self.DB_CONNECTION = None
    self.DB_CURSOR = None
    self.LOGGING_ON = loggingOn_
    self.LOG_FILENAME = logFilename_
    self.LOG_MODE = logMode_
    # * 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (
        (loggingOn_ is True)
    ):
      self.FD_OUT = open(LOG_FILENAME, LOG_MODE)
    # * ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱
    else:
      self.FD_OUT = None
    # * ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
    self.doOpen()
    self.logIt("Initted")
    # fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

  def __enter__(self):
    # fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
    self.logIt("Entered")
    return self
    # fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

  def __exit__(self, *args_, *kwargs_):
    # fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
    pass
    # fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

  def doOpen(self, *,
      thisConfig_=None,
  ):
    # fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
    # * 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (
        (thisConfig_ is None)
    ):
      _myConfig_ = self.SQL_CONFIG
    # * ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱
    else:
      _myConfig_ = thisConfig_
    # * ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
    # * 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (
        (self.LOGGING_ON is True)
    ):
      self.logIt(f"""opening {_myConfig_["host"]}, {_myConfig["database"]}""")
    # * ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
    _DBConnection_ = SQL.connect(
        user=_myConfig_["user"],
        host=_myConfig_["host"],
        password=_myConfig_["password"],
        database=_myConfig_["database"]
    )
    _DBCursor_ = _DBConnection_.cursor(buffered=True, dictionary=True)
    # * 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (
        (thisConfig_ is None)
    ):
      self.DB_CONNECTION = _DBConnection_
      self.DB_CURSOR = _DBCursor_
    # * ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱
    else:
      return {
          "CONNECTION": _DBConnection_,
          "CURSOR": _DBCursor_
      }
    # * ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
    # fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2

  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  # * start of doClose
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  def doClose(self, *,
      DBConnection_=None,
  ):
    TDBLinks[C.DBCONNECTION].close()
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  # * end of doClose
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

  def doBlobSqlAll(TDBLinks, SQLStr, myBlob):
    SQLStr = fixSQLStr(SQLStr)
    TDBLinks[C.DBCURSOR].execute(SQLStr, myBlob)
    SQLRows = TDBLinks[C.DBCURSOR].fetchall()
    if len(SQLRows) > 0:
      SQLStr = """select found_rows() as FR;"""
      TDBLinks[C.DBCURSOR].execute(SQLStr)
      SQLNumRows = TDBLinks[C.DBCURSOR].fetchall()[0]["FR"]
    else:
      SQLRows = []
      SQLNumRows = 0
    return SQLRows, SQLNumRows

  def getSqlOne(TDBLinks, SQLStr):
    SQLStr = fixSQLStr(SQLStr)
    # TDBLinks[C.DBCURSOR].mysql_reset_connection()
    SQLResultReturned = TDBLinks[C.DBCURSOR].execute(SQLStr)
    if not SQLResultReturned:
      SQLRow = TDBLinks[C.DBCURSOR].fetchone()
    else:
      # TDBLinks[C.DBCONNECTION].commit()
      SQLRow = None
    return SQLRow

  def getSqlAll(TDBLinks, SQLStr):
    SQLStr = fixSQLStr(SQLStr)
    TDBLinks[C.DBCURSOR].execute(SQLStr)
    if SQLStr.casefold().find("select") > -1:
      SQLRows = TDBLinks[C.DBCURSOR].fetchall()
      if len(SQLRows) > 0:
        SQLStr = """select found_rows() as FR;"""
        TDBLinks[C.DBCURSOR].execute(SQLStr)
        TRow = TDBLinks[C.DBCURSOR].fetchall()
        SQLNumRows = TRow[0]["FR"]
      else:
        SQLRows = []
        SQLNumRows = 0
    else:
      SQLRows = []
      SQLNumRows = 0
    return SQLRows, SQLNumRows

  def insertDict(TDBLinks, myTable, myDict, myTypes):
    # myDict = fixDictToAddUpd(myDict)
    for key in myDict:
      tempType = myTypes[key]
      if C.DEBUGME == 42:
        print(f"""{str(DS.getDebugInfo(""))}
  key {key} tempType {tempType}
  myDict[key] {repr(myDict[key])}
  """)
      if tempType in ["datetime", "varchar"]:
        if isinstance(myDict[key], int):
          myDict[key] = TDS.TS2ISO(myDict[key])
        elif isinstance(myDict[key], str):
          myDict[key] = TDS.toStr(myDict[key])
        if myDict[key].find(C.DBLQT) == -1:
          myDict[key] = C.DBLQT + myDict[key] + C.DBLQT
        if tempType == "datetime" and myDict[key] == C.DFLTSTR:
          myDict[key] = TDS.nowStrSql(DT.now())
        if myDict[key].find(C.DBLQT) == -1:
          myDict[key] = C.DBLQT + myDict[key] + C.DBLQT
      if myDict[key] is None:
        myDict[key] = 0
      myDict[key] = str(myDict[key])
    dataStr = ', '.join(myDict.values())
    columns = ', '.join(myDict.keys())
    SQLStr = f"INSERT INTO {myTable} ({columns}) VALUES ({dataStr});"
    if C.DEBUGME == 42:
      print(f"{DS.getDebugInfo('SQLStr')} {SQLStr:s}")
    SQLResultReturned = TDBLinks[C.DBCURSOR].execute(SQLStr)
    if C.DEBUGME:
      print(f"{DS.getDebugInfo('SQLResultReturned')} {repr(SQLResultReturned)}")
    if not SQLResultReturned:
      SQLResultReturned = TDBLinks[C.DBCONNECTION].commit()
      if C.DEBUGME:
        print(f"{DS.getDebugInfo('SQLRESULT')} {repr(SQLResultReturned)}")
      if not SQLResultReturned:
        return None
      SQLRows = TDBLinks[C.DBCURSOR].fetchall()
      return SQLRows

  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  # start of logIt
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  def logIt(self,
      textToLog_,
      *,
      timeToLog_=None,
      stackPosition_=-2,
  ):
    # fold here ⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2⟱2
    # * 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱ 2⟱
    if (
        (timeToLog_ is None)
    ):
      _myTime_ = CFTDT.nowStr()
    # * ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱ ⟰2⟱
    else:
      _myTime_ = timeToLog_
    # * ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2 ⟰2
    self.FD_OUT.write(f"""{_myTime_} :: {DBG.whoAmI(stackPosition_=stackPosition_)} :: {textToLog_}{CFV.NEWLINE}""")
    # fold here ⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2⟰2
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  # end of logIt
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  # * start of updateDict
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  def updateDict(self, *,
      TDBLinks,
      myTable,
      myDict,
  ):
    # myDict = fixDictToAddUpd(myDict)
    SQLStr = f"UPDATE {myTable}\n\t SET "
    for key, value in myDict.items():
      SQLStr += f"{key} = {value},\n\t"
    SQLStr = SQLStr[:-3] + f"\n\twhere RID = {myDict['RID']}"
    if C.DEBUGME:
      print(f"{DS.getDebugInfo('SQLStr')} {SQLStr:s}")
    SQLResultReturned = TDBLinks[C.DBCURSOR].execute(SQLStr)
    if C.DEBUGME:
      print(f"{DS.getDebugInfo('SQLResultReturned')} {repr(SQLResultReturned)}")
    if not SQLResultReturned:
      SQLResultReturned = TDBLinks[C.DBCONNECTION].commit()
      if C.DEBUGME:
        print(f"{DS.getDebugInfo('SQLRESULT')} {repr(SQLResultReturned)}")
      if not SQLResultReturned:
        return None
      SQLRows = TDBLinks[C.DBCURSOR].fetchall()
      return SQLRows
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  # * end of updateDict
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  # * start of whoAmI
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  def whoAmI(self,
      *,
      stackPosition_=-1,
  ):
    # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
      _stack_ = INS.stack()
      # print(repr(_stack_))
      func_call = f"""{_stack_[stackPosition_][4][0].rstrip()}::"""
      # func_call = f"""{_stack_[stackPosition_][1]}::{_stack_[stackPosition_][2]}::{_stack_[stackPosition_][3]}::{_stack_[stackPosition_][4][0].rstrip()}::"""
      return _strToRtn_
    # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
  # * end of whoAmI
  # * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1

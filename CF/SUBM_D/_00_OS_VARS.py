

from CF.SUBM_D import _00_VALS_IN as CF_V
from os import path as OSPATH
from pathlib import Path as LPATH_
import glob as GLOB_
import inspect as INS
import os as OS
import re as RE
import subprocess as SP
import sys as SYS


V = None
locals().update(CF_V.ALL_THE_VALS)

ARGV = SYS.argv
EXIT = SYS.exit


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Keys
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
K_ACCESS_TIME = "K_ACCESS_TIME"
K_BLOCKS_ALLOCATED = "K_BLOCKS_ALLOCATED"
K_CHANGED_TIME = "K_CHANGED_TIME"
K_DEFAULT = "K_DEFAULT"
K_DIR = "K_DIR"
K_EXTENSION = "K_EXTENSION"
K_F_OK = OS.F_OK
K_FILENAME = "K_FILENAME"
K_FILETYPE = "K_FILETYPE"
K_FT_CODE = "K_FT_CODE"
K_FT_DATA = "K_FT_DATA"
K_FT_DOCS = "K_FT_DOCS"
K_FT_PICS = "K_FT_PICS"
K_FT_SNDS = "K_FT_SNDS"
K_FT_TEXT = "K_FT_TEXT"
K_FT_UNKNOWN = "K_FT_UNKNOWN"
K_FT_VIDS = "K_FT_VIDS"
K_GID = "K_GID"
K_I_CAN_EXECUTE = "K_I_CAN_EXECUTE"
K_I_CAN_READ = "K_I_CAN_READ"
K_I_CAN_WRITE = "K_I_CAN_WRITE"
K_IS_A_DIR = "K_IS_A_DIR"
K_IS_A_FILE = "K_IS_A_FILE"
K_IS_A_KNOWN_FILE_TYPE = "K_IS_A_KNOWN_FILE_TYPE"
K_IS_A_SYMLINK = "K_IS_A_SYMLINK"
K_JUST_FILENAME = "K_JUST_FILENAME"
K_LAST = "K_LAST"
K_LIST = "K_LIST"
K_MODE = "K_MODE"
K_MODIFY_TIME = "K_MODIFY_TIME"
K_NEW_FILENAME = "K_NEW_FILENAME"
K_NUMS = "K_NUMS"
K_PATH = "K_PATH"
K_QUIT = "K_QUIT"
K_R_OK = OS.R_OK
K_SIZE = "K_SIZE"
K_UID = "K_UID"
K_VERSION = "K_VERSION"
K_W_OK = OS.W_OK
K_X_OK = OS.X_OK


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Entry Vars
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
SHORT_ENTRY_TUP = (
    (K_PATH, ""),
    (K_DIR, ""),
    (K_FILENAME, ""),
    (K_JUST_FILENAME, ""),
    (K_EXTENSION, ""),
    (K_NUMS, 0),
)
def E_SHORT_ENTRY():
  return dict((x, y) for x, y in SHORT_ENTRY_TUP)


ENTRY_TUP = (
    (K_ACCESS_TIME, 0),
    (K_BLOCKS_ALLOCATED, 0),
    (K_CHANGED_TIME, 0),
    (K_DIR, ""),
    (K_EXTENSION, ""),
    (K_FILENAME, ""),
    (K_FILETYPE, K_FT_UNKNOWN),
    (K_GID, 0),
    (K_I_CAN_EXECUTE, False),
    (K_I_CAN_READ, False),
    (K_I_CAN_WRITE, False),
    (K_IS_A_DIR, False),
    (K_IS_A_FILE, False),
    (K_IS_A_KNOWN_FILE_TYPE, False),
    (K_IS_A_SYMLINK, False),
    (K_JUST_FILENAME, False),
    (K_MODE, -1),
    (K_MODIFY_TIME, 0),
    (K_NEW_FILENAME, ""),
    (K_NUMS, 0),
    (K_PATH, ""),
    (K_SIZE, 0),
    (K_UID, 0),
)
def E_ENTRY():
  return dict((x, y) for x, y in ENTRY_TUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Sanity Checks
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
DIR_BLACK_LIST = "[a-zA-Z0-9./]"
DIR_WHITE_LIST = "[^a-zA-Z0-9\-_\./]"
FILE_BLACK_LIST = "[a-zA-Z0-9.]"
FILE_WHITE_LIST = "[^a-zA-Z0-9\-_\.]"


ILLEGALPATHS = [  # list of absolute paths to be completely ignored if used
  "/",  # do not operate on / ever
]

ILLEGALWILDCARDS = [  # list all of the portions of a filename which will result in an error [0:] based
  "/bin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/boot/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/dev/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/efi/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/etc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/home/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/lib/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/lib64/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/media/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/opt/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/proc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/root/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/run/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/sbin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/srv/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/sys/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/tmp/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/usr/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/var/",  # illegal wildcards, these are most often /path/ and will be [0:] based
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of sortDedupeList
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def sortDedupeList(listIn_):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  _listToRtn_ = list(sorted(set(listIn_)))
  return _listToRtn_
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of sortDedupeList
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Type Lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FTL_CODE = [
    ".c",
    ".coffee",
    ".php",
    ".pl",
    ".py",
    ".sh",
    ".zsh",
]

FTL_DATA = [
    ".cson",
    ".csv",
    ".db",
    ".json",
    ".kml",
    ".kmz",
    ".sqlite",
]
FTL_TEXT_DATA = [
    ".cson",
    ".csv",
    ".json",
    ".kml",
]

FTL_DOCS = [
    ".md",
    ".pdf",
    ".txt",
    ".pkl",
    ".odt",
]
FTL_TEXT_DOCS = [
    ".md",
    ".txt",
]

FTL_PICS = [
    ".bmp",
    ".gif",
    ".jp2",
    ".jpe",
    ".jpeg",
    ".jpg",
    ".png",
    ".riff",
    ".webp",
]

FTL_SNDS = [
    ".au",
    ".mp3",
    ".wav",
]

FTL_TEXT = [
    ".lst",
    ".txt",
]
FTL_TEXT.extend(FTL_CODE)
FTL_TEXT.extend(FTL_TEXT_DOCS)
FTL_TEXT.extend(FTL_TEXT_DATA)
FTL_TEXT = sortDedupeList(FTL_TEXT)

FTL_VIDS = [
    ".asx",
    ".avi",
    ".divx",
    ".flv",
    ".gifv",
    ".hdv1",
    ".hdv2",
    ".hdv3",
    ".m2ts",
    ".m4a",
    ".m4v",
    ".mkv",
    ".mov",
    ".mp1v",
    ".mp4",
    ".mpeg",
    ".mpg",
    ".mpg1",
    ".ogv",
    ".qt",
    ".vcr2",
    ".video",
    ".webm",
    ".wmv",
]

# LEAVE AT BOTTOM OF FILE TYPES
FTL_MEDIA = []
FTL_MEDIA.extend(FTL_PICS)
FTL_MEDIA.extend(FTL_SNDS)
FTL_MEDIA.extend(FTL_VIDS)
FTL_MEDIA = sortDedupeList(FTL_MEDIA)

FTL_ALL_KNOWN = []
FTL_ALL_KNOWN.extend(FTL_CODE)
FTL_ALL_KNOWN.extend(FTL_DATA)
FTL_ALL_KNOWN.extend(FTL_DOCS)
FTL_ALL_KNOWN.extend(FTL_PICS)
FTL_ALL_KNOWN.extend(FTL_SNDS)
FTL_ALL_KNOWN.extend(FTL_TEXT)
FTL_ALL_KNOWN.extend(FTL_VIDS)
FTL_ALL_KNOWN = sortDedupeList(FTL_ALL_KNOWN)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Ignore File Lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
IL_PYTHON = [
    "__enter__.py",
    "__exit__.py",
    "__init__.py",
    "__main__.py",
]

IL_MEDIA = [
    "thumbs.db",
    "__unrename__.zsh"
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Modes
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
A_R = lambda __MODE__: __MODE__ and 0o004
A_RW = lambda __MODE__: __MODE__ and 0o006
A_RWX = lambda __MODE__: __MODE__ and 0o007
A_W = lambda __MODE__: __MODE__ and 0o002
A_X = lambda __MODE__: __MODE__ and 0o001
G_R = lambda __MODE__: __MODE__ and 0o040
G_RW = lambda __MODE__: __MODE__ and 0o060
G_RWX = lambda __MODE__: __MODE__ and 0o070
G_W = lambda __MODE__: __MODE__ and 0o020
G_X = lambda __MODE__: __MODE__ and 0o010
U_R = lambda __MODE__: __MODE__ and 0o400
U_RW = lambda __MODE__: __MODE__ and 0o600
U_RWX = lambda __MODE__: __MODE__ and 0o700
U_W = lambda __MODE__: __MODE__ and 0o200
U_X = lambda __MODE__: __MODE__ and 0o100


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of KD_ERROR_DIALOG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def KD_ERROR_DIALOG(*,
    details_=None,
    message_,
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (details_ in V.CF_V.EMPTY_STR_LST)
  ):
    _listToRtn_ = [
        "kdialog",
        "--error",
        f"""{V.CF_V.DBLQT}{message_}{V.CF_V.DBLQT}""",
    ]
  # ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱
  else:
    _listToRtn_ = [
        "kdialog",
        "--detailederror",
        f"""{V.CF_V.DBLQT}{message_}{V.CF_V.DBLQT}""",
        f"""{V.CF_V.DBLQT}{details_}{V.CF_V.DBLQT}""",
    ]
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  return _listToRtn_
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of KD_ERROR_DIALOG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


DEBUG_ERROR_CODES = {
    1: "IO error.",
    2: "File or directory not found.",
    3: "Incorrect parameters given."
}


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of KD_WARNING_DIALOG_LIST
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def KD_WARNING_DIALOG_LIST(*,
    message_,
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  _strToRtn_ = f"""{V.CF_V.DBLQT}{message_}{V.CF_V.DBLQT}"""
  _listToRtn_ = [
      "kdialog",
      "--warningyesno",
      _strToRtn_,
  ]
  return _listToRtn_
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of KD_WARNING_DIALOG_LIST
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of KD_TWO_BTN_DIALOG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def KD_TWO_BTN_DIALOG(*,
    noLabel_="no",
    message_=None,
    yesLabel_="yes",
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (message_ is None)
  ):
    message_ = ""
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  _listToRtn_ = [
      "kdialog",
      "--yesno"
      f"""{V.CF_V.DBLQT}{message_}{V.CF_V.DBLQT}""",
      "--no-label",
      f"""{V.CF_V.DBLQT}{noLabel_}{V.CF_V.DBLQT}""",
      "--yes-label",
      f"""{V.CF_V.DBLQT}{yesLabel_}{V.CF_V.DBLQT}""",
  ]
  return _listToRtn_
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of KD_TWO_BTN_DIALOG
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of SP_FIND_FILES
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def SP_FIND_FILES(*,
    filename_,
    rootDir_,
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  _listToRtn_ = [
      "find",
      f"""{rootDir_}""",
      "-name",
      f"""{filename_}"""
  ]
  _dictToRtn_ = {
      "capture_output": True,
      "text": True,
  }
  return (_listToRtn_, _dictToRtn_)
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of SP_FIND_FILES
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*




ALL_THE_KEYS = {
    "K_ACCESS_TIME": K_ACCESS_TIME,
    "K_BLOCKS_ALLOCATED": K_BLOCKS_ALLOCATED,
    "K_CHANGED_TIME": K_CHANGED_TIME,
    "K_DEFAULT": K_DEFAULT,
    "K_DIR": K_DIR,
    "K_EXTENSION": K_EXTENSION,
    "K_F_OK": K_F_OK,
    "K_FILENAME": K_FILENAME,
    "K_FILETYPE": K_FILETYPE,
    "K_FT_CODE": K_FT_CODE,
    "K_FT_DATA": K_FT_DATA,
    "K_FT_DOCS": K_FT_DOCS,
    "K_FT_PICS": K_FT_PICS,
    "K_FT_SNDS": K_FT_SNDS,
    "K_FT_TEXT": K_FT_TEXT,
    "K_FT_UNKNOWN": K_FT_UNKNOWN,
    "K_FT_VIDS": K_FT_VIDS,
    "K_GID": K_GID,
    "K_I_CAN_EXECUTE": K_I_CAN_EXECUTE,
    "K_I_CAN_READ": K_I_CAN_READ,
    "K_I_CAN_WRITE": K_I_CAN_WRITE,
    "K_IS_A_DIR": K_IS_A_DIR,
    "K_IS_A_FILE": K_IS_A_FILE,
    "K_IS_A_KNOWN_FILE_TYPE": K_IS_A_KNOWN_FILE_TYPE,
    "K_IS_A_SYMLINK": K_IS_A_SYMLINK,
    "K_JUST_FILENAME": K_JUST_FILENAME,
    "K_LAST": K_LAST,
    "K_LIST": K_LIST,
    "K_MODE": K_MODE,
    "K_MODIFY_TIME": K_MODIFY_TIME,
    "K_NEW_FILENAME": K_NEW_FILENAME,
    "K_NUMS": K_NUMS,
    "K_PATH": K_PATH,
    "K_QUIT": K_QUIT,
    "K_R_OK": K_R_OK,
    "K_SIZE": K_SIZE,
    "K_UID": K_UID,
    "K_VERSION": K_VERSION,
    "K_W_OK": K_W_OK,
    "K_X_OK": K_X_OK,
}


FILESYSTEM_DATA = {
    "A_R": A_R,
    "A_RW": A_RW,
    "A_RWX": A_RWX,
    "A_W": A_W,
    "A_X": A_X,
    "DEBUG_ERROR_CODES": DEBUG_ERROR_CODES,
    "DIR_BLACK_LIST": DIR_BLACK_LIST,
    "DIR_WHITE_LIST": DIR_WHITE_LIST,
    "E_ENTRY": E_ENTRY,
    "E_SHORT_ENTRY": E_SHORT_ENTRY,
    "FILE_BLACK_LIST": FILE_BLACK_LIST,
    "FILE_WHITE_LIST": FILE_WHITE_LIST,
    "FTL_ALL_KNOWN": FTL_ALL_KNOWN,
    "FTL_CODE": FTL_CODE,
    "FTL_DATA": FTL_DATA,
    "FTL_DOCS": FTL_DOCS,
    "FTL_MEDIA": FTL_MEDIA,
    "FTL_PICS": FTL_PICS,
    "FTL_SNDS": FTL_SNDS,
    "FTL_TEXT_DATA": FTL_TEXT_DATA,
    "FTL_TEXT_DOCS": FTL_TEXT_DOCS,
    "FTL_TEXT": FTL_TEXT,
    "FTL_VIDS": FTL_VIDS,
    "G_R": G_R,
    "G_RW": G_RW,
    "G_RWX": G_RWX,
    "G_W": G_W,
    "G_X": G_X,
    "IL_MEDIA": IL_MEDIA,
    "IL_PYTHON": IL_PYTHON,
    "ILLEGALPATHS": ILLEGALPATHS,
    "ILLEGALWILDCARDS": ILLEGALWILDCARDS,
    "U_R": U_R,
    "U_RW": U_RW,
    "U_RWX": U_RWX,
    "U_W": U_W,
    "U_X": U_X,
}


KDIALOG_DATA = {
    "KD_WARNING_DIALOG_LIST": KD_WARNING_DIALOG_LIST,
    "KD_TWO_BTN_DIALOG": KD_TWO_BTN_DIALOG,
    "KD_ERROR_DIALOG": KD_ERROR_DIALOG,
}


SUBPROCESS_DATA = {
    "SP_FIND_FILES": SP_FIND_FILES,
}


DEBUG_DATA = {
    "DEBUG_ERROR_CODES": DEBUG_ERROR_CODES,
}


ALL_THE_OS_DATA = {
    "ALL_THE_VALS": CF_V.ALL_THE_VALS,
    "ARGV": ARGV,
    "CF_V": CF_V,
    "EXIT": EXIT,
    "GLOB_": GLOB_,
    "INS": INS,
    "LPATH_": LPATH_,
    "OS": OS,
    "OSPATH": OSPATH,
    "RE": RE,
    "SP": SP,
    "SYS": SYS,
}
ALL_THE_OS_DATA.update(ALL_THE_KEYS)
ALL_THE_OS_DATA.update(FILESYSTEM_DATA)
ALL_THE_OS_DATA.update(KDIALOG_DATA)
ALL_THE_OS_DATA.update(SUBPROCESS_DATA)
ALL_THE_OS_DATA.update(DEBUG_DATA)
ALL_THE_OS_DATA.update(CF_V.ALL_THE_VALS)



#

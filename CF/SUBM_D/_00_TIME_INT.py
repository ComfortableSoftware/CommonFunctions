

from time import time as WALLSECS
from time import time_ns as TNS


DAY_MS = (60 * 60 * 24 * 1000)  # 86400000
DAY_S = (60 * 60 * 24)  # 86400
HALFDAY_S = (60 * 60 * 12)  # 43200
HALFHOUR_S = (60 * 30)  # 1800
HOUR_S = (60 * 60)  # 3600
MINUTE_S = 60 # 60
QUARTERDAY_S = (60 * 60 * 6)
QUARTERHOUR_S = (60 * 15)  # 900
TIME_S_995959 = (60 * 60 * 100)  # 360000
TIME_S_DDD235959 = (60 * 60 * 24 * 1000)


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# isPast
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def isPast(timeToChk_):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	if MTS() >= timeToChk_:
		return True
	else:
		return False
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# myTimestamp 1612179130.285 -=> 1612179130285 if TNS used, same resolution since boot not epoch for TMT
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def MTS():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	return int(TMT()*1000)
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# myTimestamp 1612179130.285 -=> 1612179130285 if TNS used, same resolution since boot not epoch for TMT
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def MTSS():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	return ((int(WALLSECS()) % 86400) + GMTOFFSET) % 86400 # 360000 for 99:59:59  86400 for 23:59:59
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# loseTheSecs
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def loseTheSecs(intIn_):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	return (intIn_ // 60) * 60
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# MTSM
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def MTSM():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	return loseTheSecs(MTSS())
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# MTSMS():
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def MTSMS():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	return ((int(WALLSECS() * 1000)) + (GMTOFFSET * 1000)) % (86400 * 1000) # 3600000 for 99:59:59  86400 for 23:59:59
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
"""
is_dst = time.daylight and time.localtime().tm_isdst > 0
utc_offset = - (time.altzone if is_dst else time.timezone)
"""

# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# MTSPlus
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def MTSPlus(numToAdd_):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	if not isinstance(numToAdd_, int):
		numToAdd_ = 0
	valToRtn_ = MTS() + numToAdd_
	# print("MTSPlus ", MTS(), numToAdd_, valToRtn_)
	return valToRtn_
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# MTSclr
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def MTSclr():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	return f"""{CLREOL}{MTS()}{NEWLINE}{CLREOL}"""
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# secsI
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def secsI():
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	return int(WALLSECS)
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# mySleep uses timer, not accurate to wallclock
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def mySleep(fToSleep_):
	# fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
	endTime_ = MTSPlus(fToSleep_)
	while MTS() < endTime_:
		pass
	# fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1



#

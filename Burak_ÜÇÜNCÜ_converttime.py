year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
hour = int(input("Enter an hour: "))
minute = int(input("Enter a minute: "))
second = float(input("Enter a second: "))

if not (1 <= month <= 12):
    print("Invalid month")
    exit()

if not (1 <= day <= 31):
    print("Invalid day")
    exit()

if not (0 <= hour <= 23):
    print("Invalid hour")
    exit()

if not (0 <= minute <= 59):
    print("Invalid minute")
    exit()

if not (0 <= second <= 59):
    print("Invalid second")
    exit()

UTC = [year, month, day, hour, minute, second]

leap_seconds_history = ["1972 6 30", "1972/12/31", "1973/12/31", "1974/12/31",
                        "1975/12/31", "1976/12/31", "1977/12/31", "1978/12/31",
                        "1979/12/31", "1981/6/30", "1982/6/30", "1983/6/30",
                        "1985/6/30", "1987/12/31", "1989/12/31", "1990/12/31",
                        "1992/6/30", "1993/6/30", "1994/6/30", "1995/12/31",
                        "1997/6/30", "1998/12/31", "2005/12/31", "2008/12/31",
                        "2012/6/30", "2015/6/30", "2016/12/31"]
leap_seconds = len(leap_seconds_history) 
if year >= 2017:
    leap_seconds = leap_seconds
elif year < 2017 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 1
elif year < 2015 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 2
elif year < 2012 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 3
elif year < 2008 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 4
elif year < 2005 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 5
elif year < 1998 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 6
elif year < 1997 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 7
elif year < 1995 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 8
elif year < 1994 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 9
elif year < 1993 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 10
elif year < 1992 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 11
elif year < 1990 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 12
elif year < 1989 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 13
elif year < 1987 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 14
elif year < 1985 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 15
elif year < 1983 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 16
elif year < 1982 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 17
elif year < 1981 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 18
elif year < 1979 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 19
elif year < 1978 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 20
elif year < 1977 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 21
elif year < 1976 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 22
elif year < 1975 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 23
elif year < 1974 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 24
elif year < 1973 and month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 25
elif year < 1972 and 6 < month <= 12 and day < 31 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 26
elif year < 1972 and month <= 6 and day < 30 and hour < 23 and minute < 59 and second < 60:
    leap_seconds = leap_seconds - 27


def convert_to_JD(UTC):
    year = UTC[0]
    month = UTC[1]
    day = UTC[2]
    hour = UTC[3]
    minute = UTC[4]
    second = UTC[5]
    if month <= 2:
        year = year - 1
        month = month + 12
    JD = int(365.25 * (year)) + int(30.6001 * (month + 1)) + day + hour / 24 + 1720981.5 + minute / 1440 + second / 86400
    return JD

utc_to_jd = convert_to_JD(UTC)  

TAI = utc_to_jd + (10 + leap_seconds) / 86400
GPST = utc_to_jd + (leap_seconds - 9) / 86400
BDT = utc_to_jd + (leap_seconds - 23) / 86400
TT = TAI + 32.184 / 86400

def converttime(self):  
    a = int(self + 0.5)
    b = a + 1537
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)  
    day = int(b - d - int(30.6001 * e) + (self + 0.5) - a)
    month = e - 1 - 12 * int(e / 14)
    year = c - 4715 - int((7 + month) / 10)
    second = round((self + 0.5 - a) * 86400, 1)
    return year, month, day, second

TAI_to_UTC = converttime(TAI)
GPST_to_UTC = converttime(GPST)
BDT_to_UTC = converttime(BDT)
TT_to_UTC = converttime(TT)

print(TAI_to_UTC, "vector that includes the date in a format, as year, month, day, second of day in TAI")
print(GPST_to_UTC, "vector that includes the date in a format, as year, month, day, second of day in GPST")
print(BDT_to_UTC, "vector that includes the date in a format, as year, month, day, second of day in BDT")
print(TT_to_UTC, "vector that includes the date in a format, as year, month, day, second of day in TT")
from datetime import datetime

t1 = "Sat 02 May 2015 19:54:36 +0530"
t2 = "Fri 01 May 2015 13:54:36 -0000"

"""
%a: Abbreviated weekday name (e.g., "Sat" for Saturday)
%d: Day of the month as a zero-padded decimal number (e.g., "02")
%b: Abbreviated month name (e.g., "May")
%Y: Four-digit year (e.g., "2015")
%H: Hour (24-hour clock) as a zero-padded decimal number (e.g., "19")
%M: Minute as a zero-padded decimal number (e.g., "54")
%S: Second as a zero-padded decimal number (e.g., "36")
%z: UTC offset in the form "+HHMM" or "-HHMM" (e.g., "+0530" for a positive UTC offset of 5 
"""

date_time_format = "%a %d %b %Y %H:%M:%S %z"
date1 = datetime.strptime(t1, date_time_format)
date2 = datetime.strptime(t2, date_time_format)

difference  = abs(int((date1 - date2).total_seconds()))
print(difference)
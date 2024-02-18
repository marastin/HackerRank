import calendar

print(calendar.TextCalendar(firstweekday=6).formatyear(2024))
print(calendar.isleap(2024))
print(calendar.weekday(2024, 2, 18)) # 6 means Sunday
print(calendar.weekheader(3)) # Return the names of week day with length n
print(calendar.monthcalendar(2024,2))
print(calendar.weekday(2024,2,18))


# HackerRank
S = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(S[2], S[0], S[1])].upper())



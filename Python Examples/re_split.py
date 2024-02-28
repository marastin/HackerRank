import re

# Example

re.split(r"-","+91-011-2711-1111")
# ['+91', '011', '2711', '1111']

# HackerRank
text = '100,000,000.000'
regex_pattern = r"[.,]"	# Do not delete 'r'.
print("\n".join(re.split(regex_pattern, text)))
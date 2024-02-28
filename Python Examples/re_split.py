import re

# Example

re.split(r"-","+91-011-2711-1111")
# ['+91', '011', '2711', '1111']

# HackerRank
text = '100,000,000.000'
regex_pattern = r"[.,]"	# Do not delete 'r'.
print("\n".join(re.split(regex_pattern, text)))



# Note:
# The r prefix before a string literal denotes a raw string literal.
# When you prefix a string literal with r (e.g., r"string"), it indicates that backslashes 
# within the string should be treated as literal characters rather than as escape characters.
# print("C:\path\to\file")  # Output: C:\path\to\file (incorrect)
# print(r"C:\path\to\file") # Output: C:\path\to\file (correct)

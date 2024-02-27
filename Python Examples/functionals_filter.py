import re


"""
Note:
re.fullmatch: This indicates that we are using the fullmatch function from the re module in Python, which attempts to match the entire string against the specified pattern. This means that the pattern must match the entire string, not just a part of it.

"[a-zA-Z0-9_-]+": This part of the expression matches one or more occurrences (+) of any lowercase letter (a-z), uppercase letter (A-Z), digit (0-9), underscore (_), or hyphen (-). This is typically the pattern for the local part of an email address before the @ symbol.

@: This matches the literal character '@', which separates the local part (username) from the domain part (hostname) in an email address.

[a-zA-Z0-9]+: This part matches one or more occurrences of any lowercase letter (a-z), uppercase letter (A-Z), or digit (0-9). This is typically for the domain part of an email address.

\.: This matches a literal dot character (.). In regular expressions, a dot usually means "any character," but when preceded by a backslash \, it matches the literal dot character.

[a-zA-Z]{1,3}: This matches between 1 and 3 occurrences of any lowercase letter (a-z) or uppercase letter (A-Z). This typically represents the top-level domain (TLD) of an email address, such as .com, .net, .org, etc.
"""


def fun(s: str):
    pattern = "[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}"
    return re.fullmatch(pattern, s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
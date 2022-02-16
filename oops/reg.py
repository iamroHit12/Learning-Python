import re

s = 'geeks$forgeeks'
 
# without using \
match = re.search(r'$', s)
print(match.start())
 
# using \
match = re.search(r'\$', s)
print(match.start())
import os
import re

lst = [re.search(r'^([\S]+)', s.strip('\n')).group() for s in os.popen('pip list -o').readlines()][2:]

print("\n--- UPDATED PACKAGES ---")
print(lst)

for p in lst:
    os.system('pip install -U '+p)


print("\n--- UPDATE FINISHED! ---")
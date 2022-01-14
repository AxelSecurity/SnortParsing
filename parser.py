import os
import requests
import re
import tarfile
import pyfiglet

ascii_banner = pyfiglet.figlet_format("AxelSecurity")
print(ascii_banner)

search_string = input("Enter string for search: ")
line_regex = re.compile(r"%s" % search_string)


url =  "https://www.snort.org/downloads/community/community-rules.tar.gz"
r = requests.get(url, stream = True)
with open ("community-rules.tar.gz", "wb") as f:
    for chunk in r.iter_content(chunk_size = 16*1024):
        f.write(chunk)
file = tarfile.open('community-rules.tar.gz')
file.extractall('./snort_rules')
file.close()
os.remove('community-rules.tar.gz')
with open ("./snort_rules/community-rules/community.rules", "r") as x:
    for line in x:
        if (line_regex.search(line)):
            if not line.startswith("#"):
                print(line)


import sys
from jinja2 import Template
template = Template(open("templates/online_browse.md").read())
import re
wrdRe=re.compile("^[a-zåäöA-ZÅÄÖ-]+$")

words=[] #tuples of dist,correct,incorrect,count_correct,count_incorrect
for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    dist,correct,incorrect,count_correct,count_incorrect=line.split("\t")
    dist=int(float(dist))
    if not wrdRe.match(correct):
        continue
    if dist==2 and len(correct)<4:
        continue
    words.append((dist,correct,incorrect,count_correct,count_incorrect))

print(template.render(words=words))


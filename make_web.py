import sys
from jinja2 import Template
template = Template(open("templates/online_browse.md").read())

words=[] #tuples of dist,correct,incorrect,count_correct,count_incorrect
for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    dist,correct,incorrect,count_correct,count_incorrect=line.split("\t")
    dist=str(int(float(dist)))
    words.append((dist,correct,incorrect,count_correct,count_incorrect))

print(template.render(words=words))


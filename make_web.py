import sys
from jinja2 import Template
template = Template(open("templates/online_browse.md").read())
template_idx = Template(open("templates/idx.md").read())
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
    if len(correct)<3:
        continue
    words.append((dist,correct,incorrect,count_correct,count_incorrect))

words.sort(key=lambda w: w[1])
first_letters=sorted(set(w[1][0] for w in words)-set("-"))
for l in first_letters:
    with open("docs/"+l+".md","w") as f:
        print(template.render(words=list(w for w in words if w[1][0]==l),letter=l),file=f)


with open("docs/index.md","w") as f:
    print(template_idx.render(letters=first_letters),file=f)

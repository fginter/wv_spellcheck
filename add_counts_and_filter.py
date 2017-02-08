import six
assert six.PY3, "Run with python3"
import sys
import re

punct_surround=re.compile(r"^([^a-zA-ZÅÄÖäöå]*)(.*?)([^a-zA-ZÅÄÖäöå]*)$")
def simple_hit(w1,w2):
    """Check whether w2 is simply w1 with surrounding punctuation"""
    match=punct_surround.match(w2)
    assert match
    if (len(match.group(1))>0 or len(match.group(3))>0) and match.group(2).lower()==w1.lower():
        print("Trivial", w1, w2, file=sys.stderr)
        return True
    else:
        return False

unknown=set()
known=set()
with open("pairs_initial.vocab.omorfi","r") as f:
    for line in f:
        line=line.strip()
        if not line:
            continue
        wordform,analysis=line.split("\t")
        if analysis=="+?":
            unknown.add(wordform)
        else:
            known.add(wordform)

counts={}
with open("/home/jmnybl/embedding_models/finnish_vocab","r") as f:
    for line in f:
        line=line.rstrip("\n").lstrip()
        count,wform=line.split(" ",1)
        if wform in known or wform in unknown: #I will need this count
            counts[wform]=int(count)

#this reads pairs-initial
for line in sys.stdin:
    line=line.strip()
    score,w1,w2=line.split("\t")
    if w1 in known and w2 in known: #Both known, skip
        continue
    elif w1 in unknown and w2 in unknown: #Both unknown, skip
        continue
    elif w1 in unknown and w2 in known:
        w1,w2=w2,w1
    elif w1 in known and w2 in unknown:
        pass
    else:
        print("Skipping weird pair", w1, w1 in known, w1 in unknown, "   ", w2, w2 in known, w2 in unknown, file=sys.stderr)
        continue
    if w1 not in counts or w2 not in counts:
        print("Skipping weird pair w/o counts", w1, w1 in known, w1 in unknown, "   ", w2, w2 in known, w2 in unknown, file=sys.stderr)
        continue
    assert w1 in known and w2 in unknown, (w1,w2)
    if simple_hit(w1,w2):
        continue
    print(score,w1,w2,counts[w1],counts[w2],sep="\t")


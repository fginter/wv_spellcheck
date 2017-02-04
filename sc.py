from __future__ import print_function
import sys
import math
import lwvlib
import numpy as np
from Bio import pairwise2

def edist(w,nearest,wv):
    """ w - words, nearest - indices into wv """
    for nn in nearest:
        nn_word=wv.words[nn]
        if abs(len(w)-len(nn_word))>2:
            continue
        score=pairwise2.align.globalxx(w,wv.words[nn],score_only=True)
        err=max(len(w),len(nn_word))-score
        if err>2 or err==0:
            continue
        print(err,w.encode("utf-8"),nn_word.encode("utf-8"),sep="\t")
        

if __name__=="__main__":
    batch=200
    K=10
    wv=lwvlib.load("/home/ginter/w2v/pb34_wf_200_v2.bin",1500000,1500000)
    np.divide(wv.vectors, wv.norm_constants[:,None], wv.vectors)
    vectors=wv.vectors
    for i in range(0,vectors.shape[0],batch):
        sims=vectors[i:i+batch,:].dot(vectors.T)
        top_K=np.argpartition(sims,sims.shape[1]-K)[:,-K:] #words x K-1 indices of the nearest elements
        top_K_sims=sims[np.arange(batch)[:, None], top_K]
        #print(top_K_sims)
        argsorted=np.argsort(-top_K_sims)
        top_K_sorted=top_K[np.arange(batch)[:, None], argsorted]
        for w,nearest in zip(wv.words[i:i+batch],top_K_sorted):
            edist(w,nearest,wv)
        print(i,file=sys.stderr)
        sys.stdout.flush()
        sys.stderr.flush()


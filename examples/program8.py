import random, math                                                        
from collections import defaultdict
sentences=[input(f"Enter sentence {i+1}: ").lower() for i in range(3)]
text=" ".join(sentences).split()
ngrams=defaultdict(lambda:defaultdict(int))
for i in range(len(text)-1):
    ctx=(text[i],)
    nxt=text[i+1]
    ngrams[ctx][nxt]+=1
probs={ctx:{w:c/sum(nw.values()) for w,c in nw.items()} for ctx,nw in ngrams.items()}
def generate(seed,length=20):
    ctx=(seed.lower(),)
    out=[seed]
    for _ in range(length):
        if ctx not in probs:break
        words,p=zip(*probs[ctx].items())
        nxt=random.choices(words,p)[0]
        out.append(nxt)
        ctx=(nxt,)
    return " ".join(out)
def perplexity():
    logp,c=0,0
    for i in range(len(text)-1):
        ctx,nxt=(text[i],),text[i+1]
        prob=probs.get(ctx,{}).get(nxt,1e-8)
        logp+=math.log(prob)
        c+=1
    return math.exp(-logp/c)
seed=input("\nSeed word: ")
print("\nGenerated Text:")
print(generate(seed,30))
print("\nModel Perplexity:",perplexity())

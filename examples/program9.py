import numpy as np                     
import matplotlib.pyplot as plt
from numpy.linalg import norm
sentence="the quick brown fox jumps over the lazy dog"
tokens=sentence.split()
n,d=len(tokens),16
np.random.seed(42)
E=np.random.rand(n,d)
E=E/norm(E,axis=1,keepdims=True)
Wq,Wk,Wv=[0.1*np.random.randn(d,d) for _ in range(3)]
Q,K,V=E@Wq,E@Wk,E@Wv
def softmax(x):
    x=x-np.max(x,axis=-1,keepdims=True)
    ex=np.exp(x)
    return ex/ex.sum(axis=-1,keepdims=True)
att=softmax((Q@K.T)/np.sqrt(d))
plt.figure(figsize=(10,8))
plt.imshow(att,cmap="viridis")
plt.xticks(range(n),tokens,rotation=45,ha="right")
plt.yticks(range(n),tokens)
plt.title("Self-Attention Heatmap",fontsize=14)
plt.colorbar(label="Attention Weight")
plt.tight_layout()
plt.show()

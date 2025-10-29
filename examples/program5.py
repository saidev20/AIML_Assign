import pandas as pd                                          
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
FILE = "housing.csv"
K = 3
COLS = None
df = pd.read_csv(FILE)
X = df[COLS].values if COLS else df.select_dtypes("number").values
km = KMeans(n_clusters=K, n_init=10).fit(X)
km_labels = km.labels_
sil_km = silhouette_score(X, km_labels)
gmm = GaussianMixture(n_components=K).fit(X)
gmm_labels = gmm.predict(X)
sil_gmm = silhouette_score(X, gmm_labels)
print("\nKMeans Silhouette:", sil_km)
print("GMM    Silhouette:", sil_gmm)
print("\nBetter Model:", "KMeans" if sil_km > sil_gmm else "GMM")
plt.bar(["KMeans", "GMM"], [sil_km, sil_gmm])
plt.title("Silhouette Score Comparison")
plt.ylabel("Silhouette Score")
plt.show()

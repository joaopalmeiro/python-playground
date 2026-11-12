import time

import faiss
import numpy as np
from faiss.contrib.e_means import NumpyEmeans
from sklearn.datasets import make_blobs
from sklearn.metrics import adjusted_rand_score

N_INSTANCES = 10_000_000
N_FEATURES = 2
N_CLUSTERS = 5
SEED = 0


if __name__ == "__main__":
    x, y_true = make_blobs(n_samples=N_INSTANCES, n_features=N_FEATURES, centers=N_CLUSTERS, random_state=SEED)
    x = x.astype(np.float32)

    em = NumpyEmeans(N_FEATURES, N_CLUSTERS, seed=SEED)
    t0 = time.perf_counter()
    _, y_em = em.train(x)
    t_em = time.perf_counter() - t0

    km = faiss.Kmeans(N_FEATURES, N_CLUSTERS, seed=SEED, max_points_per_centroid=N_INSTANCES)
    t0 = time.perf_counter()
    km.train(x)
    _, y_km = km.assign(x)
    t_km = time.perf_counter() - t0

    print(f"e-means: {t_em:.2f}s, ARI {adjusted_rand_score(y_true, y_em):.4f}")
    print(f"k-means: {t_km:.2f}s, ARI {adjusted_rand_score(y_true, y_km.ravel()):.4f}")

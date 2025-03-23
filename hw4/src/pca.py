import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from tqdm import tqdm
from collections import defaultdict

np.random.seed(4300)
scaler = StandardScaler()

img_ori = None
with open("train_img") as f :
    img_ori = np.array([list(map(float, line.split(','))) for line in tqdm(f.readlines())])
img_ori = scaler.fit_transform(img_ori)

cen_ori = None
with open("random_seed_1") as f :
    cen_ori = np.array([list(map(float, line.split(','))) for line in f.readlines()])
cen_ori = scaler.fit_transform(cen_ori)

for M in [4, 8, 16, 32, 64] :
    print("M =", M)

    pca = PCA(n_components=M)
    img = pca.fit_transform(img_ori)

    print("Energy Kept:", sum(pca.explained_variance_**2))

    xaxis = range(1, M+1)
    plt.plot(xaxis, pca.explained_variance_)
    plt.xlabel("Component Number")
    plt.ylabel("Eigenvalue")
    plt.xticks(xaxis, range(1, M+1))
    plt.show()

    cen = pca.transform(cen_ori)
    kmeans = KMeans(n_clusters=10, init=cen, tol=.05)
    kmeans.fit(img)

    print()

    labels = None
    with open("train_label") as f :
        labels = [int(line.strip()) for line in f.readlines()]

    cen_count = [defaultdict(lambda: 0) for _ in range(10)]
    for i in range(60000) :
        cen_count[kmeans.labels_[i]][labels[i]] += 1
    for i in range(10) :
        count = cen_count[i]
        label = None
        for key in count :
            if count[key] == max(count.values()) :
                label = key
                break
        print("Centroid", i, ":")
        print("Major label of the cluster:", label)
        print("# Train images belonging to the cluster:", sum(count.values()))
        print("# Correctly clustered images:", count[label])
        print("Classification Accuracy:", count[label]/sum(count.values()))
        print()

    print()
    print()

with open("pca_components_64", 'w') as f :
    for eigenvec in pca.components_ :
        f.write(','.join(map(str, eigenvec)) + '\n')

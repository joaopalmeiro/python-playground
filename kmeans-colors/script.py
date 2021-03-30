import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


class DominantColors:
    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters=5):
        self.CLUSTERS = clusters
        self.IMAGE = image

    def dominantColors(self):
        img = cv2.imread(self.IMAGE)

        # Convert from BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img = img.reshape((img.shape[0] * img.shape[1], img.shape[2]))

        self.IMAGE = img

        # Use k-means to cluster pixels
        kmeans = KMeans(n_clusters=self.CLUSTERS)
        kmeans.fit(img)

        # Dominant colors
        self.COLORS = kmeans.cluster_centers_

        # Labels of each point/pixel
        self.LABELS = kmeans.labels_

        return self.COLORS.astype(int)

    def rgb_to_hex(self, rgb):
        # 2-digit hexadecimal number (missing digits are padded with zeroes)
        return "#%02x%02x%02x" % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

    def plotHistogram(self):
        num_labels = np.arange(0, self.CLUSTERS + 1)

        # Create frequency count tables
        hist, _ = np.histogram(self.LABELS, bins=num_labels)
        hist = hist.astype("float")
        hist /= hist.sum()
        # or
        # hist, _ = np.histogram(self.LABELS, bins=num_labels, density=True)

        colors = self.COLORS
        print((hist).argsort())

        # plt.savefig('hist.png', bbox_inches='tight')


img = "colors.jpeg"
dc = DominantColors(img)

colors = dc.dominantColors()
# print(colors)

dc.plotHistogram()

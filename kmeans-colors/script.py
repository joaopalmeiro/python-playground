import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


class DominantColors:
    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None
    DPI = None
    COOLORS_BASE_URL = "https://coolors.co/"

    def __init__(self, image, clusters=5, dpi=320):
        self.CLUSTERS = clusters
        self.IMAGE = image
        self.DPI = dpi

    def dominant_colors(self):
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

    @staticmethod
    def rgb_to_hex(rgb, prefix="#"):
        # 2-digit hexadecimal number (missing digits are padded with zeroes)
        return "%s%02x%02x%02x" % (prefix, int(rgb[0]), int(rgb[1]), int(rgb[2]))

    def to_coolors(self):
        colors = "-".join(self.rgb_to_hex(color, prefix="") for color in self.COLORS)

        return f"{self.COOLORS_BASE_URL}{colors}"

    def plot_histogram(self):
        num_labels = np.arange(0, self.CLUSTERS + 1)

        # Create frequency count tables
        hist, _ = np.histogram(self.LABELS, bins=num_labels)
        hist = hist.astype("float")
        hist /= hist.sum()
        # or
        # hist, _ = np.histogram(self.LABELS, bins=num_labels, density=True)

        # Frequency count in descending order
        sorting_criteria = (-hist).argsort()

        colors = self.COLORS[sorting_criteria]
        hist = hist[sorting_criteria]

        # Create empty chart
        chart = np.zeros((50, 500, 3), np.uint8)  # Unsigned integer (0 to 255)
        start = 0

        # Create color rectangles
        for i in range(self.CLUSTERS):
            end = start + hist[i] * 500

            r = colors[i][0]
            g = colors[i][1]
            b = colors[i][2]

            # print(help(cv2.rectangle))

            # (X-coordinate, Y-coordinate)
            # Thickness of -1 px will fill the rectangle shape by the specified color
            cv2.rectangle(
                img=chart,
                pt1=(int(start), 0),
                pt2=(int(end), 50),
                color=(r, g, b),
                thickness=-1,
            )
            start = end

        fig = plt.figure()
        plt.axis("off")
        plt.imshow(chart)
        # plt.show()
        fig.savefig("hist.png", dpi=self.DPI, bbox_inches="tight")


img = "colors.jpeg"
dc = DominantColors(img)

colors = dc.dominant_colors()
# colors = [dc.rgb_to_hex(color) for color in colors]
print("Colors (RGB):", colors, sep="\n")
print(f"\n{dc.to_coolors()}")

dc.plot_histogram()

import numpy as np
import xy

if __name__ == "__main__":
    rng = np.random.default_rng(0)
    x = rng.normal(size=10_000_000)
    y = x * 0.6 + rng.normal(scale=0.8, size=x.size)

    density_chart = xy.scatter_chart(
        xy.scatter(x, y, size=4, density=True),
        xy.x_axis(label="x"),
        xy.y_axis(label="y"),
        title="10M density scatter",
    )

    density_chart.to_html("density_scatter.html")

    chart = xy.scatter_chart(
        xy.scatter(x, y, size=4, density=False),
        xy.x_axis(label="x"),
        xy.y_axis(label="y"),
        title="10M scatter",
    )

    chart.to_html("scatter.html")

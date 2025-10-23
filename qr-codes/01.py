import qrcode

CODES = [
    {
        "id": "biy",
        "url": "https://research.feedzai.com/publication/benchmark-it-yourself-biy-preparing-a-dataset-and-benchmarking-ai-models-for-scatterplot-related-tasks/",
    }
]

# Source: https://github.com/lincolnloop/python-qrcode/blob/v8.2/qrcode/main.py#L82
DEFAULT_BOX_SIZE = 10

if __name__ == "__main__":
    for code in CODES:
        qr = qrcode.QRCode(box_size=DEFAULT_BOX_SIZE * 3)

        qr.add_data(code["url"])

        img = qr.make_image(fill_color="white", back_color="transparent")

        img.save(f"{code['id']}.png")

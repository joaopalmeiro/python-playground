import base64
import json
import struct

if __name__ == "__main__":
    with open("dev.ipynb", "r") as fp:
        nb = json.load(fp)

    output = nb["cells"][1]["outputs"][0]

    base64_img = output["data"]["image/png"]
    binary_img = base64.b64decode(base64_img)

    w, h = struct.unpack(">LL", binary_img[16:24])
    print(f"Width: {w}; Height: {h}")

    scaleFactor = output["metadata"]["application/vnd.vegalite.v4+json"][
        "embed_options"
    ]["scaleFactor"]
    print(f"scaleFactor (metadata): {scaleFactor}")

    with open("via_embedded_image.png", "wb") as fp:
        fp.write(base64.b64decode(base64_img))

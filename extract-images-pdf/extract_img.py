import fitz

# https://pymupdf.readthedocs.io/en/latest/
# https://pymupdf.readthedocs.io/en/latest/module.html
# https://pymupdf.readthedocs.io/en/latest/document.html#Document.get_page_images
# https://pymupdf.readthedocs.io/en/latest/document.html#other-examples
# https://stackoverflow.com/a/47877930
# https://github.com/pymupdf/PyMuPDF
if __name__ == "__main__":
    doc = fitz.open("2107.11367.pdf")

    for i in range(doc.page_count):
        imglist = doc.get_page_images(i)

        for img in imglist:
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)

            filename = f"p{i}-{xref}.png"
            print(filename)

            if pix.n - pix.alpha < 4:
                pix.save(filename)
            else:  # CMYK
                pix0 = fitz.Pixmap(fitz.csRGB, pix)
                pix0.save(filename)
                pix0 = None
                
            pix = None  # Free Pixmap resources.

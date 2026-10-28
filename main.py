import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def create_searchable_pdf(image_path, output_pdf_path, lang="eng"):
    pdf_bytes = pytesseract.image_to_pdf_or_hocr(image_path, lang=lang, extension="pdf")
    with open(output_pdf_path, "wb") as f:
        f.write(pdf_bytes)
    print(f"сохранил {output_pdf_path}")


if __name__ == "__main__":
    create_searchable_pdf("document2.jpeg", "result_exact2.pdf")

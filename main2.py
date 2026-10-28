from pdf2image import convert_from_path
import pytesseract
from docx import Document

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
poppler_path = r"c:\poppler\poppler-25.12.0\Library\bin"


def pdf_to_docx(pdf_path, docx_path, lang="rus+eng"):
    pages = convert_from_path(pdf_path, 300, poppler_path=poppler_path)
    doc = Document()

    for i, page in enumerate(pages):
        print(f"страница {i + 1} из {len(pages)}")
        text = pytesseract.image_to_string(page, lang=lang)
        doc.add_paragraph(text)
        if i < len(pages) - 1:
            doc.add_page_break()

    doc.save(docx_path)
    print(f"сохранил {docx_path}")


if __name__ == "__main__":
    pdf_to_docx("result_exact.pdf", "output.docx")

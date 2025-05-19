from pdfminer.high_level import extract_text
from docx import Document

def parse_pdf(path):
    return extract_text(path)

def parse_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def parse_txt(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

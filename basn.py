#pip install pymupdf python-docx
import fitz
import docx
from docx.shared import Inches

def extract_text_from_pdf(pdf_path, word_path):

    try:
        pdf_document = fitz.open(pdf_path)
        doc = docx.Document()

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)

            text = page.get_text()
            if text:
                doc.add_paragraph(text)
        image_list = page.get_images()

        for img_ind, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_pytes  = base_image["image"]
            image_ext = base_image["ext"]

            image_path_temp = f"image_{img_ind}.{image_ext}"


    except Exception as e:
         pass

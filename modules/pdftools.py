import PyPDF2
import re

def extract_and_clean_pdf_text(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            
            extracted_text = ""
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                extracted_text += page_text
                
        cleaned_text = clean_text(extracted_text)
        return cleaned_text
    except Exception as e:
        return str(e)

def clean_text(text):
    # Remove non-ASCII characters, newlines, and tabs
    cleaned_text = re.sub(r'[^\x00-\x7F]+', '', text)
    cleaned_text = cleaned_text.replace('\n', ' ').replace('\t', ' ')
    return cleaned_text

# Usage
if __name__ == '__main__':
    pdf_path = 'path_to_your_pdf.pdf'
    extracted_text = extract_and_clean_pdf_text(pdf_path)
    print(extracted_text)

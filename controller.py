from pypdf import PdfMerger

def merge_pdfs(pdfs, pdf_name):
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf['name'])

    merger.write(pdf_name)
    merger.close()
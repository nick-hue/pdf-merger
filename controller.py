from pypdf import PdfMerger

def merge_pdfs(pdfs, pdf_name):
    merger = PdfMerger()

    for pdf in pdfs:
        # check all files are pdfs
        merger.append(pdf)

    merger.write(pdf_name)
    merger.close()
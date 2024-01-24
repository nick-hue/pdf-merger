from pypdf import PdfMerger

def merge_pdfs(pdfs):
    merger = PdfMerger()


    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()
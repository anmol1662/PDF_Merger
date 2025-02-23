from PyPDF2 import PdfMerger


# By appending in the end
def by_appending():
    merger = PdfMerger()
    # Either provide file stream
    f1 = open("samplePdf1.pdf", "rb")
    merger.append(f1)
    # Or direct file path
    merger.append("samplePdf2.pdf")

    merger.write("mergedPdf.pdf")


# By inserting at after an specified page no.
# def by_inserting():
#     merger = PdfMerger()
#     merger.append("samplePdf1.pdf")
#     merger.merge(0, "samplePdf2.pdf")
#     merger.write("mergedPdf1.pdf")


if __name__ == "__main__":
    by_appending()
    # by_inserting()
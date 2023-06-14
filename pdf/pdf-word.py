from pdf2docx import parse


class pdf(object):
    def __init__(self):
        """pdf 转换word """
        self.pdf_file = ""
        self.word_file = ""

    def convert(self):
        parse(self.pdf_file, self.word_file)
        return self.word_file


if __name__ == '__main__':
    pdf = pdf()
    pdf.convert()

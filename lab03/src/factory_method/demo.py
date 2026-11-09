from .creators import PdfCreator, HtmlCreator
def run():
    text = "Отчёт о результатах работы"
    pdf_creator = PdfCreator()
    html_creator = HtmlCreator()
    print(pdf_creator.export_document(text))
    print(html_creator.export_document(text))
if __name__ == "__main__":
            run()
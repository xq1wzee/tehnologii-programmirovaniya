from abc import ABC, abstractmethod
class DocumentExporter(ABC):
    @abstractmethod
    def export(self, text: str) -> str:
        pass
class PdfExporter(DocumentExporter):
    def export(self, text: str) -> str:
        return f"Экспорт в PDF: {text}"
class HtmlExporter(DocumentExporter):
    def export(self, text: str) -> str:
        return f"Экспорт в HTML: <p>{text}</p>"
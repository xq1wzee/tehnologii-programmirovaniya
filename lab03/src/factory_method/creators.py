from abc import ABC, abstractmethod
from exporters import DocumentExporter, PdfExporter, HtmlExporter
class ExporterCreator(ABC):
    @abstractmethod
    def create_exporter(self) -> DocumentExporter:
        pass
    def export_document(self, text: str) -> str:
        exporter = self.create_exporter()
        return exporter.export(text)
class PdfCreator(ExporterCreator):
    def create_exporter(self) -> DocumentExporter:
        return PdfExporter()
class HtmlCreator(ExporterCreator):
    def create_exporter(self) -> DocumentExporter:
        return HtmlExporter()
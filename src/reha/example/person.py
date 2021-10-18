from uvcreha.contents import documents_store
from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from uvcreha.browser.document import (
    DefaultDocumentEditForm,
    DocumentEdit,
    DefaultDocumentPDF,
    PDFView,
)
from reha.example import TEMPLATES
import io


from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


@dataclass
class Person(JsonSchemaMixin):

    name: str = field(
        metadata=dict(title="The age of the user", description="do not lie!")
    )
    surname: str
    age: int


documents_store.add("person", Person.json_schema())


@DocumentEdit.component("person.1.0")
class CTDocumentEditForm(DefaultDocumentEditForm):
    template = TEMPLATES["person_edit.pt"]


@PDFView.component("person.1.0")
class PersonPdf(DefaultDocumentPDF):

    def generate_pdf(self, context):
        pdf = Document()
        page = Page()
        pdf.append_page(page)
        layout = SingleColumnLayout(page)
        layout.add(Paragraph("Hello World!"))
        layout.add(Paragraph(context.item))
        stream = io.BytesIO()
        PDF.dumps(stream, pdf)
        stream.seek(0)
        return stream

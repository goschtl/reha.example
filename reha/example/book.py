"""Main module."""
from uvcreha.contents import documents_store
from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from uvcreha.browser.document import DefaultDocumentEditForm, DocumentEdit
from reha.example import TEMPLATES


@dataclass
class Book(JsonSchemaMixin):

    name: str = field(
        metadata=dict(title="The age of the user", description="do not lie!")
    )
    isbn: str
    pages: int


documents_store.add("Book", Book.json_schema())


@DocumentEdit.component('Book.1.0')
class CTDocumentEditForm(DefaultDocumentEditForm):
    template = TEMPLATES['mytest.pt']

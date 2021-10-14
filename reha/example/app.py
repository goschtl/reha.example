"""Main module."""

from fanstatic import Resource, Library
from uvcreha.browser import Page, routes, action
from uvcreha.browser.form import FormView
from uvcreha.browser.composed import ComposedView
from uvcreha import events
from reha.prototypes.events import (
    WorkflowTransitionEvent,
    ObjectModifiedEvent,
    ObjectAddedEvent,
)
from reha.prototypes.workflows.document import document_workflow
from reha.prototypes.workflows.file import file_workflow
from reha.example import TEMPLATES
from reha.prototypes.contents import File


library = Library("reha.example", "static")


@routes.register("/test")
class TestView(Page):

    template = TEMPLATES["test_views.pt"]

    def GET(self):
        return dict(request=self.request)


@events.subscribe(ObjectAddedEvent)
def handle_wf(event):
    print(event)


@events.subscribe(ObjectAddedEvent, obj=File)
def handle_file_wf(event):
    ct, crud = event.request.get_crud("file")
    crud.update(event.obj, {"state": file_workflow.states.validated.name})


from uvcreha.contents import documents_store
from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class Person(JsonSchemaMixin):

    name: str = field(
        metadata=dict(title="The age of the user", description="do not lie!")
    )
    surname: str
    age: int


documents_store.add("person", Person.json_schema())

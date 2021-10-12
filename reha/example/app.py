"""Main module."""

from fanstatic import Resource, Library
from uvcreha.browser import Page, routes, action
from uvcreha.browser.form import FormView
from uvcreha.browser.composed import ComposedView
from uvcreha import events
from reha.prototypes.events import WorkflowTransitionEvent, ObjectModifiedEvent
from reha.prototypes.workflows.document import document_workflow
from reha.example import TEMPLATES


library = Library('reha.example', 'static')


@routes.register("/test")
class TestView(Page):

    template = TEMPLATES["test_views.pt"]

    def GET(self):
        import pdb; pdb.set_trace()
        return dict(request=self.request)




@events.subscribe(ObjectModifiedEvent)
def handle_wf(event):
    print(event)



from uvcreha.contents import documents_store
from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin

@dataclass
class Person(JsonSchemaMixin):

    name: str = field(metadata=dict(title='The age of the user', description='do not lie!'))
    surname: str
    age: int

documents_store.add('person', Person.json_schema())

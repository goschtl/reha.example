
from uvcreha.contents import documents_store
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

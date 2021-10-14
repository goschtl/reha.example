import uvcreha._api as api
from reha.example import TEMPLATES
from wtforms import Form, StringField, TextAreaField, validators


class MyForm(api.Form):
    name = StringField(u"Full Name", [validators.required(), validators.length(max=10)])
    address = TextAreaField(
        u"Mailing Address", [validators.optional(), validators.length(max=200)]
    )


@api.routes.register("/testform")
class TestForm(api.FormView):
    def setupForm(self, data=None, formdata=None):
        form = MyForm()
        form.process(data=data, formdata=formdata)
        return form

    @api.action(title="Save", css="btn btn-primary")
    def handle_save(self, data):
        form = self.setupForm(formdata=data.form)
        if not form.validate():
            return dict(form=form)
        print(data)





from uvcreha.browser.document import DefaultDocumentEditForm, DocumentEdit


@DocumentEdit.component('person.1.0')
class CTDocumentEditForm(DefaultDocumentEditForm):
    template = TEMPLATES['mytest.pt']

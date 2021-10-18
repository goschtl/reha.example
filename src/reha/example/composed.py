

from uvcreha import _api as api


@api.routes.register('/composed')
class CP(api.ComposedView):
    title="CP"
    description="Description"

    def get_name(self):
        return self.request.query.get('page', default="t1")


@CP.pages.register('t1')
class T1(api.Page):
    title="T1"

    def GET(self):
        return u"HALLO WELT T1"


@CP.pages.register('t2')
class T2(api.Page):
    title="T2"

    def GET(self):
        return u"HALLO WELT T2"


@CP.pages.register('t3')
class T3(api.FormView):
    title="T3"

    def setupForm(self):
        return api.Form()

    @api.action('Speichern')
    def handle_save(self, data):
        return


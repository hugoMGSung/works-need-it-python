import falcon

class HelloResource(object):
    def on_get(self, req, resp):
        resp.media = {'message': 'Hello, World!'}

app = falcon.App()
hello_resource = HelloResource()

app.add_route('/hello', hello_resource)
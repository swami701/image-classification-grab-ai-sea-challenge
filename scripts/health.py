import flask_restful
import mixins


class Ping(flask_restful.Resource, mixins.RegisterableMixin):

    url = '/health'

    def get(self):
        return {'status': 'true'}

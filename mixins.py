import os


class RegisterableMixin(object):
    @classmethod
    def register(cls, api):
        namespace = os.getenv('NAMESPACE', '')
        if namespace != '':
            namespace = '/{}'.format(namespace)
        api.add_resource(cls, namespace + cls.url)

import mixins
import importlib
import inspect
import os
import pkgutil


def dynamically_register_resources(api):
    path = os.path.join(os.path.dirname(__file__), 'scripts')
    module_path = 'scripts'
    for _, name, _ in pkgutil.walk_packages(path=[path]):
        module = importlib.import_module(
            '%s.%s' % (module_path, name))
        for _, obj in inspect.getmembers(module):
            if (inspect.isclass(obj) and
                    issubclass(obj, mixins.RegisterableMixin) and
                    obj != mixins.RegisterableMixin):
                obj.register(api)

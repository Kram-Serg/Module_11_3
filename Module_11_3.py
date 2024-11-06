from pprint import pprint


def introspection_info(obj):
    inf_obj = {'type':type(obj), 'attributes': [att for att in dir(obj) if not att.startswith('__')], 'metods': [method for method in dir(obj)
            if callable(getattr(obj, method))], 'module': obj.__class__.__module__}
    return inf_obj


class Info_class:
    def name(self):
        pass




number_info = introspection_info(42)
class_info = introspection_info(Info_class)
func_info = introspection_info(Info_class.name)

pprint(number_info)
pprint(class_info)
pprint(func_info)

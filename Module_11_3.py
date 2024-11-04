
def introspection_info(obj):
    inf_obj = {'type':type(obj), 'attributes': dir(obj), 'metods': [method for method in dir(obj)
            if callable(getattr(obj, method))], 'module': obj.__class__.__module__}
    return inf_obj


class Info_class:
    def name(self):
        pass




number_info = introspection_info(42)
class_info = introspection_info(Info_class)
func_info = introspection_info(Info_class.name)

print(number_info)
print(class_info)
print(func_info)

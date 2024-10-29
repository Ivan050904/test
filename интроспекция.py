import inspect


def introspection_info(obj):
    slovar = {}
    slovar['type'] = type(obj)
    slovar.update({'attributes':dir(obj),'модуль':inspect.getmodule(introspection_info)})
    return slovar

number_info = introspection_info(42)
print(number_info)
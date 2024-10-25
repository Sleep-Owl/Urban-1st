from inspect import getmodule


def introspection_info(obj):
    info = {'type': type(obj),
            'atribute': dir(obj),
            'methods_has': hasattr(obj, '__name__'),
            'methods_get': getattr(obj, '__name__', 'Not have name'),
            'module': getmodule(obj)}

    if isinstance(obj, (list, tuple)):
        info['length'] = len(obj)
    elif isinstance(obj, dict):
        info['keys'] = list(obj.keys())

    return info


number_info = introspection_info(42)
for key, value in number_info.items():
    print(f"{key}: {value}", end='\n')

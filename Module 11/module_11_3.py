from inspect import getmodule


def introspection_info(obj):
    info = {
        'type': type(obj),
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': None,
        'class': getattr(obj, '__class__', None),
        'init': getattr(obj, '__init__', None),
        'length': len(obj) if hasattr(obj, '__len__') else None,
        'values': getattr(obj, 'values', None)
    }

    if hasattr(obj, '__module__'):
        info['module'] = getattr(obj, '__module__')

    return info


number_info = introspection_info(42)
for key, value in number_info.items():
    print(f"{key}: {value}", end='\n')

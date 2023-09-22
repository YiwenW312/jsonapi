import json


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {
                "__complex__": True,
                "a": obj.real,
                "b": obj.imag
            }
        return super().default(obj)


class ComplexDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook,
                                  *args, **kwargs)

    def object_hook(self, dct):
        if "__complex__" in dct:
            return complex(dct["a"], dct["b"])
        return dct


def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=ComplexEncoder, *args, **kwargs)


def loads(s, *args, **kwargs):
    return json.loads(s, cls=ComplexDecoder, *args, **kwargs)

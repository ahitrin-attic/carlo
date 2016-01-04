class ModelException(Exception):
    pass

class Model(object):
    def __init__(self, *entities):
        self.entities = entities

    def restricted_by(self, *args):
        return self

    def build(self):
        names = [e[0] for e in self.entities]
        if len(names) != len(set(names)):
            raise ModelException()
        return FrozenModel(self.entities)


class FrozenModel(object):
    def __init__(self, entities):
        self.entities = entities

    def create(self):
        result = list()
        for name, params in self.entities:
            resolved_params = dict()
            for param_name, param_fn in params.iteritems():
                resolved_params[param_name] = param_fn()
            result.append((name, resolved_params))
        return result

def int_val():
    pass

def string_val():
    pass

def time_val():
    pass

def eq(first, second):
    pass

def ge(first, second):
    pass

def cardinal_many(*args):
    pass

def generate(model, amount):
    pass

class Model(object):
    def __init__(self, *entities):
        self.entities = entities

    def restricted_by(self, *args):
        return self

    def build(self):
        return FrozenModel(self.entities)


class FrozenModel(object):
    def __init__(self, entities):
        self.entities = entities

    def create(self):
        result = list()
        for name, params in self.entities:
            result.append((name, {
                        params.keys()[0]: params.values()[0]()}))
        return result

def model(*args):
    return Model(*args)

def entity(name, values):
    return (name, values)

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

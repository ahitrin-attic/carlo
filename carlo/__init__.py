class Model(object):
    def __init__(self, *entities):
        self.entities = entities

    def restricted_by(self, *args):
        return self

    def build(self):
        pass

    def create(self):
        name, params = self.entities[0]
        return [(name, {
                    params.keys()[0]: params.values()[0]()})]

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

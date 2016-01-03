class Model(object):
    def restricted_by(self, *args):
        return self

    def build(self):
        pass

def model(*args):
    return Model()

def entity(name, values):
    pass

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

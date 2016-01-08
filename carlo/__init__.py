import logpy


class ModelException(Exception):
    pass


class Model(object):
    def __init__(self, **entities):
        self.entities = entities
        self.restrictions = list()

    def restricted_by(self, *args):
        self.restrictions.extend(args)
        return self

    def build(self):
        self._validate()
        return FrozenModel(self.entities, self.restrictions)

    def _validate(self):
        variables = dict()
        conditions = list()
        for name, params in self.entities.iteritems():
            for param_name, param in params.iteritems():
                full_name = '.'.join([name, param_name])
                v = logpy.var()
                variables[full_name] = v
                conditions.append(logpy.eq(v, param[0]))
        for first, second in self.restrictions:
            fv = variables[first]
            sv = variables[second]
            conditions.append(logpy.eq(fv, sv))
        ok = logpy.run(1, variables.values()[0], *conditions)
        if not ok:
            raise ModelException()


class FrozenModel(object):
    def __init__(self, entities, restrictions):
        self.entities = entities
        self.restrictions = {v:k for (k, v) in restrictions}

    def create(self):
        ready_values = dict()
        result = list()
        for name, params in self.entities.iteritems():
            for param_name, param in params.iteritems():
                full_name = '.'.join([name, param_name])
                ready_values[full_name] = param[1]()
        for name, params in self.entities.iteritems():
            resolved_params = dict()
            for param_name in params.keys():
                full_name = '.'.join([name, param_name])
                if full_name in self.restrictions:
                    full_name = self.restrictions[full_name]
                resolved_params[param_name] = ready_values[full_name]
            result.append((name, resolved_params))
        return result

def int_val(fixed_value=None):
    return ('int', lambda: fixed_value)

def string_val(fixed_value=None):
    return ('str', lambda: fixed_value)

def time_val():
    pass

def eq(first, second):
    return (first, second)

def ge(first, second):
    pass

def cardinal_many(*args):
    pass

def generate(model, amount):
    pass

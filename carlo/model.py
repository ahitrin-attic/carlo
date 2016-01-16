from .common import ModelException
import sympy


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
        used_variabled = list()
        for name, params in self.entities.iteritems():
            for param_name, param in params.iteritems():
                full_name = '.'.join([name, param_name])
                variables[full_name] = param[0]
        for first, second in self.restrictions:
            first_type = variables[first]
            second_type = variables[second]
            first_var, second_var = sympy.symbols(' '.join([first, second]))
            conditions.extend([first_var - first_type,
                second_var - second_type, first_var - second_var])
            used_variabled.extend([first_var, second_var])
        if conditions:
            ok = sympy.solve(conditions, used_variabled)
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

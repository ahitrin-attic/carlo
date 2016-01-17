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
                variables[full_name] = dict()
                constraints = param[1]
                for k, v in constraints.iteritems():
                    var = sympy.symbols('.'.join([full_name, k]))
                    variables[full_name][k] = (var, v)
                    conditions.append(var - v)
                    used_variabled.append(var)
        for first, second in self.restrictions:
            for key in [k for k in variables[first] if k in variables[second]]:
                first_var = variables[first][key][0]
                second_var = variables[second][key][0]
                conditions.append(first_var - second_var)
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
                ready_values[full_name] = param[0]()
        for name, params in self.entities.iteritems():
            resolved_params = dict()
            for param_name in params.keys():
                full_name = '.'.join([name, param_name])
                if full_name in self.restrictions:
                    full_name = self.restrictions[full_name]
                resolved_params[param_name] = ready_values[full_name]
            result.append((name, resolved_params))
        return result

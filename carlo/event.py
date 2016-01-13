def generate(model, amount):
    def wrap(n):
        for i in range(n):
            yield model.create()
    return [y for x in wrap(amount) for y in x]

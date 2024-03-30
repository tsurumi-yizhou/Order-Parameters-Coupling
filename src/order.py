from atom import Atom


class Order:
    def __init__(self, element: str, plus: set[Atom], minus: set[Atom]):
        self.element = element
        self.plus = plus
        self.minus = minus

    def operate(self, rotation: list[Atom]):
        new_plus, new_minus = [], []
        for atom in self.plus:
            new_plus.append(atom.operate(rotation))
        for atom in self.minus:
            new_minus.append(atom.operate(rotation))
        self.plus, self.minus = new_plus, new_minus

    def __eq__(self, other):
        return self.plus == other.plus and self.minus == other

    def __neg__(self):
        return Order(self.element, self.minus, self.plus)

    def __pos__(self):
        return Order(self.element, self.plus, self.minus)



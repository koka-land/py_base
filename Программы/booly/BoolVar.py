class BoolVar:
    def __init__(self, value):
        self.value = value
        # print("INIT =", value)

    def __neg__(self):
        return BoolVar(not self.value)

    def __add__(self, other):
        return BoolVar(self.value or other.value)

    def __mul__(self, other):
        return BoolVar(self.value and other.value)

    def __gt__(self, other):
        return BoolVar((not self.value) or other.value)

    def __eq__(self, other):
        return BoolVar(self.value == other.value)

    def __str__(self):
        return "True" if self.value else "False"

    def __format__(self, format_spec):
        return format(str(self), format_spec)
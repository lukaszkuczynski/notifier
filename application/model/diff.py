class Diff:

    def __init__(self, value):
        self.value = value

    def changed(self):
        return len(self.value) > 0

    def first_element(self):
        if len(self.value) < 1:
            raise Exception('Cannot get first element of empty list')
        return self.value[0]

    def all_changes(self):
        return self.value
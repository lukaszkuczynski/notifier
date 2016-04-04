class Element:

    def add_key_value(self, key, value):
        self.__dict__[key] = value

    def __str__(self):
        return self.__dict__.__str__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        hash_value = 1
        for key in self.__dict__.keys():
            hash_value ^= hash(key)
        return hash_value

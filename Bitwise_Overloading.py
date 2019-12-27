# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
class Bits_Ovrlod():
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Bits_Ovrlod):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Bits_Ovrlod):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Bits_Ovrlod):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Bits_Ovrlod):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, Bits_Ovrlod):
            return self.value >> obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value


if __name__ == "__main__":
    a = Bits_Ovrlod(20)
    b = Bits_Ovrlod(22)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)

# Python 3.5.2

from my_class import MyClass


def function(name):
    c = MyClass()
    return c.my_method(name)


if __name__ == '__main__':
    print(function('Python'))

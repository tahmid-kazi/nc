# 2/2/25) 1010-1012pm) Sun)

class A:
    def print_method(self) -> None:
        print("A")

class B(A):
    def print_method(self) -> None:
        print("B")

class C(A):
    def print_method(self) -> None:
        print("C")

class D(B, C):  # This order matters, MRO = Method Resolution order
    pass


# Do not change the code below
d = D()
d.print_method()

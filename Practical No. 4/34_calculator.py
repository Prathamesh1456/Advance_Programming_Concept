class Calculator:

    def add(self, a, b, c=0, d=0):
        return a + b + c + d


calculator = Calculator()

print("Addition of two numbers:", calculator.add(10, 20))
print("Addition of three numbers:", calculator.add(10, 20, 30))
print("Addition of four numbers:", calculator.add(10, 20, 30, 40))
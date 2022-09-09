class IsolationIntervalFinder:
    def __init__(self, fun, a, b, e):
        self.function = fun.lower()
        self.a = a
        self.b = b
        self.e = e
        self.iteration = 1

    def get_middle_point(self):
        return (self.a + self.b) / 2

    def get_x_point_value(self, x):
        point_function = self.function.replace("x", f"({x})")
        return eval(point_function.split("=")[0])

    def do_iteration(self):
        middle = self.get_middle_point()
        if self.get_x_point_value(middle) * self.get_x_point_value(self.a) < 0:
            self.b = middle
        else:
            self.a = middle
        print(f"Iteration.{self.iteration}: {self.a, self.b}")

    def find(self):
        while abs(self.a - self.b) >= self.e:
            self.do_iteration()
            self.iteration += 1
        print(f"Answer: {self.a, self.b}")


function = input("Enter your function: ")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
e = float(input("Enter e: "))
i = IsolationIntervalFinder(function, a, b, e)
i.find()

# x ** 3 + x ** 2 - 1
# x ** 3 - 0.2 * x ** 2 + 0.5 * x + 1.5

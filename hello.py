import requests


class Person:
    hands = 2

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Employee(Person):

    def __init__(self, salary, name):
        super().__init__(name)
        self.salary = salary

    def get_adder(self, adder):
        return requests.get(adder)


if __name__ == '__main__':
    p = Employee(5000, 'ben')
    print(p.get_adder('https://www.apple.com').text, p.get_name(), p.salary)



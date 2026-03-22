class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} is in {self.house}"
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is empty")
        self.__name = name
    @property
    def house(self):
        return self.__house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "School"]:
            raise ValueError("There is no such house in the list")
        self.__house = house
    @classmethod
    def smth(cls):
        print("This is class method")

def main():
    harry = Student("Harry", "Gryffindor")
    print(harry)
    print(harry.name)
    harry.name = "daun"
    print(harry.name)
    Student.smth()
if __name__ == "__main__":
    main()

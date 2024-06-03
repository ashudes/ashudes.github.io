class Vehicle:
    def __init__(self, color, registration_number):
        self.color = color  ## This is an unprotected variable
        self._registration_number = registration_number  ## This is a semi-private/"protected" variable

    def get_color(self):
        return self.color

    def _get_registration_number(self):
        return self._registration_number

## Create an object of Vehicle
car = Vehicle("Red", "XYZ 1234")

## Accessing unprotected variable
print(car.color)  ## Output: Red

## Accessing unprotected method
print(car.get_color())  ## Output: Red

## protected variables or semi-private variables/methods should not be accessed directly
print(car._registration_number)  ## Output: XYZ 1234
print(car._get_registration_number())  ## Output: XYZ 1234

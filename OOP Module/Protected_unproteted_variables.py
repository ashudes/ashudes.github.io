class MyClass:
    def __init__(self):
        self.public_var = "I'm public!"  ## This is a public variable
        self._semi_private_var = "I'm semi-private!"  ## This is a semi-private/"protected" variable

    def public_method(self):
        return self.public_var

    def _semi_private_method(self):
        return self._semi_private_var

## Create an object of MyClass
obj = MyClass()

## Accessing public variable
print(obj.public_var)  ## Output: I'm public!

## Accessing public method
print(obj.public_method())  ## Output: I'm public!
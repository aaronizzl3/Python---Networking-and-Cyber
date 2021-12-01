class MyClass:
  __name = "Aaron"

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value


# Create Object
myObject = MyClass()

# Use Property (Getter)
print(myObject.name)

# Use Property (Setter)
myObject.name = "Dean"
print(myObject.name)

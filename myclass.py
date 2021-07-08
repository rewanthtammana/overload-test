class Random:
  def __init__(self) -> None:
      self.x = "5"
  def hello(self):
    self.x =  "6"
  def __str__(self) -> str:
      return "value of x = " + self.x

# p1 = MyClass()
# print(p1)

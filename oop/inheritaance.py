# class Parent:
#     def speak(self):
#       print("I can speak")

# class child(Parent):
#    pass

# print(child)

# multiple inheritance
class father:
    def show(self, name):
      self.name= name
    
class child(father):
  def show(self):
     print(f"my name is {self}")


obj= child()
obj.show("Hamza")

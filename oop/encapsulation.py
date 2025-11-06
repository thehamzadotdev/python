class Example:
    def __init__(self):
        self.public = "Public Variable"
        self._protected = "Protected Variable"
        self.__private = "Private Variable"

obj = Example()

print(obj.public)       # ✅ Accessible
print(obj._protected)   # ⚠️ Accessible but not recommended
print(obj.__private)    # ❌ Error — can't access directly







class student:
    def __init__(self, name, marks):
        self.name= name
        self.__marks= marks
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        if marks>= 0 and marks <=100:
            self.__marks =marks
        else:
            print("invalid marks")
s= student("hamza", 85)
print(s.get_marks())

s.set_marks(95)
print(s.get_marks())

s.set_marks(105)
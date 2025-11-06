class animal:
    def sound(self):
        print("animal make sounds")


class dog(animal):
    def sound(self):
        print("dog barks")


obj = dog()

obj.sound()
from enum import auto
i=0
class Person:
    def __init__(self, name):
        global i
        self.id = i
        self.name = name
        i+=1

    def __str__():
        print (self.id , self.name)

class PersonFactory:
    def create_person(self, name):
        # todo
        return Person(name)



p1 = PersonFactory()
p2 = PersonFactory()

hi  = p1.create_person(name ="anupam")
there = p2.create_person(name = "pandey")
print (hi.id)
print (there.id)
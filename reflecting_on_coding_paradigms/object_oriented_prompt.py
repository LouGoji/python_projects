class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price




    def repair(self):
        self.condition = "repaired"



class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2





class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super.init(max_speed, condition, price)

    def flame_jet(self, other):
        other.condition = "trashed"


'''
Make sure to answer the following prompts about your coding experience:
Q: How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
A:  Abstraction, Encapsulation, Inheritance, Polymorphism.

Q:Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
A: Probably not because of the easiness of reusing the code through inheritance. 
    
Q:How in particular did Object Oriented Programming assist in the solving of this problem?
A: Object-oriented programming is ultimately about taking a huge problem and breaking it down to solvable chunks.
'''
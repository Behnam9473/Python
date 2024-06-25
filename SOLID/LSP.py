# This principal fored inherited classes from parent class to not make the parent class ruls violate
# it meant if panguin cant fly it shoud not inherit from Bird class
class Bird:
    def eat(self):
        return "Eating"

class FlyingBird(Bird):
    def fly(self):
        return "Flying"

class NonFlyingBird(Bird):
    pass

class Eagle(FlyingBird):
    pass

class Penguin(NonFlyingBird):
    pass

# Function that works with Bird objects
def make_bird_fly(bird: Bird):
    if isinstance(bird, FlyingBird):
        return bird.fly()
    else:
        return "This bird can't fly"

# Using the function with different bird objects
eagle = Eagle()
penguin = Penguin()

print(make_bird_fly(eagle))    # Output: "Flying"
print(make_bird_fly(penguin))  # Output: "This bird can't fly"

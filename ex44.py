class Other(object):
    
    # defines the functions of the PARENT class
    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")
        
# creates a class that inherits the functions from the PARENT
class Child(object):
    
    def __init__(self):
        self.other = Other()
        
    def implicit(self):
        self.other.implicit()
        
    def override(self):
        print("CHILD override()")
        
    def altered(self):
        print("CHILD, BEOFRE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
        
son = Child()
son.implicit()
son.override()
son.altered()

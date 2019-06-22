class Coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance(self, other):
		x_diff_sq = (self.x-other.x)**2
		y_diff_sq = (self.y-other.y)**2
		return (x_diff_sq + y_diff_sq)**0.5
	def __str__(self):
		return "<" + str(self.x) + "," + str(self.y) + ">"
	def __sub__(self, other):
		return Coordinate(self.x - other.x, self.y - other.y)
		
class Clock(object):
	def __init__(self, time):
		self.time = time
	def print_time(self):
		print(self.time)


class fraction(object):
	# initialize parameters
	def __init__(self, numer, denom):
		self.numer = numer
		self.denom = denom
	def __str__(self):
		return str(self.numer) + ' / ' + str(self.denom)
	# Method to return top and bottom of fraction
	def getNumer(self):
		return self.numer
	def getDenom(self):
		return self.denom
	# Method to add and subtract fractions
	def __add__(self, other):
		numerNew = other.getDenom() * self.getNumer() \
					+ other.getNumer() * self.getDenom()
		denomNew = other.getDenom() * self.getDenom()
		return fraction(numerNew, denomNew)
	def __sub__(self, other):
		numerNew = other.getDenom() * self.getNumer() \
					- other.getNumer() * self.getDenom()
		denomNew = other.getDenom() * self.getDenom()
		return fraction(numerNew, denomNew)
	# convert from fraction to float
	def convert(self):
		return self.getNumer() / self.getDenom()
		
class intSet(object):
	# create empty set
	def __init__(self):
		self.vals = []
	# if e is not in set then add it
	def insert(self, e):
		if not e in self.vals:
			self.vals.append(e)
	# boolean returns T/F if e is or is not a member of set
	def member(self, e):
		return e in self.vals
	# remove e from self, return value error if not in set to begin with
	def remove(self, e):
		try:
		      self.vals.remove(e)
		except:
		      raise ValueError(str(e) + ' not found')
	# print method to return values of the set
	def __str__(self):
		self.vals.sort()
		result = ''
		for e in self.vals:
			result = result + str(e) + ','
		return '{' + result[:-1] + '}'
		
# Exercise
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    def __eq__(self, other):
    	#method that returns True if coordinates refer to same point in the plane
    	#  (i.e., have the same x and y coordinate).
    	if self.getX() == other.getX() and self.getY() == other.getY():
    		return True
    	else:
    		return False
    # a special method that returns a string that looks like a valid Python 
    # expression that could be used to recreate an object with the same value. 
    # In other words, eval(repr(c)) == c given the definition of __eq__ from 
    # part 1.
    def __repr__(self):
    	return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
class Animal(object):
	def __init__(self, age):
		self.age = age
		self.name = None
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
	def set_age(self, newage):
		self.age = newage
	def set_name(self, newname = ""):
		self.name = newname
	def __str__(self):
		return "animal:"+str(self.name)+":"+str(self.age) 
class Cat(Animal):
	def speak(self):
		print("meow")
	def __str__(self):
		return "cat:"+str(self.name)+":"+str(self.age)	      				
class Rabbit(Animal):
	def speak(self):
		print("meep")
	def __str__(self):
		return "rabbit:"+str(self.name)+":"+str(self.age)
		
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
    def getDescription(self):
        return 'No description'
    
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)
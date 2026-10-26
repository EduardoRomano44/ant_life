from entities.Ant.Ant_State import Searching, Returning, Dead
import random

class Ant:
    search, returning, dead = Searching(), Returning(), Dead()
    transitions = {
        (search, "gather"): returning,
        (returning, "deposit"): search,
        (search, "age limit"): dead,
        (search, "poison"): dead,
        (returning, "age limit"): dead,
        (returning, "poison"): dead
    }

    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    def __init__(self, name, location, subject=None):
        self.name = name
        self.location = location
        self.home_location = location
        self.subject = subject
        self.current = self.search
        self.current.enter(self)
        self.age = 0
        self.bag = None
        self.bounds = None
        self.direction = "down"
    
    def change(self, target, event=None):
        if target is self.current:
            return
        self.current.exit(self)
        self.current = target
        self.current.enter(self, event)

    def tick(self, event=None):
        if self.current is self.dead:
            return
        target = Ant.transitions.get((self.current, event))
        if target is not None:
            self.change(target, event)
        self.current.update(self)
        self.age += 1
    
    def move(self, direction):
        dx, dy = self.directions[direction]
        x, y = self.location
        position = (x + dx, y + dy)
        if self.bounds is None or (0 <= position[0] < self.bounds[0] and 0 <= position[1] < self.bounds[1]):
            self.location = position

    def move_home(self):
        if self.location != self.home_location:
            self.move(self.get_direction(self.home_location))
    
    def get_direction(self, location):
        if self.location[0] < location[0]:
            return "right"
        elif self.location[0] > location[0]:
            return "left"
        elif self.location[1] < location[1]:
            return "down"
        elif self.location[1] > location[1]:
            return "up"
    
    def move_random(self):
        self.direction = random.choice(list(Ant.directions.keys()))
        self.move(self.direction)

    def move_front(self):
        self.move(self.direction)

    def collect_resource(self, resource):
        if self.bag is None and resource.pickup(self.location):
            self.bag = resource
            return True
        return False
    
    def deposit_resource(self):
        if self.location == self.home_location and self.bag is not None:
            resource = self.bag
            self.bag = None
            if self.subject:
                self.subject.notify("resource_received", context={"resource": resource, "ant": self})
            return True
        return False

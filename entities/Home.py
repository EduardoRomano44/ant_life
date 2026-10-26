from entities.Ant.Ant import Ant
from entities.Resourse import Food, Water
from logic.observer import Subject

class Home:
    """Represents the ant colony home nest and acts as an observer for delivered resources."""

    def __init__(self, location=(0, 0), subject=None, starting_ants=3):
        self.location = location
        self.ants = []
        self.food_in_home = 0
        self.water_in_home = 0
        self.ant_index = 0
        # Re-use or initialize the event bus for colony events
        self.subject = subject if subject is not None else Subject()
        self.subject.register("resource_received", self.on_resource_received)
        for _ in range(starting_ants):
            self.add_ant()
    
    def on_resource_received(self, context=None):
        """Handles resource delivery notifications and attempts to spawn new ants."""
        if not context:
            return
        resource = context.get("resource")
        if isinstance(resource, Food):
            self.food_in_home += 1
        elif isinstance(resource, Water):
            self.water_in_home += 1
        
        self.try_spawn()

    def try_spawn(self):
        """Spawns an ant when both food and water requirements are met."""
        if self.food_in_home > 0 and self.water_in_home > 0:
            self.food_in_home -= 1
            self.water_in_home -= 1
            self.add_ant()
    
    def add_ant(self):
        name = self.get_ant_name()
        self.ants.append(Ant(name, self.location, subject=self.subject))
    
    def has_ants(self):
        return len(self.ants) > 0
    
    def get_ant_name(self):
        index = self.ant_index
        self.ant_index += 1
        return "Ant" + str(index)

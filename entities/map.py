from entities.Home import Home

class Map:
    def __init__(self, dimensions, resources, subject=None, starting_location=(0, 0), starting_ants=3, background_image=None):
        self.width, self.height = dimensions
        self.background_image = "default" if background_image is None else background_image
        self.home = Home(starting_location, subject, starting_ants)
        self.food = resources.get("food", [])
        self.water = resources.get("water", [])

    def tick(self):
        # Deposits may add ants; newborn ants start on the next frame.
        for ant in tuple(self.home.ants):
            ant.bounds = (self.width, self.height)
            ant.tick()
            if ant.current is ant.search:
                for resource in self.food + self.water:
                    if ant.collect_resource(resource):
                        ant.change(ant.returning, "gather")
                        break
        self.home.ants[:] = [ant for ant in self.home.ants if ant.current is not ant.dead]

    def get_background(self):
        return self.background_image

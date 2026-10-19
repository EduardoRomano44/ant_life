class Resourse:
    def __init__(self, positions):
        self.positions = self.get_starting_positions(positions)

    @staticmethod
    def get_starting_positions(positions):
        return {(x, y) for x in range(positions[0], positions[1]) for y in range(positions[0], positions[0] + positions[2])}
        
    def pickup(self, position):
        if position in self.positions:
            self.positions.remove(position)
            return True
        return False

    def spawn(self, position):
        self.positions.add(position)

class Food(Resourse):
    def __init__(self, positions):
        super().__init__(positions)

class Water(Resourse):
    def __init__(self, positions):
        super().__init__(positions)

    
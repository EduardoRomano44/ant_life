class Resourse:
    def __init__(self, positions):
        self.positions = self.get_starting_positions(positions)

    @staticmethod
    def get_starting_positions(positions):
        start, right_size, down_size = positions
        return {
            (x, y)
            for x in range(start[0], start[0] + right_size)
            for y in range(start[1], start[1] + down_size)
        }
        
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
    
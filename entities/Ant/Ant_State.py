class Ant_State:
    def enter(self, ant, event=None):
        pass

    def update(self, ant):
        pass

    def exit(self, ant):
        pass

class Searching(Ant_State):
    def enter(self, ant, event=None):
        print(ant.name + " started searching")

    def update(self, ant):
        if ant.age >= 700:
            ant.change(ant.dead, "age limit")
            return
        
        if ant.age % 4 == 0:
            ant.move_random()
        else:
            ant.move_front()

    def exit(self, ant):
        print(ant.name + " found a resource")

class Returning(Ant_State):
    def enter(self, ant, event=None):
        print(ant.name + " started returning")

    def update(self, ant):
        if ant.age >= 700:
            ant.change(ant.dead, "age limit")
            return
        
        ant.move_home()
        if ant.deposit_resource():
            ant.change(ant.search, "deposit")

    def exit(self, ant):
        print(ant.name + " reached home")

class Dead(Ant_State):
    def enter(self, ant, event=None):
        print(ant.name + " died of " + str(event))
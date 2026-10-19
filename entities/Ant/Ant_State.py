class Ant_State:
    def enter(self, ant):
        pass

    def update(self, ant):
        pass

    def exit(self, ant):
        pass

class Searching(Ant_State):
    def enter(self, ant):
        print(ant + " started searching")

    def update(self, ant):
        if ant.age > 100:
            ant.change(ant.dead, "age limit")
            return
        
        ant.move_random()

    def exit(self, ant):
        print(ant.name + " found a resource")
        ant.collect_resource()

class Returning(Ant_State):
    def enter(self, ant):
        print(ant.name + " started returning")

    def update(self, ant):
        if ant.age > 100:
            ant.change(ant.dead, "age limit")
            return
        
        ant.move_home()

    def exit(self, ant):
        print(ant.name + " reached home")
        ant.deposit_resource()

class Dead(Ant_State):
    def enter(self, ant, cause):
        print(ant.name + " died of " + cause)
    
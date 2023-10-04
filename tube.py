from sprite import *


class Tube:


    def __init__(self, n_tube: int, pos_x: int, pos_y: int, up: bool) -> None:

        n = -1
        pos = (29,37)
        m = -n_tube*8+8
        if up:

            n = 1
            pos = (29,23)
            m = -1 + n_tube*8
        
        self.tubes = [Sprite(pos_x, pos_y+i*8*n,(16,8),(0,16),0) for i in range(n_tube)]

        self.tubes.append(Sprite(pos_x-3, pos_y+m,(22,4),pos,0))

        self.destroy = False

    def draw(self):

        for tube in self.tubes:

            tube.draw()


    def update(self):

        for tube in self.tubes:

            tube.pos_x -= 0.5
            if tube.pos_x <= - 22:
                self.destroy = True

    def test_collide(self, sprite: 'Sprite'):

        for tube in self.tubes:

            if tube.test_collision_sprite(sprite):

                return True
            
        return False
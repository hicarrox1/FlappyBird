import pyxel
from sprite import *

class Player(AnimateSprite):

    def __init__(self) -> None:
        super().__init__(50,50,(13,9),{"idle":[(33,2)],"fly":[(33,2),(17,2),(1,2),(17,2)],"dead":[(1,98)]},"idle",2,12)

        self.jump = False

        self.dead_b = False

        self.saut_y = 0
        self.gravity = 0.05

    def update(self):

        if not self.dead_b:

            self.aply_gravity()

            self.input()

        else:

            self.fall()

    def aply_gravity(self):

        self.pos_y += self.gravity

        if self.gravity <= 2:

            self.gravity += 0.025

        if self.jump:

            self.gravity = 0.05

            self.saut_y += 3
        
            if self.saut_y >= 8:

                self.jump = False
                self.saut_y = 0.2

            self.pos_y -= self.saut_y
    
    def input(self):

        if pyxel.btnp(pyxel.KEY_SPACE):

            self.jump = True

            self.one_anim("fly","idle")

    def dead(self):

        self.one_anim_bool = False
        self.dead_b = True
        self.state = "dead"

    def fall(self):

        if self.pos_y <= pyxel.height:
                     
            self.pos_y += self.gravity

            if self.gravity <= 2:

                self.gravity += 0.2

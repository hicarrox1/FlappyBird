import pyxel
from sprite import *
from player import Player
from tube import Tube
from random import randint

class Background:

    def __init__(self) -> None:

        self.background = [Sprite(0, 0, (101,16), (72,0), None),Sprite(0, pyxel.height-16, (101,16), (72,16), None),
                           Sprite(100, 0, (101,16), (72,0), None),Sprite(100, pyxel.height-16, (101,16), (72,16), None)]

    def update(self):

        for back in self.background:
            back.pos_x -= 0.5
            if back.pos_x <= -100:
                back.pos_x = 100

    def draw(self):

        for back in self.background:
            back.draw()

class App():

    def __init__(self) -> None:
        pyxel.init(100,100)
        pyxel.load(r"images.pyxres")
        pyxel.mouse(False)

        self.score = 0
        self.pigeon = Player()
        self.background = Background()

        self.tube = None

        self.tube_spawn_time = 140
        self.tubes = []

        self.game = True

        self.sprite_liste = [self.background, self.pigeon]

        pyxel.run(self.update,self.draw)
    
    def update(self):

        if self.game:

            self.update_all_sprite()

            self.test_generate_tube()

            self.update_tubes()

            self.test_player_dead()

        else:

            self.pigeon.update()
            self.test_replay()

    def draw(self):

        pyxel.cls(12)

        self.draw_all_sprite()

        self.draw_tubes()

        if not self.game:

            self.pigeon.draw()
            pyxel.text(35,20,"GAME OVER", 8)
            pyxel.text(10,40,"--- press space ---", 8)

    def draw_tubes(self):

        for tube in self.tubes:

            tube.draw()

    def update_tubes(self):

        for tube in self.tubes:

            tube.update()

    def draw_all_sprite(self):
        
        for sprite in self.sprite_liste:
            sprite.draw()

    def update_all_sprite(self):

        for sprite in self.sprite_liste:
            try:
                sprite.update()
            except:
                pass

    def test_generate_tube(self):
    
        if pyxel.frame_count % self.tube_spawn_time == 0:

            self.tubes.extend(self.generate_tube())

        for tube in self.tubes:

            if tube.destroy:

                self.tubes.remove(tube)

    def generate_tube(self):

        first_lenght = randint(1,7)
        second_lenght = randint(8,9) - first_lenght

        return Tube(first_lenght,pyxel.width,pyxel.height-8, False), Tube(second_lenght,pyxel.width,0, True)
    
    def test_replay(self):

        if pyxel.btnp(pyxel.KEY_SPACE):

            self.score = 0
            self.pigeon = Player()
            self.background = Background()

            self.tube = None

            self.tube_spawn_time = 140
            self.tubes = []

            self.game = True

            self.sprite_liste = [self.background, self.pigeon]

    def test_player_dead(self):

        if self.pigeon.pos_y >= pyxel.height:

            self.game = False
            self.pigeon.dead()

        for tube in self.tubes:

            if tube.test_collide(self.pigeon):

                self.game = False
                self.pigeon.dead()

App()
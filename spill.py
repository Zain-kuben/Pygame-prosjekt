import pygame as pg

pg.init()

class Kurv:
    def __init__(self, x_pos:int, y_pos:int, bredde:int, høyde:int, fart:int, vindu, farge:tuple):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._bredde = bredde
        self._høyde = høyde
        self._fart = fart
        self._vindu = vindu
        self._farge = farge
        self._retning = "stopp"
    
    def tegne(self):
        pg.draw.rect(
            self._vindu,
            self._farge,
            (self._x_pos, self._y_pos, self._bredde, self._høyde)
        )

    def flytt(self):
        if self._retning == "venstre":
            self._x_pos -= self._fart
        elif self._retning == "høyre":
            self._x_pos += self._fart

    def rettning(self, trykkede_taster):
        if trykkede_taster[pg.K_LEFT]:
            self._retning = "venstre"
        elif trykkede_taster[pg.K_RIGHT]:
            self._retning = "høyre"
        else:
            self._retning = "stopp"

    def grenser(self):
        if self._x_pos <= 0:
            self._x_pos = 0
        elif self._x_pos + self._bredde >= self._vindu.get_width():
            self._x_pos = self._vindu.get_width() - self._bredde

class Ball:
    def __init__(self, x_pos:int, y_pos:int, radius:int, fart:float, vindu, farge:tuple):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._radius = radius
        self._fart = fart
        self._vindu = vindu
        self._farge = farge

    def tegne_ball(self):
        pg.draw.circle(self._vindu, self._farge, (self._x_pos, self._y_pos), self._radius)
    
    def flytt(self):
        self._y_pos += self._fart




VINDU_BREDDE = 500
VINDU_HOYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
pg.display.set_caption("Bruk piltaster for å bevege")

kurv = Kurv(225, 450, 50, 20, 0.5, vindu, (255, 0, 0))
ball = Ball(250, 0, 15, 0.4, vindu, (0, 0, 255))

fortsett = True

while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    trykkede_taster = pg.key.get_pressed()

    kurv.rettning(trykkede_taster)
    kurv.flytt()
    kurv.grenser()

    vindu.fill((255, 255, 255))
    kurv.tegne()
    pg.display.flip()

pg.quit()

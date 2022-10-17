from pico2d import *
import game_framework
import start_image


class Background:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(800 // 2, 640 // 2)


class Mario:
    def __init__(self):
        self.x, self.y = 30, 90
        self.frame = 0
        self.image = load_image('mario.png')
        self.state = 3
        self.dirX = 0
        self.dirY = 0
        self.m = 0.5
        self.v = 0.5
        self.jump = 0
        self.F = 0


    def update(self):
        self.frame = (self.frame + 1) % 3
        self.x += self.dirX * 5

        if self.jump == 1:
            if self.v > 0:
                self.F = (0.5 * self.m * (self.v * self.v))
            else:
                self.F = -(0.5 * self.m * (self.v * self.v))

            self.y -= self.F
            self.v -= 0.1




    def draw(self):

        if self.state == 0 or self.state == 1:
            self.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(100, self.state * 100, 100, 100, self.x, self.y)




def handle_events():
    global running
    global dirX
    global dirY
    global state
    global F
    events = get_events()

    for event in events:

        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                char.dirX += 1
                char.state = 1
            elif event.key == SDLK_LEFT:
                char.dirX -= 1
                char.state = 0
            elif event.key == SDLK_z:
                char.jump = 1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                char.dirX -= 1
                char.state = 3
            elif event.key == SDLK_LEFT:
                char.dirX += 1
                char.state = 2
            elif event.key == SDLK_z:
                char.jump = 0

        if char.x < 30:
            char.dirX = 0
            if char.state == 1:
                char.dirX += 1

        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(start_image)


def enter():
    global char, back, running
    char = Mario()
    back = Background()
    running = True


def exit():
    global char, back
    del char
    del back


def update():
    char.update()


def draw():
    clear_canvas()
    back.draw()
    char.draw()
    update_canvas()
    delay(0.01)

    # def handle_events(self):
    #     self.running
    #     self.dirX
    #     self.dirY
    #     self.state
    #     self.events = get_events()
    #
    #     for event in self.events:
    #         if event.type == SDL_QUIT:
    #             self.running = False
    #         elif event.type == SDL_KEYDOWN:
    #             if event.key == SDLK_RIGHT:
    #                 self.dirX += 1
    #                 self.state = 1
    #             elif event.key == SDLK_LEFT:
    #                 self.dirX -= 1
    #                 self.state = 0
    #
    #             elif event.key == SDLK_ESCAPE:
    #                 self.running = False
    #
    #         elif event.type == SDL_KEYUP:
    #             if event.key == SDLK_RIGHT:
    #                 self.dirX -= 1
    #                 self.state = 3
    #             elif event.key == SDLK_LEFT:
    #                 self.dirX += 1
    #                 self.state = 2

    # handle_events()
    # delay(0.01)

# open_canvas(800, 640)
#
# char = Mario()
# back = Background()
# char.running = True
#
# while char.running:
#     clear_canvas()
#     back.draw()
#     char.draw()
#     update_canvas()
#     char.handle_events()
#     char.update()
#     delay(0.01)
#
# close_canvas()

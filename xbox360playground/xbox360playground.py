import signal
from xbox360controller import Xbox360Controller
from random import randint
from asciimatics.screen import Screen


def on_button_pressed(button):
    print('Button {0} was pressed'.format(button.name))


def on_button_released(button):
    print('Button {0} was released'.format(button.name))



def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))

def demo(screen):
    while True:
        screen.print_at('Hello world!',
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()

try:
    with Xbox360Controller(0, axis_threshold=0.2) as controller:
        # Button A events
        controller.button_a.when_pressed = on_button_pressed
        controller.button_a.when_released = on_button_released
        controller.button_b.when_pressed = on_button_pressed
        controller.button_b.when_released = on_button_released
        controller.button_y.when_pressed = on_button_pressed
        controller.button_y.when_released = on_button_released
        controller.button_x.when_pressed = on_button_pressed
        controller.button_x.when_released = on_button_released

        controller.button_select.when_pressed = on_button_pressed
        controller.button_select.when_released = on_button_released
        controller.button_start.when_pressed = on_button_pressed
        controller.button_start.when_released = on_button_released
        controller.button_mode.when_pressed = on_button_pressed
        controller.button_mode.when_released = on_button_released
        controller.button_thumb_l.when_pressed = on_button_pressed
        controller.button_thumb_l.when_released = on_button_released
        controller.button_thumb_r.when_pressed = on_button_pressed
        controller.button_thumb_r.when_released = on_button_released


        # Left and right axis move event
        controller.axis_l.when_moved = on_axis_moved
        controller.axis_r.when_moved = on_axis_moved
        controller.hat.when_moved = on_axis_moved

        signal.pause()
except KeyboardInterrupt:
    pass



from pygame.time import get_ticks

from icb.hardware.state import State
from icb.screens.page import Page


class Menu(Page):
    def __init__(self, screen, machine):
        Page.__init__(self, screen, machine=machine, title='Menu')
        self.add_menu_item(text="Play", machine_state=State.PLAYING)
        self.add_menu_item(text="Highscores", machine_state=State.HIGH_SCORE)
        self.add_menu_item(text="Diagnostics", machine_state=State.DIAGNOSTIC)


        self.menu_items[self.selected].selected = True

        self.time_ms_between_menu_change = 100
        self.last_press = get_ticks()

    def draw(self):
        Page.draw(self)

        for item in self.menu_items:
            item.draw()

    def event_handler(self, escape, machine):
        escape, machine = Page.event_handler(escape, machine)
        if get_ticks() > self.last_press+self.time_ms_between_menu_change:
            if self.machine.inputs["start"].state == "high":
                machine.state = self.menu_items[self.selected].machine_state
            elif self.machine.inputs["right_down"].state == "high" \
                    or self.machine.inputs["left_down"].state == "high":
                self.menu_down()

            elif self.machine.inputs["right_up"].state == "high" \
                    or self.machine.inputs["left_up"].state == "high":
                self.menu_up()

            self.last_press = get_ticks()

        return escape, machine

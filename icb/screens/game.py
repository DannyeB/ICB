from pygame.time import get_ticks
from icb.hardware.state import State
from icb.screens.page import Page
from icb.game.game_loops import Game as G
from icb.utils.colors import Colors


class Game(Page):
    def __init__(self, screen, machine):
        Page.__init__(self, screen, machine=machine, title='ICB')
        self.level = 0
        self.game = G()
        self.add_menu_item("Level:", xpos=30, ypos=50)
        self.add_menu_item(self.game.current_level.name, xpos=100, ypos=50, font_color=Colors.GREEN)
        self.add_menu_item("Time:", xpos=30)
        self.add_menu_item("", xpos=100, ypos=self.menu_items[len(self.menu_items)-1].item_ypos, font_color=Colors.GREEN)
        self.add_menu_item("Target:", xpos=30)
        self.add_menu_item("", xpos=100, ypos=self.menu_items[len(self.menu_items)-1].item_ypos, font_color=Colors.GREEN)
        self.add_menu_item("Bonus:", xpos=30)
        self.add_menu_item("0", xpos=100, ypos=self.menu_items[len(self.menu_items)-1].item_ypos, font_color=Colors.RED)
        self.add_menu_item("Balls:", xpos=30)
        self.add_menu_item(str(self.game.balls), xpos=100, ypos=self.menu_items[len(self.menu_items) - 1].item_ypos,
                           font_color=Colors.BLUE)
        self.add_menu_item("Score:", xpos=30)
        self.add_menu_item("0", xpos=100, ypos=self.menu_items[len(self.menu_items)-1].item_ypos,
                           font_color=Colors.LIME)

    def draw(self):
        Page.draw(self)

        if self.game.state == State.PLAYING:
            self.game.update_game_loop()
            self.menu_items[1].text = self.game.current_level.name
        elif self.game.state == State.HOMING:
            self.game.update_home_loop()
            self.menu_items[1].text = "HOMING..."
        elif self.game.state == State.STAGE_COMPLETE:
            self.menu_items[1].text = "Stage Complete!"
            self.game.next_level()
        elif self.game.state == State.GAME_OVER:
            self.menu_items[1].text = "GAME OVER"

        self.menu_items[3].text = str(self.game.time_seconds)
        self.menu_items[5].text = str(self.game.current_level.target)
        self.menu_items[7].text = str(self.game.current_level.bonus)
        self.menu_items[9].text = str(self.game.balls)
        self.menu_items[11].text = str(self.game.score)

        for item in self.menu_items:
            item.draw()

    def event_handler(self, escape, machine):
        escape, machine = Page.event_handler(escape, machine)

        if machine.inputs["left_home"].state == "high":
            self.game.left_home = True
        else:
            self.game.left_home = False

        if machine.inputs["right_home"].state == "high":
            self.game.right_home = True
        else:
            self.game.right_home = False

        if self.game.state == State.PLAYING:
            if machine.inputs[self.game.current_level.target].state == "high":
                self.game.state = State.STAGE_COMPLETE

            if machine.inputs["lost_ball"].state == "high":
                self.game.balls = self.game.balls - 1
                self.game.state = State.HOMING

        return escape, machine

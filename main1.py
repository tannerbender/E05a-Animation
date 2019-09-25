#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Mouse Example"


class Ball:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x # x position of the ball
        self.position_y = position_y #y position of the ball
        self.radius = radius #radius of the ball
        self.color = color #color of the ball

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) #drawing the ball


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)#setting the background of the game

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)#creating ball

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()# starting to render ball
        self.ball.draw() #drawing the ball

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x #move where mouse goes on x axis
        self.ball.position_y = y #move where mouse goes on y axis

    def on_mouse_press(self, x, y, button, modifiers): #creating something for when a button is clicked
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")# relaying a message that says you pushed a button and what button you pushed
        if button == arcade.MOUSE_BUTTON_LEFT: # if you left click
            self.ball.color = arcade.color.BLACK #if left click then ball turns black

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT: # if left button is released 
            self.ball.color = arcade.color.AUBURN #after left click released the ball will return to color auburn


def main():
    print("This game") #printing game
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()#running the game


if __name__ == "__main__":
    main()
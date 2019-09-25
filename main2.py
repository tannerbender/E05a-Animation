#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the keyboard.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_keyboard
"""

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Move Keyboard Example"
MOVEMENT_SPEED = 3


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x #creating x variable position
        self.position_y = position_y #creating y variable position
        self.change_x = change_x #creating the variable of the x change
        self.change_y = change_y #creating the variable of the y change
        self.radius = radius #radius variable of the ball
        self.color = color #color variable of the ball

    def draw(self): #drawing itself
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color) # draw circle with variables

    def update(self):
        # Move the ball
        self.position_y += self.change_y # variable y is equal to itself + whatever the change in y is 
        self.position_x += self.change_x # variable x is equal to istelf + whatever the change in x is

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius: # center of circle is not touching left boundary 
            self.position_x = self.radius # radius of circle is the distance of the center of the circle to the boundary

        if self.position_x > SCREEN_WIDTH - self.radius: # if center of circle is greater than screen width, subtract the radius
            self.position_x = SCREEN_WIDTH - self.radius 

        if self.position_y < self.radius: # center of circle is not touching top and bottom boundaries
            self.position_y = self.radius # radius of circle is the distance from the center of the circle to the boundaries of the top and bottom parts of the screen

        if self.position_y > SCREEN_HEIGHT - self.radius: # if center of circle is greater than screen height than subract the radius of the circle and show location
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False) #if visible cant be true

        arcade.set_background_color(arcade.color.ASH_GREY) # set background color of game to grey

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN) #creating the ball

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render() #rendering game
        self.ball.draw() #draw ball

    def update(self, delta_time): #update self
        self.ball.update() #update location of ball

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT: # if key on keyboard is left 
            self.ball.change_x = -MOVEMENT_SPEED # move ball towards left
        elif key == arcade.key.RIGHT: # if not left then right
            self.ball.change_x = MOVEMENT_SPEED # move ball to the right
        elif key == arcade.key.UP: # if up key is pressed
            self.ball.change_y = MOVEMENT_SPEED # move location up on screen
        elif key == arcade.key.DOWN: # else must be down
            self.ball.change_y = -MOVEMENT_SPEED # move location down on screen 

    def on_key_release(self, key, modifiers): # defining key release
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT: # once either left or right key are released
            self.ball.change_x = 0 # ball position will not change
        elif key == arcade.key.UP or key == arcade.key.DOWN: # once either up or down key are released
            self.ball.change_y = 0 # ball position won't change


def main(): 
    print("my game")
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
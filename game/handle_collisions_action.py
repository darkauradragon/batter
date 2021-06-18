import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]
       
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                #remove brick
                pass
        
        if ball.get_position().equals(paddle.get_position()):
            #change direction of ball
            pass
        
        ball_p = ball.get_position()
        if ball_p[1] > constants.MAX_Y:
            #lose game start over
            pass
        
        if ball_p[0] <1 or ball_p>constants.MAX_X or ball_p[1]:
            #rebound off wall
            pass

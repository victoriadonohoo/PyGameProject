import sys 
from time import sleep 
import pygame
from settings import Settings
from game_stats import GameStats 
from ship import Ship
from bullet import Bullet
from alien import Alien 

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # initializes the background settings pygame needs to function properly 
        pygame.init()
        # create an instance of settings
        self.settings = Settings()
        # we assign an object (surface) to self.screen that formats the display window 
        # when the game's animation loop is activated by the run_game method the surface will be redrawn on every pass 
        #   through the loop based on user input. 
        # FULLSCREEN mode - tells pygame to figure out a windpw size that fills the screen 
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # update the settings object after the screen is created using the width and height attributes 
        #   of the screens rect
        self.settings.screen_width = self.screen.get_rect().width 
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # create an instance to store game statistics 
        self.stats = GameStats(self)

        # assign the ship instance to self.ship 
        # the argument self refers to the current instance of AlienInvasion
        # this gives the ship access to the game's resources 
        self.ship = Ship(self)

        #create the group to store bullets in 
        self.bullets = pygame.sprite.Group()

        #create the group to store aliens in 
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # set the background color to light grey
        self.bg_color = (230, 230, 230)
    # create check_events method to simplify run_game() and isolate the event management loop.

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        # if user presses right arrow key, game moves the ship to the right 
        if event.key == pygame.K_RIGHT:
            #set moving_right to true (indirectly moves ship to the right)
            self.ship.moving_right = True 
        # if user presses left arrow key, game moves ship to the left 
        elif event.key == pygame.K_LEFT:
            # set moving_left to true
            self.ship.moving_left = True
        # press Q to exit 
        elif event.key == pygame.K_q:
            sys.exit()
        # when space bar is pressed, we call _fire_bullet()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # when the player releases the key, we set moving_right and moving_left to false
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if  len(self.bullets) < self.settings.bullets_allowed:
            # create an instance of Bullet 
            new_bullet = Bullet(self)
            # add the instance to the bullets group
            self.bullets.add(new_bullet)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        #  the event loop makes our program respond to events and perform appropriate tasks depending on the 
        #       kinds of events that occur  
        # the function pygame.event.get() returns a list of events that have taken place since the last time 
        #   the function was called. 
        # Any mouse movement or keyboard clicks are events.
        for event in pygame.event.get():
            # when user clicks the game windows close button, a pygame.QUIT event is detected and we call sys.exit() 
            #   to exit the game  
            if event.type == pygame.QUIT:
                sys.exit()
            # checks if user pressed keys 
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # redraw the screen during each pass through the loop - argument is from the settings class
        self.screen.fill(self.settings.bg_color)
        
        # placed here so image appears on top of the background 
        # draw the ship on the screen 
        self.ship.blitme()

        # loop through the sprites in bullets and call draw_bullet() on each one
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # make an alien appear 
        self.aliens.draw(self.screen)

        # make the most recently drawn screen visible - display is updated continuously to show the new positions of the game 
        #   and hide old ones, creating illusion of smooth movement
        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions 
        # call update ship method 
        self.bullets.update()
        # get rid of bullets that disappeared 
        # allows us to modify bullets inside the loop
        for bullet in self.bullets.copy():
            # check if the bullet has disappeared 
            if bullet.rect.bottom <= 0:
                # if it has we remove it from bullets
                self.bullets.remove(bullet)
        # print how many bullets currently exist in the game and verify that they're being deleted when they reach the 
        #   top of the screen 
        print(len(self.bullets))
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # check for any bullets that have hit any aliens 
        # if so, get rid of the bullet and the alien 
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # check if the aliens group is empty 
        # it is empty if it evaluates to false 
        if not self.aliens:
            # destroy existing bullets and create new fleet 
            self.bullets.empty()
            self._create_fleet()


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # create an alien and find the number of aliens in a row

        #create alien
        alien = Alien(self)
        # get width/height of alien 
        alien_width, alien_height = alien.rect.size
        # calculate the horizontal space available for aliens 
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # calculate number of aliens that will fit in that space 
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows of aliens that fit on the screen 
        ship_height = self.ship.rect.height 
        # calculate number of rows that fits on screen 
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create the full fleet by counting from 0 to number of rows available 
        for row_number in range(number_rows):
            # creates aliens in one row 
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # create an alien and place it in the row 
        # spacing between each alien is equal to one alien width s
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number 
        alien.rect.x = alien.x 
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Check if the fleet is at an edge, 
                then update the positions of all aliens in the fleet. """
        self._check_fleet_edges()
        self.aliens.update()

        # loops through the group aliens and returns the first alien it finds that has collided with the ship 
        # if no collisions occur, spritecollideany() returns None and if block does not execute 
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # look for aliens hitting the bottom of the screen after updating the positions of all the aliens 
        #   and after looking for an alien and ship collision 
        # new fleet appears after a ship is hit or an alien hits the bottom 
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        # loop through the fleet and call check_edges() on each alien 
        for alien in self.aliens.sprites():
            # if aliens have reached the edge, the whole fleet changes direction
            # if so, call _change_fleet_direction and break out of the loop 
            if alien.check_edges():
                self._change_fleet_direction()
                break 

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        # loop through all aliens and drop each one using the setting fleet_drop_speed 
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed 
        # change the value of the fleet_direction by multiplying its current value by -1 
        # not a part of the for loop because we only want to change the direction of the fleet once 
        self.settings.fleet_direction *= -1 

    def _ship_hit(self):
            """Respond to the ship being hit by an alien. """
            # sets game_active to False when player has used all of their ships
            if self.stats.ships_left > 0:
                # decrement ships_left 
                self.stats.ships_left -= 1

                # get rid of any remaining aliens and bullets 
                self.aliens.empty()
                self.bullets.empty()

                # create a new fleet and center the ship 
                self._create_fleet()
                self.ship.center_ship()

                # pause before elements are changed for half a second 
                sleep(0.5)
            else:
                self.stats.game_active = False 

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        # if the rect.bottom value of an alien is >= to the screens rect.bottom attribute
        for alien in self.aliens.sprites():
            # only need one alien to hit the bottom so no need to check the rest 
            if alien.rect.bottom >= screen_rect.bottom:
                # treat same as if a ship was hit 
                self._ship_hit()
                break 

    def run_game(self):
        """Start the main loop for the game."""
        # run_game() method controls the game and the while loop will run continuously 
        while True:
            # call check events method 
            self._check_events()
            # if the game is in active mode, do the following 
            if self.stats.game_active:
                # call update method from ship file 
                self.ship.update()
                # call update bullets method 
                self._update_bullets()
                # call update aliens method 
                self._update_aliens() 
            # call update events method
            self._update_screen()
if __name__ == '__main__':
    # make a game instance, and run the game. 
    ai = AlienInvasion()
    ai.run_game()


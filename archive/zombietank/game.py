import pgzrun
import random
import time


TITLE = "Zombies vs Tanks"
WIDTH = 800
HEIGHT = 640

UP = 180
DOWN = 0
LEFT = 270
RIGHT = 90
BULLET_SPEED = 10

blue_tank = Actor("tank_blue")
blue_tank.x = WIDTH / 2
blue_tank.y = HEIGHT / 2

bullets = []
BULLET_SPEED = 10

zombie_list = []
ZOMBIE_SPEED = 1

score = 0
game_over = False

# Load the heart image and create a list to track player's hearts
heart_image = "heart.png"
player_hearts = [Actor(heart_image, (40 * i + 10, HEIGHT - 40)) for i in range(3)]
cooldown_time = 0  


def draw():
    global game_over
    if not game_over:
        screen.blit("tank.png", (0, 0))
        blue_tank.draw()
        for bullet in bullets:
            bullet.draw()
        clock.schedule(create_zombies, 5)
        for zomb in zombie_list:
            zomb.draw()
        screen.draw.text(f"score: {score} ", (350, 150))

        # Draw player's hearts
        for heart in player_hearts:
            heart.draw()

    else:
        screen.fill("blue")
        screen.draw.text(f"GAME OVER, Your score: {score} ", (350, 150))
        screen.draw.text("Press 'R' to Restart Game", (330, 200))


def update():
    global game_over  # Declare game_over as a global variable
    global bullet_fired
    if not game_over:
        if keyboard.left:
            blue_tank.x = blue_tank.x - 5
            blue_tank.angle = LEFT
        if keyboard.right:
            blue_tank.x = blue_tank.x + 5
            blue_tank.angle = RIGHT
        if keyboard.up:
            blue_tank.y = blue_tank.y - 5
            blue_tank.angle = UP
        if keyboard.down:
            blue_tank.y = blue_tank.y + 5
            blue_tank.angle = DOWN
        if keyboard.space:
            shoot_bullet()

        for bullet in bullets:
            if bullet.x >= WIDTH or bullet.x <= 0 or bullet.y >= HEIGHT or bullet.y <= 0:
                bullets.remove(bullet)
            else:
                move_bullet(bullet)

        move_zombie()
        check_player_health()

        # Check for game over based on remaining hearts
        if len(player_hearts) == 0:
            game_over = True


def shoot_bullet():
    global blue_tank, bullets
    if len(bullets) < 1:
        sounds.laserretro_004.play()
        bullet = Actor("bulletblue")
        bullet.x = blue_tank.x
        bullet.y = blue_tank.y
        bullet.angle = blue_tank.angle
        bullets.append(bullet)


def move_bullet(bullet):
    global bullets, zombie_list, score

    bullets_to_remove = []  # Create a list to store bullets to be removed

    if bullet.angle == LEFT:
        bullet.x -= BULLET_SPEED
    elif bullet.angle == RIGHT:
        bullet.x += BULLET_SPEED
    elif bullet.angle == DOWN:
        bullet.y += BULLET_SPEED
    elif bullet.angle == UP:
        bullet.y -= BULLET_SPEED

    for zomb in zombie_list:
        if bullet.colliderect(zomb):
            if bullet in bullets:
                bullets_to_remove.append(bullet)  # Add the bullet to the removal list
                zombie_list.remove(zomb)
                score += 1

        # Remove bullets from the bullets list after processing collisions
    for bullet in bullets_to_remove:
        if bullet in bullets:  # Check again to avoid errors
            bullets.remove(bullet)


def create_zombies():
    if len(zombie_list) < 10:
        loc_rand = random.randint(0, 3)
        if loc_rand == 0:
            y = random.randint(40, HEIGHT - 40)
            z = Actor("zombie_stand.png")
            z.x = 1
            z.y = y
            zombie_list.append(z)
        elif loc_rand == 1:
            y = random.randint(40, HEIGHT - 40)
            z = Actor("zombie_stand.png")
            z.x = WIDTH - 1
            z.y = y
            zombie_list.append(z)
        elif loc_rand == 2:
            x = random.randint(40, WIDTH - 40)
            z = Actor("zombie_stand.png")
            z.y = 1
            z.x = x
            zombie_list.append(z)
        elif loc_rand == 3:
            x = random.randint(40, WIDTH - 40)
            z = Actor("zombie_stand.png")
            z.y = HEIGHT - 1
            z.x = x
            zombie_list.append(z)


def move_zombie():
    global score, game_over
    for zomb in zombie_list:
        if zomb.x < blue_tank.x:
            zomb.x += ZOMBIE_SPEED
        elif zomb.x > blue_tank.x:
            zomb.x -= ZOMBIE_SPEED
        elif zomb.y < blue_tank.y:
            zomb.y += ZOMBIE_SPEED
        elif zomb.y > blue_tank.y:
            zomb.y -= ZOMBIE_SPEED


def check_player_health():
    global player_hearts, game_over, cooldown_time  # Add cooldown_time here
    
    current_time = int(time.time() * 1000)  # Get current time in milliseconds
    
    if not game_over:
        for zomb in zombie_list:
            if blue_tank.colliderect(zomb):
                if current_time >= cooldown_time:  # Check if cooldown_time has passed
                    cooldown_time = current_time + 1000  # Set next cooldown_time to 1 second later
                    if len(player_hearts) > 0:
                        lost_heart = player_hearts.pop()
                        lost_heart.image = "empty_heart.png"  # Replace with the empty heart image
                        sounds.damage.play()
                        break  # This ensures that only one heart is lost per frame
                    else:
                        game_over = True






def restart_game():
    global game_over, score, bullets, zombie_list, player_hearts
    game_over = False
    score = 0
    bullets = []
    zombie_list = []
    player_hearts = [Actor(heart_image, (40 * i + 10, HEIGHT - 40)) for i in range(3)]


# Restart game when 'R' key is pressed
def on_key_down(key):
    global game_over
    if game_over and key == keys.R:
        restart_game()

pgzrun.go()

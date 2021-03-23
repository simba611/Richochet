## Brick Breaker Game
### The game starts with initial position of the ball randomly on the paddle. You can move the paddle left or right using 'a' and 'd' characters respectively. 
### Press and hold 'w' to launch the ball. Once the ball launches it will collide with the walls, bricks and paddle. If it misses the paddle you lose a life. There are a total of 3 lives. 
### The bricks have different strength levels with -
Red = Strength 3,
Yellow = Strength 2,
Green = Strength 1
Grey = Unbreakable 
Magenta = Explosive 

Rainbow brick keeps on changing it's color till its hit by the ball for the first time. After that it behaves like a normal brick.

### If an explosive brick is hit, it will break all bricks around it including unbreakable bricks and will cause a chain reaction with the rest of the explosive bricks

### Upon breaking a brick a powerup might drop from the following - 
F = Fast Ball - Increases the speed of the ball for duration of he powerup. It stacks if you pick up more than one.

L = Large paddle - Increases the length of the paddle for the duration of the powerup. It stacks if you pick up more than one.

S = Small paddle - Decreases the length of the paddle for the duration of the powerup. It stacks but doesn;t decrease below certain limit.

P = Paddle Grab - Allows the paddle to grab the ball and move it before releasing it with 'w' again for the duration of the powerup.

T = Through Ball - The ball destroys all blocks in its path for the duration of the powerup

X = Shooting Paddle - The paddle shoots bullets periodically. Each bullet hits a brick once and has the same effect as the ball
### All powerups have duration 20 seconds and will reset on loss of life. They attain the initial velocity of the ball and then fall under gravity.
### A score of 10 is earned everytime a brick other than unbreakable brick is destroyed 

### There are a total of 3 levels in the game with the last level being the boss level. Score and lives carry across levels. You can press 'p' to skip a level.

### In the boss level only some unbreakable bricks spawn. The boss follows the paddle and drops bombs after regular intervals. If a bomb hits the paddle a life is lost. Every time the ball hits the boss the boss loses a life. When the boss is at health 3 and 6, it spawns a row of bricks under it as protection.

### There is a timer of 100 seconds after which the bricks move down one row every time the ball hits the paddle. If the bottommost brick reaches the paddle the game ends. 

### The ball produces a sound every time it collides with an entity.

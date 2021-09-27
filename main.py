
import pygame


class Player:

    def __init__(self, name):
        self.name = name
        self.squares = []


class Game:

    def __init__(self):
        pygame.init()
        self. window = pygame.display.set_mode((300, 300))
        self. window.fill((255, 255, 255))
        pygame.display.set_caption("Two Player Tic Tac")
        self.blocks = []
        self.player1 = Player('Player 1')
        self.player2 = Player('Player 2')
        self.current_blocks = []
        self.count = 0

    def draw_blocks(self):

        x = y = 0
        width = height = 100
        for i in range(1, 4):
            for j in range(1, 4):
                pygame.draw.rect(self.window, (66, 170, 245), (x, y, width, height), 1)
                pygame.display.flip()
                x += 100
            x = 0
            y += 100

    def draw_cross(self, x, y):

        line1 = pygame.draw.line(self.window, (0, 0, 0), (x, y), (x + 100, y + 100))
        line2 = pygame.draw.line(self.window, (0, 0, 0), (x + 100, y), (x, y + 100))
        pygame.display.flip()

    def draw_circle(self, x, y):

        x = x + 50
        y = y + 50
        circle = pygame.draw.circle(self.window, (188, 164, 222), (x, y), 25)
        pygame.display.flip()

    def determine_block(self, x, y):
        if x == 0 and y == 0:
            return 1
        if x == 100 and y == 0:
            return 2
        if x == 200 and y == 0:
            return 3
        if x == 0 and y == 100:
            return 4
        if x == 100 and y == 100:
            return 5
        if x == 200 and y == 100:
            return 6
        if x == 0 and y == 200:
            return 7
        if x == 100 and y == 200:
            return 8
        if x == 200 and y == 200:
            return 9

    def is_winner(self, squares):
        squares = set(squares)
        if {1,4,7}.issubset(squares) or {2,5,8}.issubset(squares) or {3,6,9}.issubset(squares)
                or {1,2,3}.issubset(squares) or {4, 5, 6}.issubset(squares) or {7,8,9}.issubset(squares) 
                or {1,5,9}.issubset(squares) or {3,5,7}.issubset(squares):
            return True
        return False

    def display_play_again(self):
        font = pygame.font.SysFont('arial', 20)
        play_again = font.render("If You want to play again press ENTER", True, (0, 0, 0))
        self.window.blit(play_again, (10, 150))

    def display_winner(self, player):

        font = pygame.font.SysFont('arial', 30)
        winner = font.render(f"WINNER : {player.name}", True, (0,0,0))
        self.window.blit(winner, (10, 100))
        self.display_play_again()
        pygame.display.flip()

    def reset(self):
        self.window.fill((255, 255, 255))
        self.draw_blocks()
        pygame.display.flip()
        self.current_blocks = []
        self.player1.squares = []
        self.player2.squares = []
        self.count = 0

    def display_DRAW(self):
        font = pygame.font.SysFont('arial', 30)
        draw = font.render("DRAW", True, (0, 0, 0))
        self.window.blit(draw, (10, 100))
        self.display_play_again()
        pygame.display.flip()

    def mouse_button(self, pos):

        x = (pos[0] // 100) * 100
        y = (pos[1] // 100) * 100
        block = self.determine_block(x, y)

        if block in self.current_blocks:
            return False

        self.current_blocks.append(block)
        self.count += 1

        if self.count % 2 == 0:
            self.player2.squares.append(block)
            self.draw_circle(x, y)

            if self.is_winner(self.player2.squares):
                self.display_winner(self.player2)
                return True

        else:
            self.player1.squares.append(block)
            self.draw_cross(x, y)

            if self.is_winner(self.player1.squares):
                self.display_winner(self.player1)
                return True

        if len(self.current_blocks) == 9:
            self.display_DRAW()
            return True

        return False

    def run(self):
        running = True
        self.draw_blocks()
        pygame.time.delay(100)
        pause = False

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if pause:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pause = False
                            self.reset()
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        pause = self.mouse_button(pos)


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()

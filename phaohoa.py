import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set up tiêu đề
pygame.display.set_caption("Pháo Hoa")

# Định nghĩa màu
colors = [
    (255, 0, 0),  # Đỏ
    (0, 255, 0),  # Xanh
    (0, 0, 255),  # Lam
    (255, 255, 0),  # Vàng
    (255, 0, 255),  # Tím
    (0, 255, 255)  # Xanh biển
]

class PhaoHoa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.color = random.choice(colors)
        self.size = random.randint(2, 5)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

def main():
    clock = pygame.time.Clock()
    phao_hoa_list = [PhaoHoa(width // 2, height // 2) for _ in range(100)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for phao_hoa in phao_hoa_list:
            phao_hoa.update()
            phao_hoa.draw()

            if phao_hoa.x < 0 or phao_hoa.x > width or phao_hoa.y < 0 or phao_hoa.y > height:
                phao_hoa.x = width // 2
                phao_hoa.y = height // 2
                phao_hoa.speed_x = random.uniform(-2, 2)
                phao_hoa.speed_y = random.uniform(-2, 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
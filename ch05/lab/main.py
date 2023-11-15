import pygame
import sys

def threenp1(n):
    count = 0
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
        count = count + 1
    return count

def threenp1range(upper_limit):
    objs_in_seq = {}
    start_value = 2

    for number in range(start_value, upper_limit + 1):
        iters = threenp1(number)
        objs_in_seq[number] = iters

    return objs_in_seq

def graph_coordinates(screen, data, x_scale, y_scale):
    coords = []

    for x, y in data.items():
        x_pixel = x * x_scale
        y_pixel = y * y_scale
        coords.append((x_pixel, y_pixel))

    if len(coords) >= 2:
        pygame.draw.lines(screen, ("red"), False, coords, 2)

def main():
    pygame.init()

    WINDOW_WIDTH = 800
    WINDOW_LENGTH = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_LENGTH))

    upper_limit = int(input("Enter the upper limit for the range (>=20): "))

    if upper_limit < 20:
        print("Upper limit should be at least 20.")
        sys.exit()

    results = threenp1range(upper_limit)
    x_scale = WINDOW_WIDTH / upper_limit
    y_scale = WINDOW_LENGTH / max(results.values())

    running = True

    max_iters_key = 0
    max_iters_value = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("light blue")

        graph_coordinates(screen, results, x_scale, y_scale)

        pygame.display.flip()

        font = pygame.font.Font(None, 36)
        max_iters_key = max(results, key=results.get)
        max_iters_value = results[max_iters_key]
        message = f"Max Iterations: {max_iters_key} - {max_iters_value} iterations"
        msg = font.render(message, True, ("Red"))
        screen.blit(msg, (10, 10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
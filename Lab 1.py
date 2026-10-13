
# 1. ФЛАГ Финляндия
import os
import time

CSI = '\x1b['  # ANSI escape code starter
RESET = f'{CSI}0m'  # Reset terminal colors

# Universal 16-color ANSI codes for perfect terminal compatibility
BLUE_BG = f"{CSI}44m"
WHITE_BG = f"{CSI}47m"

def draw_finland_flag(scale=2, delay=0.01):
    """
    Draw Finland flag: blue cross on white background
    Proportions: 11:18 ratio, cross is 3 units thick
    """
    print("--- 1. Finland Flag ---")
    H = 11 * scale  # Height
    W = 18 * scale  # Width
    THICK = 3 * scale  # Cross thickness

    cross_x = 5 * scale  # Vertical bar starts here
    cross_y = 4 * scale  # Horizontal bar starts here

    for y in range(H):
        line = ""
        in_horizontal = cross_y <= y < cross_y + THICK

        for x in range(W):
            in_vertical = cross_x <= x < cross_x + THICK

            if in_horizontal or in_vertical:
                line += f"{BLUE_BG}  {RESET}"
            else:
                line += f"{WHITE_BG}  {RESET}"

        print(line)
        time.sleep(delay)


# 2. повторяющийся узор
def draw_pattern_h(rows=6, cols=8):
    print("\n--- 2. Repeating Pattern ---")
    balls = ["●●"]
    for r in range(rows):
        for line in balls:
            print((line * cols)[:cols * len(line)])


# 3. график функции
def plot_function_first_quadrant(f=lambda x: x/2, x_max=10, width=60, height=20):
    print("\n--- 3. Function Graph ---")
    y_max = f(x_max)
    canvas = [[" " for _ in range(width + 1)] for _ in range(height + 1)]

    for r in range(height + 1):
        canvas[r][0] = "|"
    for c in range(width + 1):
        canvas[height][c] = "-"
    canvas[height][0] = "+"

    for col in range(1, width + 1):
        x = x_max * col / width
        y = f(x)
        if 0 <= y <= y_max:
            row = height - int(round((y / y_max) * height))
            canvas[row][col] = "█"

    for r in range(height + 1):
        print("".join(canvas[r]))


# 4. диаграмму процентного
def read_sequence():
    """Read numbers from sequence.txt file"""
    try:
        with open('sequence.txt', 'r') as f:
            return [float(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        return [7, 8, -7, -8, 6, -6, 9, -9, 10, -10, 5, -5]


def filter_range(values):
    """Keeps only numbers in [-10,-5] or [5,10]."""
    return [v for v in values if (5 <= v <= 10) or (-10 <= v <= -5)]


def chart_last_digit_distribution(values):
    """Draws a percentage chart of the last digit distribution (0-9)."""
    counts = [0] * 10  # Fixed sequence matrix syntax error
    for v in values:
        d = abs(int(round(v))) % 10
        counts[d] += 1
    total = sum(counts) if sum(counts) else 1

    print("\n--- 4. Percentage Chart by Last Digit ---")
    for d, c in enumerate(counts):
        perc = c * 100.0 / total
        bar = "█" * int(round(perc / 2))
        print(f"{d}: {perc:5.1f}% |{bar}")


def clear_console():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


# 5.  анимацию
def animate_three_frames(duration_sec=5):
    """Runs a simple 3-frame animation."""
    frames = ["(•  )", "( • )", "(  •)"]
    t0 = time.time()
    i = 0

    while time.time() - t0 < duration_sec:
        clear_console()
        print("--- 5. Three-frame animation Running ---\n")
        print(frames[i % len(frames)])
        i += 1
        time.sleep(0.2)


# ---------------------------------------------------------
# UNIFIED CENTRAL CONTROL BLOCK (The Gateway)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Clear screen initially for a clean setup
    clear_console()
    
    # Task 1: Draw flag matrix
    draw_finland_flag(scale=2, delay=0.03)
    
    # Task 2: Draw geometric repeating strings
    draw_pattern_h()
    
    # Task 3: Render function plane
    plot_function_first_quadrant()
    
    # Task 4: Load sequence and process distribution chart
    values = read_sequence()
    filtered = filter_range(values)
    print("\nFiltered values database list:", filtered)
    chart_last_digit_distribution(filtered)
    
    # Hold screen safe window lock so you can see tasks 1-4!
    print("\nAll tasks calculated! Loading animation begins in 5 seconds...")
    time.sleep(5)
    
    # Task 5: Launch terminal animation (Wipes previous tasks, runs for 5 seconds)
    animate_three_frames(duration_sec=5)


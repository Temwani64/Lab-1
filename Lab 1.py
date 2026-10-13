# 1. ФЛАГ Финляндия
import os
import time

CSI = '\x1b['  # ANSI escape code starter
RESET = f'{CSI}0m'  # Reset terminal colors


def draw_finland_flag(scale=2, delay=0.03):
    """
    Draw Finland flag: blue cross on white background
    Proportions: 11:18 ratio, cross is 3 units thick
    """
    H = 11 * scale  # Height
    W = 18 * scale  # Width
    THICK = 3 * scale  # Cross thickness

    # Cross position - centered
    cross_x = 5 * scale  # Vertical bar starts here
    cross_y = 4 * scale  # Horizontal bar starts here

    for y in range(H):
        line = ""
        # Check if current row is in horizontal cross section
        in_horizontal = cross_y <= y < cross_y + THICK

        for x in range(W):
            # Check if current column is in vertical cross section
            in_vertical = cross_x <= x < cross_x + THICK

            if in_horizontal or in_vertical:
                line += f"{CSI}48;5;27m  {RESET}"  # Blue
            else:
                line += f"{CSI}48;5;255m  {RESET}"  # White

        print(line)
        time.sleep(delay)  # Animation effect


# 2. повторяющийся узор
if __name__ == "__main__":
    draw_finland_flag(scale=2, delay=0.05)


def draw_pattern_h(rows=6, cols=8):
    balls = [
        "●●"  # Pattern unit - two solid circles
    ]
    # Repeat pattern for specified rows and columns
    for r in range(rows):
        for line in balls:
            # Repeat pattern across columns, trim to exact width
            print((line * cols)[:cols * len(line)])


draw_pattern_h()


# 3. график функции
def plot_function_first_quadrant(f=lambda x: x/2, x_max=10, width=60, height=20):
    # Calculate maximum y value for scaling
    y_max = f(x_max)
    # Create empty canvas (2D grid of spaces)
    canvas = [[" " for _ in range(width + 1)] for _ in range(height + 1)]

    # Draw y-axis (vertical line on left side)
    for r in range(height + 1):
        canvas[r][0] = "|"
    # Draw x-axis (horizontal line on bottom)
    for c in range(width + 1):
        canvas[height][c] = "-"
    # Draw origin point where axes meet
    canvas[height][0] = "+"

    # Plot the function point by point
    for col in range(1, width + 1):
        # Convert column position to x value
        x = x_max * col / width
        y = f(x)
        # Only plot points in first quadrant (positive y)
        if 0 <= y <= y_max:
            # Convert y value to row position (inverted because terminal starts from top)
            row = height - int(round((y / y_max) * height))
            canvas[row][col] = "█"  # Plot point

    # Print the finished graph
    for r in range(height + 1):
        print("".join(canvas[r]))


plot_function_first_quadrant()


# 4. диаграмму процентного
def read_sequence():
    """Read numbers from sequence.txt file"""
    try:
        with open('sequence.txt', 'r') as f:
            return [float(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        # Return sample data if file doesn't exist
        return [7, 8, -7, -8, 6, -6, 9, -9, 10, -10, 5, -5]


def filter_range(values):
    """Keeps only numbers in [-10,-5] or [5,10]."""
    return [v for v in values if (5 <= v <= 10) or (-10 <= v <= -5)]


def chart_last_digit_distribution(values):
    """Draws a percentage chart of the last digit distribution (0-9)."""
    counts = [0] * 10  # Array to count occurrences of each digit 0-9
    for v in values:
        d = abs(int(round(v))) % 10  # Get last digit (absolute value, rounded)
        counts[d] += 1
    total = sum(counts) if sum(counts) else 1  # Avoid division by zero

    print("\nPercentage chart by last digit:\n")
    for d, c in enumerate(counts):
        perc = c * 100.0 / total  # Calculate percentage
        bar = "█" * int(round(perc / 2))  # Each block represents ~2%
        print(f"{d}: {perc:5.1f}% |{bar}")


if __name__ == "__main__":
    values = read_sequence()  # Now this function is defined
    filtered = filter_range(values)
    print("Filtered values:", filtered)
    chart_last_digit_distribution(filtered)


def clear_console():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")  # Windows vs Unix systems


# 5.  анимацию
def animate_three_frames(duration_sec=5):
    """Runs a simple 3-frame animation."""
    frames = ["(•  )", "( • )", "(  •)"]  # Three frames with dot moving
    t0 = time.time()  # Record start time
    i = 0  # Frame counter

    # Run animation for specified duration
    while time.time() - t0 < duration_sec:
        clear_console()  # Clear screen between frames
        print("Three-frame animation:\n")
        print(frames[i % len(frames)])  # Cycle through frames 0,1,2,0,1,2...
        i += 1
        time.sleep(0.2)  # Control animation speed


if __name__ == "__main__":
    animate_three_frames()

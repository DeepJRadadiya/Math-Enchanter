import math
import matplotlib.pyplot as plt

def distance_between_points(x1, y1, x2, y2):
    # formmula: rt((x2​ − x1​)^2 +(y2​ − y1)^2​)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def slope(x1, y1, x2, y2):
    if x1 == x2:
        return None  # undefined slope
    return (y2 - y1) / (x2 - x1)

def equation_of_line(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    if m is None:
        return f"x = {x1}"  # vertical line-equation
    b = y1 - m * x1
    return f"y = {m:.2f}x + {b:.2f}"

def plot_graph(x1, y1, x2, y2):
    plt.figure()
    plt.scatter([x1, x2], [y1, y2], color='red', label='Points')
    plt.plot([x1, x2], [y1, y2], linestyle='--', label='Line Segment')
    
    m = slope(x1, y1, x2, y2)
    if m is not None:
        x_values = [min(x1, x2) - 1, max(x1, x2) + 1]
        y_values = [m * x + (y1 - m * x1) for x in x_values]
        plt.plot(x_values, y_values, label='Equation of Line', color='blue')
    
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.title('Coordinate Geometry Graph')
    plt.grid()
    plt.show()

def main():
    print("Coordinate Geometry Calculator")
    x1, y1 = map(float, input("Enter first point (x1 y1): ").split())
    x2, y2 = map(float, input("Enter second point (x2 y2): ").split())
    
    print(f"Distance between points: {distance_between_points(x1, y1, x2, y2):.2f}")
    print(f"Midpoint: {midpoint(x1, y1, x2, y2)}")
    
    m = slope(x1, y1, x2, y2)
    if m is None:
        print("Slope: Undefined (vertical line)")
    else:
        print(f"Slope: {m:.2f}")
    
    print(f"Equation of line: {equation_of_line(x1, y1, x2, y2)}")
    
    show_graph = input("Do you want to display the graph? (yes/no): ").strip().lower()
    if show_graph == 'yes':
        plot_graph(x1, y1, x2, y2)



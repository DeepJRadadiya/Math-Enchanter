import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# basic equation of linear and quadratic curve
def linear_curve(x, a, b):
    return a * x + b

def quadratic_curve(x, a, b, c):
    return a * x**2 + b * x + c

def fit_curve():
    print("Curve Fitting Tool")
    print("Select the type of curve to fit:")
    print("1. Linear Curve")
    print("2. Quadratic Curve")

    choice = int(input("Enter your choice (1 or 2): "))

    if choice not in [1, 2]:
        print("Invalid choice. Please select 1 or 2.")
        return

    # input data of x and y
    print("\nEnter data points:")
    x_points = list(map(float, input("Enter x values (comma): ").split(',')))
    y_points = list(map(float, input("Enter y values (comma): ").split(',')))
    # print(x_points,y_points)

    if len(x_points) != len(y_points):
        print("Error: Number of x and y values must be the same.")
        return

    x_points = np.array(x_points)
    y_points = np.array(y_points)

    # Curve fitting
    if choice == 1:
        popt, _ = curve_fit(linear_curve, x_points, y_points)
        fitted_y = linear_curve(x_points, *popt)
        equation = f"y = {popt[0]:.2f}x + {popt[1]:.2f}"
    else:
        popt, _ = curve_fit(quadratic_curve, x_points, y_points)
        fitted_y = quadratic_curve(x_points, *popt)
        equation = f"y = {popt[0]:.2f}x^2 + {popt[1]:.2f}x + {popt[2]:.4f}"

    print("\nFitted Curve Equation:")
    print(equation)

    graphChoice = int(input('Enter to see graph 1 or 2 for not:'))
    if graphChoice not in [1,2]:
        print('run again!')
    elif graphChoice == 1:
        # plotting the graph
        plt.scatter(x_points, y_points, color='red', label='Data Points')
        plt.plot(x_points, fitted_y, color='blue', label='Fitted Curve')
        plt.title("Curve Fitting")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.legend()
        plt.grid()
        plt.show()
    else:
        exit

    

if __name__ == "__main__":
    fit_curve()

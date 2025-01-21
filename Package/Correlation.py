import numpy as np
from scipy.stats import spearmanr
import matplotlib.pyplot as plt

def pearson_correlation(x, y):
    return np.corrcoef(x, y)[0, 1]

def spearman_rank_correlation(x, y):
    rank_corr, _ = spearmanr(x, y)
    return rank_corr

def regression_line(x, y):
    #  y = a + bx
    b = np.cov(x, y)[0, 1] / np.var(x)  
    a = np.mean(y) - b * np.mean(x)     
    return a, b

def regression_x_on_y(x, y):
    #  x = a' + b'y
    b_prime = np.cov(x, y)[0, 1] / np.var(y)  
    a_prime = np.mean(x) - b_prime * np.mean(y)  
    return a_prime, b_prime


def correlation_regression_menu():
    print("\nSelect the operation:")
    print("1. Pearson's Correlation Coefficient")
    print("2. Spearman's Rank Correlation Coefficient")
    print("3. Regression Line (Y on X)")
    print("4. Regression Line (X on Y)")
    print("0. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
       
        x = list(map(float, input("Enter X values (comma separated): ").split(',')))
        y = list(map(float, input("Enter Y values (comma separated): ").split(',')))
        print(f"Pearson's Correlation Coefficient: {pearson_correlation(x, y)}")
        
    elif choice == 2:
       
        x = list(map(float, input("Enter X values (comma separated): ").split(',')))
        y = list(map(float, input("Enter Y values (comma separated): ").split(',')))
        print(f"Spearman's Rank Correlation Coefficient: {spearman_rank_correlation(x, y)}")
        
    elif choice == 3:
       
        x = list(map(float, input("Enter X values (comma separated): ").split(',')))
        y = list(map(float, input("Enter Y values (comma separated): ").split(',')))
        a, b = regression_line(x, y)
        print(f"Regression Line (Y on X): y = {a} + {b}x")
        plt.scatter(x, y, color="blue", label="Data points")
        plt.plot(x, a + b * np.array(x), color="red", label="Regression Line")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()

    elif choice == 4:
       
        x = list(map(float, input("Enter X values (comma separated): ").split(',')))
        y = list(map(float, input("Enter Y values (comma separated): ").split(',')))
        a_prime, b_prime = regression_x_on_y(x, y)
        print(f"Regression Line (X on Y): x = {a_prime} + {b_prime}y")
        plt.scatter(x, y, color="green", label="Data points")
        plt.plot(y, a_prime + b_prime * np.array(y), color="orange", label="Regression Line")
        plt.xlabel("Y")
        plt.ylabel("X")
        plt.legend()
        plt.show()

    elif choice == 0:
        print("Exiting...")
        exit()

    else:
        print("Invalid choice. Try again.")
    
    correlation_regression_menu()

if __name__ == "__main__":
    correlation_regression_menu()

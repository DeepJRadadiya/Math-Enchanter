import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def mean_individual(observations):
    return np.mean(observations)

def mean_discrete(values, frequencies):
    return np.sum(np.array(values) * np.array(frequencies)) / np.sum(frequencies)

def mean_continuous(values, frequencies, assumed_mean):
    deviations = np.array(values) - assumed_mean
    mean = assumed_mean + (np.sum(deviations * frequencies) / np.sum(frequencies))
    return mean

def median_individual(observations):
    return np.median(observations)

def median_discrete(values, frequencies):
    cumulative_frequencies = np.cumsum(frequencies)
    total = np.sum(frequencies)
    median_class_index = np.where(cumulative_frequencies >= total / 2)[0][0]
    median = values[median_class_index]
    return median

def mode_individual(observations):
    mode_val = stats.mode(observations)
    return mode_val.mode[0]

def mode_discrete(values, frequencies):
    mode_index = np.argmax(frequencies)
    return values[mode_index]

def standard_deviation_variance(observations):
    variance = np.var(observations)
    std_deviation = np.std(observations)
    return std_deviation, variance

def skewness(observations):
    mean_val = np.mean(observations)
    median_val = np.median(observations)
    std_dev = np.std(observations)
    skew = (3 * (mean_val - median_val)) / std_dev
    return skew

def kurtosis(observations):
    kurt = stats.kurtosis(observations)
    return kurt

def statistics_menu():
    print("\nSelect the statistic to calculate:")
    print("1. Mean")
    print("2. Median")
    print("3. Mode")
    print("4. Standard Deviation and Variance")
    print("5. Skewness")
    print("6. Kurtosis")
    print("0. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        Error: ValueError
    if choice == 1:
        # Mean Calculation
        sub_choice = int(input("\n1. Individual Observations\n2. Discrete Frequency Distribution\n3. Continuous Frequency Distribution (Assumed Mean)\nChoose option: "))
        if sub_choice == 1:
            observations = list(map(float, input("Enter observations (comma separated): ").split(',')))
            print(f"Mean: {mean_individual(observations)}")
        elif sub_choice == 2:
            values = list(map(float, input("Enter values (comma separated): ").split(',')))
            frequencies = list(map(int, input("Enter frequencies (comma separated): ").split(',')))
            print(f"Mean: {mean_discrete(values, frequencies)}")
        elif sub_choice == 3:
            values = list(map(float, input("Enter values (comma separated): ").split(',')))
            frequencies = list(map(int, input("Enter frequencies (comma separated): ").split(',')))
            assumed_mean = float(input("Enter assumed mean: "))
            print(f"Mean: {mean_continuous(values, frequencies, assumed_mean)}")

    elif choice == 2:
        # Median Calculation
        sub_choice = int(input("1. Individual Observations\n2. Discrete Frequency Distribution\nChoose option: "))
        if sub_choice == 1:
            observations = list(map(float, input("Enter observations (comma separated): ").split(',')))
            print(f"Median: {median_individual(observations)}")
        elif sub_choice == 2:
            values = list(map(float, input("Enter values (comma separated): ").split(',')))
            frequencies = list(map(int, input("Enter frequencies (comma separated): ").split(',')))
            print(f"Median: {median_discrete(values, frequencies)}")

    elif choice == 3:
        # Mode Calculation
        sub_choice = int(input("1. Individual Observations\n2. Discrete Frequency Distribution\nChoose option: "))
        if sub_choice == 1:
            observations = list(map(float, input("Enter observations (comma separated): ").split(',')))
            print(f"Mode: {mode_individual(observations)}")
        elif sub_choice == 2:
            values = list(map(float, input("Enter values (comma separated): ").split(',')))
            frequencies = list(map(int, input("Enter frequencies (comma separated): ").split(',')))
            print(f"Mode: {mode_discrete(values, frequencies)}")

    elif choice == 4:
        # Standard Deviation and Variance
        observations = list(map(float, input("Enter observations (comma separated): ").split(',')))
        std_deviation, variance = standard_deviation_variance(observations)
        print(f"Standard Deviation: {std_deviation}, Variance: {variance}")

    elif choice == 5:
        # Skewness Calculation
        observations = list(map(float, input("Enter observations (comma separated): ").split(',')))
        print(f"Skewness: {skewness(observations)}")

    elif choice == 6:
        # Kurtosis Calculation
        observations = list(map(float, input("Enter observations (comma separated): ").split(',')))
        print(f"Kurtosis: {kurtosis(observations)}")

    elif choice == 0:
        print("Exiting...")
        exit()
    
    else:
        print("Invalid choice. Try again.")

    
    statistics_menu()


if __name__ == "__main__":
    statistics_menu()

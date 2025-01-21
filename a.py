# Given data
P = [12, 15, 21, 25]  # Pull in kg-wt
W = [50, 70, 100, 120]  # Load in kg-wt

# Number of data points
n = len(P)

# Summations
sum_W = sum(W)
sum_P = sum(P)
sum_WP = sum(w * p for w, p in zip(W, P))
sum_W2 = sum(w ** 2 for w in W)

# Calculating slope (m) and intercept (C)
m = (n * sum_WP - sum_W * sum_P) / (n * sum_W2 - sum_W ** 2)
C = (sum_P - m * sum_W) / n

# Predicted P for W = 150
W_new = 150
P_new = m * W_new + C

print(m, C, P_new)

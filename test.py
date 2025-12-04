
#===============================================================================

# def get_user_height():
#     height = input("How tall are you in cm?")
#     height = int(height)

#     if height >= 180:
#         print("\nYou are one tall lad")
#     else:
#         print("\nNice you still have way to grow")

# get_user_height()

#===============================================================================

# import numpy as np

# def train_linear_regression(X, y):
#     """Training linear regression."""
#     X = np.asarray(X, dtype=float)
#     y = np.asarray(y, dtype=float)
#     n_samples, n_features = X.shape

#     # Initiatig parameters
#     w = np.zeros(n_features, dtype=float)
#     b = 0.0

#     for epoch in range(1, epochs + 1):
#         preds = X.dot(w) + b
#         errors = preds - y

        


#===================================================================
import numpy as np      # numpy for array + random + math

# defining a function to split data into a train/test set
def train_test_split(X, y, test_size=0.2, seed=42):
    """Splits features X and labels y into training and test parts.
    """
    X = np.asarray(X)           # convert X to numpy array (consistent indexing)
    y = np.asarray(y)           # convert y to a NumPy array (same reason)

    rng = np.random.default_rng(seed)   #create a random number generator with a fixed seed
    idx = np.arange(len(X))             # make indices
    rng.shuffle(idx)                    # shuffle indices randomly

    test_n = int(len(X) * test_size)    # compute number of test rows
    test_idx = idx[:test_n]             #pick first chunk as test indices
    train_idx = idx[test_n:]            # pick remaining as train indices

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx] # return (X_train, X_test, y_train, y_test)

# --- test for function above ---
if __name__ == "__main__":              # run this test when file is executed
    X = [[1], [2], [3], [4], [5]]       # example features (one feature per row)
    y = [2, 4, 6, 8, 10]                # example labels (2x relationship)

    X_train, X_test, y_train, y_test = train_test_split(X, y, 0.4, 1) # split test size 40% and fixed seed 1

    print("X_train:", X_train.tolist()) # print training featuresa
    print("y_train:", y_train.tolist()) # print training labels
    print("X_test:", X_test.tolist())   # print test features
    print("y_test:", y_test.tolist())   # print test labels
#===================================================================
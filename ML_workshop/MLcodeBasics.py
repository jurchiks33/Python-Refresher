
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

#===================================================================
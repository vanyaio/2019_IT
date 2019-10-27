import matplotlib.pyplot as plt
import numpy as np

n = 5
m = 3
X = np.random.rand(n, m)

def index_value(X):
    index = 0
    for value in X:
        yield (index, value)
        index += 1 

def check_if_pareto(idx_to_check, X):
    for idx, vec in index_value(X):
        if idx != idx_to_check and (not np.any(X[idx_to_check] > vec)):
            return False
    return True

def pareto_vectors(X):
    for index, vec in index_value(X):
        if check_if_pareto(index, X):
            yield vec

if __name__ == "__main__":
    print(X.shape)
    _, axis = plt.subplots(ncols=2, subplot_kw=dict(polar=True))
    rotational_angle = np.arange(0, 2 * np.pi + 2 * np.pi / m,  2 * np.pi / m)
    for vector in pareto_vectors(X):
        axis[0].plot(rotational_angle, np.append(vector, vector[0]))
    for vector in X:
        axis[1].plot(rotational_angle, np.append(vector, vector[0]))
    plt.show()

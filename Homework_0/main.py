import numpy as np

if __name__ == "__main__":
    # Basic example of python
    print(r"Example of python", "\n")
    a, b = 1.0, 2.0
    print(r"a = {}".format(a), "\n")
    print(r"a / b = {}".format(a / b), "\n")
    print(r"np.sqrt(b) =  {}".format(np.sqrt(b)), "\n")
    print(r"np.arccos(-1) = {}".format(np.arccos(-1)), "\n")
    print(r"np.sin(30.0 / 180.0 * np.arccos(-1)) = {}".format(np.sin(30.0 / 180.0 * np.arccos(-1))), "\n")

    # Example of vector
    print(r"Example of vector", "\n")
    v = np.array([1.0, 2.0, 3.0])
    w = np.array([1.0, 0.0, 0.0])
    print(r"v = {}".format(v), "\n")
    print(r"v + w = {}".format(v + w), "\n")
    print(r"v * 3.0 = ".format(v * 3.0), "\n")
    print(r"2.0 * v = {}".format(2.0 * v), "\n")

    # Example of matrix
    i = np.array([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0],
                  [7.0, 8.0, 9.0]], dtype=np.float32)
    j = np.array([[2.0, 3.0, 1.0],
                  [4.0, 6.0, 5.0],
                  [9.0, 7.0, 8.0]], dtype=np.float32)
    print(r"i = {}".format(i), "\n")
    print(r"i + j".format(i + j), "\n")
    print(r"i * 2.0 = {}".format(i * 2.0), "\n")
    print(r"i.dot(j) = {}".format(i.dot(j)), "\n")
    print(r"i.dot(v) = {}".format(i.dot(v)), "\n")

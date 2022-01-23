# import pandas
import numpy as np
import gram_schmidt as ga


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print('Hola')
    A = np.array([[1,0,1],[1,1,0],[0,1,1]], np.int32)
    Q = ga.gram_schmidt_ortonorm(A)




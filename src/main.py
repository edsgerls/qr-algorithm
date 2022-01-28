# import pandas
import numpy as np
import gram_schmidt as ga


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    A = np.array([[2,1],[1,2]])

    P = np.identity(2)

    while not (np.allclose(A,np.tril(A)) or np.allclose(A,np.triu(A))):

        Q = ga.gram_schmidt_ortonorm(A)
        P = np.matmul(P,Q)

        # Compute Ri matrix
        R = np.matmul(np.transpose(Q),A)

        Anew = np.matmul(R,Q)

        A = Anew

    print(A.diagonal())
    print(P)


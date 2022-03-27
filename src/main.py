# import pandas
import numpy as np
import gram_schmidt as gs


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    A = np.array([[2,1],[1,2]])


    m, n = np.shape(A)
    P = np.identity(n)

    # TODO: pending to check for symmetry
    if np.allclose(A, A.T, rtol=1e-05, atol=1e-05):

        while not (np.allclose(A,np.tril(A)) or np.allclose(A,np.triu(A))):

            Q = gs.gram_schmidt_ortonorm(A)
            P = np.matmul(P,Q)

            # Compute Ri matrix
            R = np.matmul(np.transpose(Q),A)

            Anew = np.matmul(R,Q)

            A = Anew

    print(A.diagonal())
    print(P)


import numpy as np

# TODO Comment every section

def gram_schmidt_ortonorm(A):
    m, n = np.shape(A)
    tmp = []

    for k in range(n):
        vk = A[:,k]
        Q = np.transpose(np.array(tmp))

        proy = 0
        for i in range(1, k+1):
            ui = Q[:,i-1]
            proy += (np.dot(vk,ui)) * ui

        vpk = vk - proy
        ui = vpk / np.linalg.norm(vpk)
        tmp.append(ui)

    return np.transpose(np.array(tmp))

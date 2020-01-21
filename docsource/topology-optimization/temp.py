# ==============================================================================
# 2D Example 1
# ==============================================================================

# from matplotlib import pyplot as plt

# nelx = 400
# nely = 40

# plt.figure(figsize=(12, 8))
# plt.axis([0, nelx, 0, nely])
# plt.ion()

# def callback(x):
#     plt.imshow(1 - x, cmap='gray', origin='lower')
#     plt.pause(0.001)

# loads = {
#     '200-40': [0, -1],
# }

# supports = {
#     '0-0': [1, 1],
#     '400-0': [0, 1],
# }

# x = topop_numpy(nelx=nelx, nely=nely, loads=loads, supports=supports, volfrac=0.5, callback=callback)

# ==============================================================================
# 2D Example 2
# ==============================================================================

from matplotlib import pyplot as plt

nelx = 100
nely = 200

plt.figure(figsize=(12, 8))
plt.axis([0, nelx, 0, nely])
plt.ion()

def callback(x):
    plt.imshow(1 - x, cmap='gray', origin='lower')
    plt.pause(0.001)

loads = {
    '0-50': [1, 0],
    '0-100': [1, 0],
    '0-150': [1, 0],
    '0-200': [1, 0],
}

supports = {
    '0-0': [1, 1],
    '50-0': [1, 1],
    '100-0': [1, 1],
}

x = topop_numpy(nelx=nelx, nely=nely, loads=loads, supports=supports, volfrac=0.3, callback=callback)

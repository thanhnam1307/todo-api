Ptrans = (16, -7, 42.5, 1)

theta = 30 * np.pi / 180

rotation_matrix = np.array([
    [np.cos(theta), 0, np.sin(theta), 0],
    [0, 1, 0, 0],
    [-np.sin(theta), 0, np.cos(theta), 0],
    [0, 0, 0, 1]
])

Prot = np.dot(Ptrans, rotation_matrix)

print("Tọa độ của điểm Prot:", Prot[:3])

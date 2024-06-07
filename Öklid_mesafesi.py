import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (8, 10), (10, 10)]

# Öklid mesafesi fonksiyonunu tanımlama
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Mesafelerin hesaplanması
distances = []
num_points = len(points)

for i in range(num_points):
    for j in range(i + 1, num_points):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

print("Mesafelerin hesaplanması:", distances)

# Sonucu yazdırma
print("Minimum Öklid Mesafesi:", min_distance)

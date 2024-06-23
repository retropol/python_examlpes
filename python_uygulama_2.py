import sys

points = []
distances = []

def euclideanDistance(r1, q1, r2, q2):
    return ((r2 - r1) ** 2 + (q2 - q1) ** 2) ** 0.5

# Kullanıcıdan nokta koordinatlarını almak
for i in range(5):
    x = float(input(f"Bir x koordinatı giriniz (çift {i+1}): "))
    y = float(input(f"Bir y koordinatı giriniz (çift {i+1}): "))
    points.append([x, y])


for i in range(5):
    for k in range(5):
        if i == k:
            continue
        q1, r1 = points[i]
        q2, r2 = points[k]
        distance = euclideanDistance(r1, q1, r2, q2)
        distances.append(distance)


formatted_distances = [format(dist, ".2f") for dist in distances]

print("Noktalar:", points)
print("Mesafeler:", formatted_distances)


enkucuk = sys.float_info.max

for distance in formatted_distances:
    if float(distance) < enkucuk:
        enkucuk = float(distance)

print(f"En küçük mesafe: {enkucuk}")

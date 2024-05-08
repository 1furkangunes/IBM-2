import math

points = (3,4), (7,8), (10,12)
distance = []
def euclideanDistance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance.append(euclideanDistance(points[i], points[j]))

print("Minimum Distance:",  {min(distance)})

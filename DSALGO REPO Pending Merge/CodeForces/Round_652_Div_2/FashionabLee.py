
def isPolygonBeautiful(polygons):
    for polygon in polygons:
        if polygon % 4 == 0:
            print("YES")
        else:  
            print("NO")

if __name__ == "__main__":
    t = int(input())
    polygons = []
    for _ in range(t):
        polygons.append(int(input()))

    isPolygonBeautiful(polygons)
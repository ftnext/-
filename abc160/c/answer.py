lake_circumference, house_count = map(int, input().split())
locations = list(map(int, input().split()))
min_distance = 10e6
for i in range(house_count):
    if i == 0:
        distance = locations[house_count-1] - locations[0]
    else:
        distance = lake_circumference + locations[i-1] - locations[i]
    if distance < min_distance:
        min_distance = distance
print(min_distance)

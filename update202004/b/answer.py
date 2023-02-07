# 読み間違えで動かない
ballCountN = int(input())
blueBalls = []
redBalls = []
for _ in range(ballCountN):
    number_str, color = input().split()
    if color == 'B':
        blueBalls.append(int(number_str))
    elif color == 'R':
        redBalls.append(int(number_str))
blueBalls.sort()
redBalls.sort()
while True:
    if len(redBalls) > 0:
        print(redBalls.pop(0))
    if len(blueBalls) > 0:
        print(blueBalls.pop(0))
    if len(redBalls) == 0 and len(blueBalls) == 0:
        break

N = int(input())
the_highest_name = None
second_highest_name = None
first_height = None
second_height = None

for i in range(N):
    name, height_str = input().split()
    height = int(height_str)
    if i == 0:
        second_highest_name, second_height = name, height
        continue
    if i == 1:
        if second_height > height:
            the_highest_name, first_height = second_highest_name, second_height
            second_highest_name, second_height = name, height
        else:
            the_highest_name, first_height = name, height
        continue

    # 暫定1位も暫定2位も決まっている場合
    if height < second_height:
        continue
    elif height < first_height:
        second_highest_name, second_height = name, height
    else:  # first_height < height
        second_highest_name, second_height = the_highest_name, first_height
        the_highest_name, first_height = name, height

print(second_highest_name)

"""Create large data

N = int(1e5)
with open("large.txt", "w") as fout:
    fout.write(f"{N}\n")
    for i in range(1, N+1):
        fout.write(f"{i} {i}\n")
"""

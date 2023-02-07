# historyを文字列としてもたせるアイディアを試す
# 123と321の重複が解消できていない
# 3245 -> 345 に対応できていない
import re


number_vertices, x, y = map(int, input().split())
connections = {}
for i in range(1, number_vertices+1):
    next_vertices = []
    if i != 1:
        next_vertices.append(i-1)
    if i != number_vertices:
        next_vertices.append(i+1)
    connections[i] = next_vertices
connections[x].append(y)
connections[y].append(x)


def count_distance(v_i, k, history_str):
    if k == 0:
        history = history_str + str(v_i)
        result = set(history)
        if len(history) != len(result):
            # たどった頂点に重複がある時はカウントしない
            return 0
        cleaned_history = re.sub(f'{x}.+{y}', f'{x}{y}', history)
        cleaned_history = re.sub(f'{y}.+{x}', f'{y}{x}', cleaned_history)
        print(history, cleaned_history)
        if len(cleaned_history) < len(history):
            # 最短距離でないのでカウントしない
            return 0
        return 1
    else:
        nexts = connections[v_i]
        sum_count = 0
        for v_n in nexts:
            new_history = history_str + str(v_i)
            sum_count += count_distance(v_n, k-1, new_history)
        return sum_count


print(number_vertices)  # k=1の出力
for k in range(2, number_vertices):  # k=2, N-1まで
    count = 0
    for i in range(1, number_vertices+1):
        count += count_distance(i, k, '')
    print(count)

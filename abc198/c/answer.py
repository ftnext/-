import math
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def euclidean_distance(p1: Point, p2: Point) -> float:
    """
    >>> euclidean_distance(Point(0, 0), Point(0, 5))
    5.0
    """
    distance_square = (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2
    return math.sqrt(distance_square)


def walk_step(distance: float, radius: float) -> int:
    """
    >>> walk_step(5.0, 5.0)
    1
    >>> walk_step(6.0, 5.0)
    2
    >>> walk_step(15.0, 5.0)
    3
    >>> walk_step(11.0, 5.0)
    3
    >>> walk_step(4 * math.sqrt(2), 3.0)
    2
    """
    if math.isclose(distance, radius):
        return 1
    if distance < 2 * radius:
        return 2
    return 1 + walk_step(distance - radius, radius)


if __name__ == "__main__":
    R, X, Y = list(map(int, input().split()))
    start = Point(0, 0)
    goal = Point(X, Y)
    distance = euclidean_distance(start, goal)
    print(walk_step(distance, float(R)))

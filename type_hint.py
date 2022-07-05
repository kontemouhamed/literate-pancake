
# import math
from typing import List

# def circle_surface(radius: float) -> float:
#     return 3.141516 * math.sqrt(radius)


# def square(number: int) -> int:
#     return number ** 2


# if __name__ == '__main__':
#     print(square(3))
#     print(square(3.14))
CONSTANT = 1


def example() -> None:
    first_item = 1
    items = [first_item, None]
    reveal_locals()


Vector = List[float]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(2.14, [1.0, 3.14]))


if __name__ == '__main__':
    print(scale(2.14, [1.0, 3.14]))

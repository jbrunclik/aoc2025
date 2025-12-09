#!/usr/bin/env python3
"""Day 9: Largest rectangles."""


from aoc import load_lines

from dataclasses import dataclass


@dataclass
class Tile:
    x: int
    y: int


@dataclass
class Edge:
    is_vertical: bool
    fixed: int
    var_min: int
    var_max: int


class Rectangle:
    __slots__ = ("x1", "x2", "y1", "y2")

    def __init__(self, xa: int, xb: int, ya: int, yb: int) -> None:
        self.x1 = min(xa, xb)
        self.x2 = max(xa, xb)
        self.y1 = min(ya, yb)
        self.y2 = max(ya, yb)

    def area(self) -> int:
        """Calculate the area of the rectangle."""
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1)


def parse_tiles(input_lines: list[str]) -> list[Tile]:
    """Parse input lines into tile coordinates."""
    tiles = []
    for line in input_lines:
        x, y = map(int, line.split(","))
        tiles.append(Tile(x, y))
    return tiles


def find_rectangles(tiles: list[Tile]) -> list[Rectangle]:
    """Generate all rectangle pairs."""
    rectangles = []
    for i, tile in enumerate(tiles):
        for other in tiles[i + 1 :]:
            rectangles.append(Rectangle(tile.x, other.x, tile.y, other.y))

    rectangles.sort(key=lambda r: r.area(), reverse=True)
    return rectangles


def part1(rectangles: list[Rectangle]) -> int:
    """Find the area of the largest rectangle."""
    return rectangles[0].area()


def iter_edges(polygon: list[Tile]):
    """Yield all edges of the polygon."""
    n = len(polygon)
    for i in range(n):
        v1 = polygon[i]
        v2 = polygon[(i + 1) % n]  # wrap around
        if v1.x == v2.x:
            yield Edge(True, v1.x, min(v1.y, v2.y), max(v1.y, v2.y))
        else:
            yield Edge(False, v1.y, min(v1.x, v2.x), max(v1.x, v2.x))


def edge_crosses_rectangle(edge: Edge, rectangle: Rectangle) -> bool:
    """Check if an edge crosses the rectangle."""
    if edge.is_vertical:
        return (
            rectangle.x1 < edge.fixed < rectangle.x2
            and edge.var_min < rectangle.y2
            and edge.var_max > rectangle.y1
        )
    else:
        return (
            rectangle.y1 < edge.fixed < rectangle.y2
            and edge.var_min < rectangle.x2
            and edge.var_max > rectangle.x1
        )


def is_rectangle_valid(rectangle: Rectangle, polygon: list[Tile]) -> bool:
    """Check if rectangle is inside the bounding polygon."""
    for edge in iter_edges(polygon):
        if edge_crosses_rectangle(edge, rectangle):
            return False
    return True


def part2(rectangles: list[Rectangle], polygon: list[Tile]) -> int:
    """Find the area of the largest rectangle inside the bounding polygon."""
    for rectangle in rectangles:
        if is_rectangle_valid(rectangle, polygon):
            return rectangle.area()
    return 0


if __name__ == "__main__":
    input_lines = load_lines(9)
    tiles = parse_tiles(input_lines)
    rectangles = find_rectangles(tiles)
    print(part1(rectangles))
    print(part2(rectangles, tiles))

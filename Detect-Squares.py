class DetectSquares:

    def __init__(self):
        self.dict_coordinates = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.dict_coordinates[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        dx, dy = point
        for tuple_, freq in list(self.dict_coordinates.items()):
            x, y = tuple_
            if abs(dx - x) != abs(dy - y) or dx == x or dy == y:
                continue
            # if not at equal distance on both axes or points are same on either axis
            # cant form a square
            
            count += freq * self.dict_coordinates[(dx, y)] * self.dict_coordinates[(x, dy)]
        return count 
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
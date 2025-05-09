from abc import ABC, abstractmethod
from typing import Tuple

# Abstract Base Class
class Furniture(ABC):
    def __init__(self, material: str, size: Tuple[float, float, float], weight_limit: float):
        self.material = material
        self.size = size  # (width, depth, height)
        self.weight_limit = weight_limit


    @abstractmethod
    def assemble(self) -> str:
        pass

    @abstractmethod
    def disassemble(self) -> str:
        pass


# Chair Subclass
class Chair(Furniture):
    def __init__(self, material, size, weight_limit, has_armrest: bool, legs: int):
        super().__init__(material, size, weight_limit)
        self.has_armrest = has_armrest
        self.legs = legs

    def assemble(self):
        return "Chair assembled by attaching legs and armrest."

    def disassemble(self):
        return "Chair disassembled by removing legs and armrest."


# Table Subclass
class Table(Furniture):
    def __init__(self, material, size, weight_limit, shape: str, has_drawers: bool):
        super().__init__(material, size, weight_limit)
        self.shape = shape
        self.has_drawers = has_drawers

    def assemble(self):
        return "Table assembled by fixing tabletop and legs."

    def disassemble(self):
        return "Table disassembled by detaching tabletop and legs."


# Sofa Subclass
class Sofa(Furniture):
    def __init__(self, material, size, weight_limit, color: str, is_recliner: bool):
        super().__init__(material, size, weight_limit)
        self.color = color
        self.is_recliner = is_recliner

    def assemble(self):
        return "Sofa assembled by joining frame and cushions."

    def disassemble(self):
        return "Sofa disassembled by separating cushions and frame."
    
class Bookshelf(Furniture):
    def __init__(self, material, size, weight_limit, color: str):
        def


# Object creation and method testing
if __name__ == "__main__":
    chair = Chair("Wood", (45.0, 45.0, 90.0), 120.0, True, 4)
    table = Table("Metal", (120.0, 80.0, 75.0), 200.0, "Rectangle", True)
    sofa = Sofa("Leather", (200.0, 90.0, 100.0), 120.0, "Pink", True)

    for furniture in [chair, table, sofa]:
        print(f"{furniture.__class__.__name__}:")
        print(f"  Material: {furniture.material}")
        print(f"  Size: {furniture.size}")
        print(f"  Weight Limit: {furniture.weight_limit} kg")
        print(f"  Assemble: {furniture.assemble()}")
        print(f"  Disassemble: {furniture.disassemble()}")
        print()

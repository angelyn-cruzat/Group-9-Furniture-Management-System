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
    def __init__(self, material, size, weight_limit, color: str, has_books: bool):
        super().__init__(material,size,weight_limit)
        self.color = color
        self.has_books = has_books
        
    def assemble(self):
        return "Bookshelf assembled by joining screws and shelves."
        
    def disassemble(self):
        return "Bookshelf disassembled by removing screws and shelves."


if __name__ == "__main__":
    chair = Chair("Wood", (45.0, 45.0, 90.0), 4.0, True, 4)
    table = Table("Metal", (300.0, 80.0, 75.0), 18.0, "Rectangle", True)
    sofa = Sofa("Leather", (200.0, 90.0, 100.0), 120.0, "Pink", True)
    bookshelf = Bookshelf("Wood", (80.0, 30.0, 202.0), 125.0, "White", True)

    for furniture in [chair, table, sofa, bookshelf]:
        print(f"{furniture.__class__.__name__}:")
        print(f"  Material: {furniture.material}")
        print(f"  Size: {furniture.size}")
        print(f"  Weight Limit: {furniture.weight_limit} kg")
        
        if isinstance(furniture, Chair):
            print(f"  Legs: {furniture.legs}")
        elif isinstance(furniture, Table):
            print(f"  Shape: {furniture.shape}")
        elif isinstance(furniture, Sofa):
            print(f"  Color: {furniture.color}")
        elif isinstance(furniture, Bookshelf):
            print(f"  Color: {furniture.color}")
        
        print(f"  Assemble: {furniture.assemble()}")
        print(f"  Disassemble: {furniture.disassemble()}")
        print()


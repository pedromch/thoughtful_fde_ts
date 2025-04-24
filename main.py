from enum import StrEnum
from typing import Any

class InputKey(StrEnum):
    WIDTH = "width"
    HEIGHT = "height"
    LENGTH = "length"
    MASS = "mass"

class Stack(StrEnum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED" 
    
INPUT_KEYS_TO_TYPES: dict[InputKey, type] = {
    InputKey.WIDTH: int,
    InputKey.HEIGHT: int,
    InputKey.LENGTH: int,
    InputKey.MASS: int
}

def validate_input(input_: Any):
    if not isinstance(input_, dict):
        raise TypeError("Input should be a valid dict.")
        
    for key, type_ in INPUT_KEYS_TO_TYPES.items():
        value = input_.get(key)
        if value is None:
            raise ValueError(f"Missing {key} entry in input.")
            
        if not isinstance(value, type_):
            raise ValueError(f"{key}'s type is wrong, it should be {type_.__name__}.")
        
        if type_ == int and value <= 0:
            raise ValueError(f"{key} must be greater than 0.")
        
        

def is_bulky(width: int, height: int, length: int):
    volume = 1
    for dimension in (width, height, length):
        if dimension >= 150:
            return True
        
        volume *= dimension
        if volume >= 1e6:
            return True
        
    return False

def is_heavy(mass: int):
    return mass >= 20

def sort(width: int, height: int, length: int, mass:int):
    package_is_bulky = is_bulky(width, height, length)
    package_is_heavy = is_heavy(mass)

    if package_is_bulky and package_is_heavy:
        return Stack.REJECTED
    
    if package_is_bulky or package_is_heavy:
        return Stack.SPECIAL
    
    return Stack.STANDARD


if __name__ == "__main__":
    import json
    from pathlib import Path
    
    INPUT_PATH = Path(__file__).parent.joinpath("input.json")
    input_ = json.loads(INPUT_PATH.read_bytes())
    validate_input(input_)

    width, height, length, mass = (input_[key] for key in input_.keys())
    print(sort(width, height, length, mass))
    


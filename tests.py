from main import Stack, is_bulky, is_heavy, sort


def bulky_when_dimension_higher_or_equal_to_150():
    not_bulky_dimension = 10
    bulky_dimension = 150

    assert is_bulky(bulky_dimension, not_bulky_dimension, not_bulky_dimension) == True
    assert is_bulky(not_bulky_dimension, bulky_dimension, not_bulky_dimension) == True
    assert is_bulky(not_bulky_dimension, not_bulky_dimension, bulky_dimension) == True
    assert is_bulky(not_bulky_dimension, not_bulky_dimension, not_bulky_dimension) == False
    
def bulky_when_volume_higher_or_equal_to_1e6():
    bulky_dimensions = (100, 100, 100)

    assert is_bulky(*bulky_dimensions) == True

    not_bulky_dimensions = (10, 10, 10)
    assert is_bulky(*not_bulky_dimensions) == False
    
def heavy_when_mass_higher_or_equal_to_20():
    heavy_mass = 20
    assert is_heavy(heavy_mass) == True

    not_heavy_mass = 10
    assert is_heavy(not_heavy_mass) == False
    
def rejected_when_bulky_and_heavy():
    bulky_dimensions = (100, 100, 100)
    heavy_mass = 20
    
    assert sort(*bulky_dimensions, heavy_mass) == Stack.REJECTED
    
def special_when_bulky_or_heavy():
    bulky_dimensions = (100, 100, 100)
    not_heavy_mass = 10
    
    assert sort(*bulky_dimensions, not_heavy_mass) == Stack.SPECIAL
    
    not_bulky_dimensions = (10, 10, 10)
    heavy_mass = 20
    assert sort(*not_bulky_dimensions, heavy_mass) == Stack.SPECIAL
    
def standard_when_not_bulky_nor_heavy():
    not_bulky_dimensions = (10, 10, 10)
    not_heavy_mass = 10

    assert sort(*not_bulky_dimensions, not_heavy_mass) == Stack.STANDARD
    

if __name__ == "__main__":
    bulky_when_dimension_higher_or_equal_to_150()
    bulky_when_volume_higher_or_equal_to_1e6()
    heavy_when_mass_higher_or_equal_to_20()
    rejected_when_bulky_and_heavy()
    special_when_bulky_or_heavy()
    standard_when_not_bulky_nor_heavy()
    
    
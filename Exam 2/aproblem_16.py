# Primary function
def numcondition(a: int, b: int):
    """Returns one or two booleans based on certain conditions"""
    condition_one = (a + b) > 10
    condition_two = (a * b) > 20

    if condition_one and condition_two:
        return True
    if (not condition_one) and (not condition_two):
        return False
    
    return condition_one, condition_two

# Test cases
print(f"5 and 4 (FALSE): {numcondition(5, 4)}")
print(f"2 and 9 (TRUE, FALSE): {numcondition(2, 9)}")
print(f"6 and 4 (FALSE, TRUE): {numcondition(6, 4)}")
print(f"10 and 10 (TRUE): {numcondition(10, 10)}")
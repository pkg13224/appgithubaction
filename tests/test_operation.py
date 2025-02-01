from src.math_operations import add, sub

def test_add():
    assert add(2, 3)==5 ## assert check whatever output we get from add(2, 3) is equal to 5 or not,if equal then it will give true
    assert add(-1, 1)==0

def test_sub():
    assert sub(5, 3)==2
    assert sub(4, 3)==1
    assert sub(3, 3)==0
    assert sub(2, 7)==-5

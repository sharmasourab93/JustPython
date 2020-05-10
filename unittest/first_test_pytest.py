def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"
    
    
def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]
    

if __name__ == '__main__':
    test_reversed()
    test_uppercase()
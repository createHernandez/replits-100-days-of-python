string = "racecars"

def test_palindrome_loop(string): 
    if len(string) == 1: 
        return True
    for i in range(len(string) // 2): 
        if string[0] != string[-1]: 
            return False
    return True

def test_palindrome_recursive(string): 
    if len(string) <= 1: 
        return True
    if string[0] != string[-1]: 
        return False
    return test_palindrome_recursive(string[1:-1])

print(f"Is {string} a palindrome?\n")
print(f"Loop Test: {test_palindrome_loop(string)}")
print(f"Recursive Test: {test_palindrome_recursive(string)}")

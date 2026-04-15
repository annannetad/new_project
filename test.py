def count_max(lst):
    if not lst:
        return 0
    max_value = max(lst)
    count = lst.count(max_value)
    return count        
# Example usage:
numbers = [1, 3, 2, 3, 4, 4, 4]
result = count_max(numbers)
print(result)  # Output: 3  

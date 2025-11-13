"""
Inefficient Code Examples - Common Performance Issues
This file demonstrates various performance anti-patterns
"""
import time


def inefficient_string_concatenation(items):
    """
    INEFFICIENT: Using += for string concatenation in a loop
    Time Complexity: O(n²) due to string immutability
    """
    result = ""
    for item in items:
        result += str(item) + ","  # Creates new string object each iteration
    return result


def inefficient_list_contains(target_list, search_items):
    """
    INEFFICIENT: Using list for membership testing
    Time Complexity: O(n*m) where n is search_items and m is target_list
    """
    found = []
    for item in search_items:
        if item in target_list:  # O(n) lookup for each item
            found.append(item)
    return found


def inefficient_loop_invariant(data, multiplier):
    """
    INEFFICIENT: Repeating expensive calculations inside loop
    """
    results = []
    for item in data:
        # Expensive calculation repeated every iteration
        expensive_value = sum(range(1000)) * multiplier
        results.append(item * expensive_value)
    return results


def inefficient_nested_loops(list1, list2):
    """
    INEFFICIENT: Nested loops where it could be avoided
    Time Complexity: O(n²)
    """
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                common.append(item1)
    return common


def inefficient_data_structure(n):
    """
    INEFFICIENT: Using wrong data structure for the job
    Creating a list and then checking membership repeatedly
    """
    seen = []  # Should use set
    unique = []
    for i in range(n):
        if i % 2 == 0:
            if i not in seen:  # O(n) operation
                seen.append(i)
                unique.append(i)
    return unique


def inefficient_file_operations(filename, lines):
    """
    INEFFICIENT: Opening/closing file in a loop
    """
    for line in lines:
        with open(filename, 'a') as f:  # Opens file each iteration
            f.write(line + '\n')


def inefficient_global_lookup():
    """
    INEFFICIENT: Repeated global variable lookups
    """
    total = 0
    for i in range(10000):
        total += len([1, 2, 3, 4, 5])  # Looks up 'len' globally each time
    return total


def inefficient_regex_compilation(texts):
    """
    INEFFICIENT: Compiling regex inside loop
    """
    import re
    results = []
    for text in texts:
        pattern = re.compile(r'\d+')  # Recompiles same pattern
        matches = pattern.findall(text)
        results.extend(matches)
    return results


def inefficient_dict_get(data_dict, keys):
    """
    INEFFICIENT: Using dict access without default
    """
    results = []
    for key in keys:
        if key in data_dict:  # Checks existence then accesses
            results.append(data_dict[key])
        else:
            results.append(None)
    return results


def inefficient_list_extension(items):
    """
    INEFFICIENT: Using append in loop instead of extend
    """
    result = []
    for item in items:
        if isinstance(item, list):
            for sub_item in item:  # Manual iteration
                result.append(sub_item)
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    # Quick demonstrations
    print("Inefficient string concatenation:")
    start = time.time()
    result = inefficient_string_concatenation(range(5000))
    print(f"Time: {time.time() - start:.4f}s, Length: {len(result)}")
    
    print("\nInefficient list contains:")
    start = time.time()
    target = list(range(1000))
    search = list(range(500, 1500))
    result = inefficient_list_contains(target, search)
    print(f"Time: {time.time() - start:.4f}s, Found: {len(result)}")

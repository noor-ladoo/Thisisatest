"""
Unit Tests for Inefficient and Optimized Code
Validates that both implementations produce identical results
"""
import unittest
import os
import tempfile
from inefficient_code import (
    inefficient_string_concatenation,
    inefficient_list_contains,
    inefficient_loop_invariant,
    inefficient_nested_loops,
    inefficient_data_structure,
    inefficient_global_lookup,
    inefficient_regex_compilation,
    inefficient_dict_get,
    inefficient_list_extension
)
from optimized_code import (
    optimized_string_concatenation,
    optimized_list_contains,
    optimized_loop_invariant,
    optimized_nested_loops,
    optimized_data_structure,
    optimized_global_lookup,
    optimized_regex_compilation,
    optimized_dict_get,
    optimized_list_extension
)


class TestCodeOptimizations(unittest.TestCase):
    """Test that optimized code produces same results as inefficient code"""
    
    def test_string_concatenation(self):
        """Test string concatenation optimization"""
        test_cases = [
            [],
            [1],
            [1, 2, 3, 4, 5],
            list(range(100))
        ]
        
        for test_input in test_cases:
            with self.subTest(input=test_input):
                result_ineff = inefficient_string_concatenation(test_input)
                result_opt = optimized_string_concatenation(test_input)
                self.assertEqual(result_ineff, result_opt)
    
    def test_list_contains(self):
        """Test list membership testing optimization"""
        test_cases = [
            ([], []),
            ([1, 2, 3], [2, 3, 4]),
            (list(range(100)), list(range(50, 150))),
            ([1, 2, 3], [4, 5, 6])  # No overlap
        ]
        
        for target, search in test_cases:
            with self.subTest(target=target, search=search):
                result_ineff = inefficient_list_contains(target, search)
                result_opt = optimized_list_contains(target, search)
                self.assertEqual(sorted(result_ineff), sorted(result_opt))
    
    def test_loop_invariant(self):
        """Test loop invariant code motion optimization"""
        test_cases = [
            ([], 1),
            ([1], 2),
            ([1, 2, 3, 4, 5], 3),
            (list(range(50)), 10)
        ]
        
        for data, multiplier in test_cases:
            with self.subTest(data=data, multiplier=multiplier):
                result_ineff = inefficient_loop_invariant(data, multiplier)
                result_opt = optimized_loop_invariant(data, multiplier)
                self.assertEqual(result_ineff, result_opt)
    
    def test_nested_loops(self):
        """Test nested loops optimization"""
        test_cases = [
            ([], []),
            ([1, 2, 3], [2, 3, 4]),
            ([1, 2, 3], [4, 5, 6]),  # No overlap
            (list(range(50)), list(range(25, 75)))
        ]
        
        for list1, list2 in test_cases:
            with self.subTest(list1=list1, list2=list2):
                result_ineff = inefficient_nested_loops(list1, list2)
                result_opt = optimized_nested_loops(list1, list2)
                self.assertEqual(sorted(result_ineff), sorted(result_opt))
    
    def test_data_structure(self):
        """Test data structure choice optimization"""
        test_cases = [0, 1, 10, 100]
        
        for n in test_cases:
            with self.subTest(n=n):
                result_ineff = inefficient_data_structure(n)
                result_opt = optimized_data_structure(n)
                self.assertEqual(result_ineff, result_opt)
    
    def test_global_lookup(self):
        """Test global variable lookup optimization"""
        result_ineff = inefficient_global_lookup()
        result_opt = optimized_global_lookup()
        self.assertEqual(result_ineff, result_opt)
    
    def test_regex_compilation(self):
        """Test regex compilation optimization"""
        test_cases = [
            [],
            ["No numbers here"],
            ["123", "456", "789"],
            ["Mix 123 with text 456", "Numbers: 789 and 012"],
            [f"Number {i}" for i in range(20)]
        ]
        
        for texts in test_cases:
            with self.subTest(texts=texts):
                result_ineff = inefficient_regex_compilation(texts)
                result_opt = optimized_regex_compilation(texts)
                self.assertEqual(result_ineff, result_opt)
    
    def test_dict_get(self):
        """Test dictionary access pattern optimization"""
        test_cases = [
            ({}, []),
            ({1: 'a', 2: 'b'}, [1, 2, 3]),
            ({i: i*2 for i in range(100)}, list(range(50, 150)))
        ]
        
        for data_dict, keys in test_cases:
            with self.subTest(data_dict=len(data_dict), keys=len(keys)):
                result_ineff = inefficient_dict_get(data_dict, keys)
                result_opt = optimized_dict_get(data_dict, keys)
                self.assertEqual(result_ineff, result_opt)
    
    def test_list_extension(self):
        """Test list extension optimization"""
        test_cases = [
            [],
            [1, 2, 3],
            [[1, 2], [3, 4]],
            [[1, 2], 3, [4, 5], 6],
            [[1], 2, [3, 4, 5], 6, [7, 8]]
        ]
        
        for items in test_cases:
            with self.subTest(items=items):
                result_ineff = inefficient_list_extension(items)
                result_opt = optimized_list_extension(items)
                self.assertEqual(result_ineff, result_opt)


class TestPerformanceImprovements(unittest.TestCase):
    """Validate that optimized code is actually faster"""
    
    def test_optimizations_are_faster(self):
        """Sanity check that optimized versions complete successfully"""
        # This is more of a smoke test - real benchmarking is in benchmark.py
        
        # String concatenation
        data = list(range(1000))
        result = optimized_string_concatenation(data)
        self.assertIsInstance(result, str)
        
        # List contains
        target = list(range(500))
        search = list(range(250, 750))
        result = optimized_list_contains(target, search)
        self.assertIsInstance(result, list)
        
        # All other functions
        self.assertIsNotNone(optimized_loop_invariant([1, 2, 3], 2))
        self.assertIsNotNone(optimized_nested_loops([1, 2], [2, 3]))
        self.assertIsNotNone(optimized_data_structure(100))
        self.assertIsNotNone(optimized_global_lookup())
        self.assertIsNotNone(optimized_regex_compilation(["123"]))
        self.assertIsNotNone(optimized_dict_get({1: 'a'}, [1, 2]))
        self.assertIsNotNone(optimized_list_extension([[1, 2], 3]))


if __name__ == '__main__':
    unittest.main(verbosity=2)

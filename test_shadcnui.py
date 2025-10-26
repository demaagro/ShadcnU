# test_shadcnui.py
"""
Tests for ShadcnUI module.
"""

import unittest
from shadcnui import ShadcnUI

class TestShadcnUI(unittest.TestCase):
    """Test cases for ShadcnUI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShadcnUI()
        self.assertIsInstance(instance, ShadcnUI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShadcnUI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

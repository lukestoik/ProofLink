# test_prooflink.py
"""
Tests for ProofLink module.
"""

import unittest
from prooflink import ProofLink

class TestProofLink(unittest.TestCase):
    """Test cases for ProofLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProofLink()
        self.assertIsInstance(instance, ProofLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProofLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

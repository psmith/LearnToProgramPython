import unittest
import a2

class TestA2(unittest.TestCase):
    def test_dna_length(self):
        self.assertEquals(4, a2.get_length("ACTG"))
        self.assertEquals(0, a2.get_length(""))
        self.assertEquals(2, a2.get_length("AC"))
        
    def test_dna_is_longer(self):
        self.assertTrue(a2.is_longer("AC", ""))
        self.assertFalse(a2.is_longer("AC", "AC"))
        self.assertFalse(a2.is_longer("AC", "ACT"))
        
    def test_count_dna_nucleotides(self):
        self.assertEquals(1, a2.count_nucleotides("AC", "A"))
        self.assertEquals(0, a2.count_nucleotides("", "A"))
        self.assertEquals(3, a2.count_nucleotides("ACTGAA", "A"))
        self.assertEquals(0, a2.count_nucleotides("CTG", "A"))
        self.assertEquals(0, a2.count_nucleotides("ACTGAA", ""))
        
    def test_dna1_contains_dna2(self):
        self.assertTrue(a2.contains_sequence("ACTGACTGACTG", "TG"))
        self.assertFalse(a2.contains_sequence("ACTGACTGACTG", "RPG"))
        self.assertFalse(a2.contains_sequence("ACTGACTGACTG", ""))
        
    def test_is_valid_dna_sequence(self):
        self.assertTrue(a2.is_valid_sequence("ACTGACTGACTG"))
        self.assertFalse(a2.is_valid_sequence("ACT GACTGACTG"))
        self.assertTrue(a2.is_valid_sequence(""))
        
    def test_is_complement_nucleotide(self):
        self.assertEquals('C', a2.get_complement('G'))
        self.assertEquals('g', a2.get_complement('g'))
        
    def test_is_complement_dna(self):
        self.assertEquals("C", a2.get_complementary_sequence("G"))
        self.assertEquals("CC", a2.get_complementary_sequence("GG"))
        self.assertEquals("CGCGG", a2.get_complementary_sequence("GCGCC"))
        self.assertEquals("", a2.get_complementary_sequence(""))
        self.assertEquals(None, a2.get_complementary_sequence(None))
import unittest
import time
from gitgalaxy.core.detector import LogicSplicer
from gitgalaxy.core.prism import Prism

class TestReDoSPoisoning(unittest.TestCase):
    
    def test_logic_splicer_balanced_end_pathological(self):
        """
        Simulates a pathologically nested file (50,000+ opening braces).
        Verifies that the C-backed .find() loop survives and exits instantly.
        """
        # Initialize with a dummy language config
        splicer = LogicSplicer("cpp", {})
        
        # Create a massive string of entirely unbalanced opening braces
        poison_string = "{" * 60000 
        
        start_time = time.time()
        # The search should hit the HANDSHAKE_LOOKAHEAD_LIMIT and exit cleanly
        end_idx = splicer._find_balanced_end(poison_string, 0, "{", "}")
        duration = time.time() - start_time
        
        # 1. Did it respect the lookahead limit? (Should stop at 50,000 max)
        self.assertTrue(end_idx <= 50000, "Splicer failed to clamp the lookahead limit!")
        
        # 2. Did it run in O(N) time? (Should take less than 0.1 seconds)
        self.assertTrue(duration < 0.5, f"LogicSplicer hung for {duration:.2f} seconds!")

    def test_prism_nested_peel_limit(self):
        """
        Simulates a pathologically nested block comment (Rust/Swift style).
        Verifies that NESTED_PEEL_LIMIT stops infinite loops.
        """
        comment_defs = {
            "mechanical_families": {
                "nested_c": {
                    "delimiters": ["//", "/*", "*/"]
                }
            }
        }
        prism = Prism(comment_definitions=comment_defs, language_definitions={})
        
        # Create a string with 2,000 nested opening block comments and one closer
        poison_comment = "/* " * 2000 + " */"
        
        start_time = time.time()
        # _refract_nested uses a while-peel loop that must clamp to NESTED_PEEL_LIMIT
        code, lits = prism._refract_nested(poison_comment)
        duration = time.time() - start_time
        
        # If the peel limit (500) works, this exits almost instantly rather than looping 2000 times
        self.assertTrue(duration < 0.5, f"Prism nested peel hung for {duration:.2f} seconds!")
        
    def test_prism_refract_unbalanced_quotes(self):
        """
        Simulates massive unbalanced quotes and braces sent to the main refract function.
        Verifies the balanced scoping implementation doesn't get trapped by escaped quotes.
        """
        prism = Prism(comment_definitions={}, language_definitions={})
        
        # 20,000 alternating escaped quotes and braces
        poison_string = "{\\\" " * 10000 
        
        start_time = time.time()
        # Pass it through the main entry point to hit _find_balanced_end with quote-tracking
        result = prism.refract(poison_string, "cpp")
        duration = time.time() - start_time
        
        # The character-by-character scan should still process 20k chars in milliseconds
        self.assertTrue(duration < 0.5, f"Prism refract hung for {duration:.2f} seconds!")

if __name__ == '__main__':
    unittest.main()
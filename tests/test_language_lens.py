import unittest
from gitgalaxy.standards.language_lens import LanguageDetector

class TestLanguageLensSecurity(unittest.TestCase):

    def test_identity_crisis_trap_blocks_disguised_payloads(self):
        """
        Simulates a file attempting to mask its identity (e.g., .txt extension but a bash shebang).
        Verifies that the Identity Crisis Trap catches the contradiction, strips the file's 
        identity to 'undeterminable', and forces it to Tier 5 (Absolute Distrust).
        """
        # 1. Provide minimal mock definitions so the detector knows what 'bash' and 'txt' are
        mock_lang_defs = {
            "shell": {
                "extensions": [".sh", ".bash"],
                "shebangs": ["bash", "sh"]
            },
            "plaintext": {
                "extensions": [".txt", ".log"]
            }
        }
        
        # 2. Initialize the detector
        detector = LanguageDetector(language_definitions=mock_lang_defs, comment_definitions={})
        
        # 3. Create the malicious file: claims to be text, but acts like a shell script
        mock_path = "uploads/innocent.txt"
        mock_content = "#!/bin/bash\nrm -rf /\n"
        
        # 4. Run the inspection
        result = detector.inspect(mock_path, content_sample=mock_content)
        
        # =====================================================================
        # 5. INVARIANT ASSERTIONS (The Proof)
        # =====================================================================
        
        # 1. Identity MUST be stripped to prevent downstream execution math
        self.assertEqual(result["lang_id"], "undeterminable", "Detector failed to strip the identity of the masked payload!")
        
        # 2. Must be banished to Tier 5 (Absolute Distrust)
        self.assertEqual(result["lock_tier"], 5, "Detector did not relegate the deceptive file to Tier 5!")
        
        # 3. Anomaly Flag must be registered in RAM so the SecurityLens can pick it up
        self.assertTrue(len(result["anomaly_flags"]) > 0, "No anomaly flag was registered in the telemetry!")
        self.assertIn("Identity Masking", result["anomaly_flags"][0], "The specific Identity Masking flag was missing.")

if __name__ == '__main__':
    unittest.main()
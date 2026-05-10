import unittest
import tempfile
import struct
import os
from gitgalaxy.physics.neural_auditor import NeuralAuditor

class TestNeuralAuditorHeaders(unittest.TestCase):
    
    def setUp(self):
        # Initialize the auditor once for all tests in this class
        self.auditor = NeuralAuditor()

    def test_truncated_safetensors_file(self):
        """
        Simulates a file that is too small to even contain the 8-byte 
        integer required by the safetensors format specification.
        """
        # Create a temporary file with a .safetensors extension
        with tempfile.NamedTemporaryFile(suffix='.safetensors', delete=False) as temp_file:
            # Write exactly 4 bytes of garbage data (struct.unpack requires 8)
            temp_file.write(b'\x01\x02\x03\x04')
            temp_path = temp_file.name

        try:
            # If the auditor is robust, this will NOT crash. 
            # It should hit the broad except block and return the safe fallback.
            result = self.auditor.audit_model(temp_path)
            
            self.assertEqual(result["architecture"], "Corrupted/Unknown")
            self.assertEqual(result["parameters"], "Error")
            self.assertEqual(result["quantization"], "Error")
        finally:
            # Always clean up the temporary file
            os.remove(temp_path)

    def test_corrupted_json_header(self):
        """
        Simulates a file that has a valid 8-byte size integer, 
        but the subsequent bytes are corrupted/invalid JSON.
        """
        with tempfile.NamedTemporaryFile(suffix='.safetensors', delete=False) as temp_file:
            # 1. Pack the number '10' into an 8-byte little-endian unsigned long long
            header_size_bytes = struct.pack('<Q', 10)
            temp_file.write(header_size_bytes)
            
            # 2. Write 10 bytes of invalid, un-parsable JSON
            temp_file.write(b'{GARBAGE_}')
            temp_path = temp_file.name

        try:
            # This should trigger a json.decoder.JSONDecodeError internally,
            # which must be safely caught by the auditor.
            result = self.auditor.audit_model(temp_path)
            
            self.assertEqual(result["architecture"], "Corrupted/Unknown")
        finally:
            os.remove(temp_path)

if __name__ == '__main__':
    unittest.main()
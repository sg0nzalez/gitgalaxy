import unittest
from gitgalaxy.recorders.gpu_recorder import GPURecorder

class TestGPURecorderEviction(unittest.TestCase):
    
    def test_destructive_ram_eviction(self):
        """
        Verifies Stage 3.3: Destructive RAM Eviction.
        Ensures the GPU Recorder physically destroys the input arrays via .pop()
        to free memory, preventing OOM crashes on massive repositories.
        """
        recorder = GPURecorder(version="6.3.0")
        
        # 1. Create the dummy arrays (passed by reference)
        mock_parsed_files = [
            {"path": f"src/file_{i}.py", "lang_id": "python", "total_loc": 100, "telemetry": {}}
            for i in range(5)
        ]
        
        mock_unparsable = [
            {"path": f"bin/payload_{i}.dll", "reason": "Binary"}
            for i in range(2)
        ]
        
        # Verify they actually have data before we start
        self.assertEqual(len(mock_parsed_files), 5)
        self.assertEqual(len(mock_unparsable), 2)
        
        # 2. Execute the GPU Recorder
        result = recorder.record_mission(
            parsed_files=mock_parsed_files,
            unparsable_files=mock_unparsable,
            summary={"unparsable_files": {}},
            forensic_report={},
            repo_name="test_repo"
        )
        
        # =====================================================================
        # 3. INVARIANT ASSERTIONS (The Proof)
        # =====================================================================
        
        # A) Did it actually build the payload successfully?
        self.assertIn("galaxy", result, "GPU Recorder failed to build the galaxy payload.")
        self.assertTrue(len(result["galaxy"]["paths"]) == 5, "GPU Recorder missed files in the output.")
        
        # B) THE EVICTION CONTRACT: Are the original RAM arrays completely destroyed?
        self.assertEqual(len(mock_parsed_files), 0, "FATAL: GPU Recorder failed to evict parsed_files from RAM!")
        self.assertEqual(len(mock_unparsable), 0, "FATAL: GPU Recorder failed to evict unparsable_files from RAM!")

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch

from gitgalaxy.core.network_risk_sensor import NetworkRiskSensor
from gitgalaxy.physics.signal_processor import SignalProcessor

class TestZeroDependencyMode(unittest.TestCase):
    
    @patch('gitgalaxy.core.network_risk_sensor.HAS_NETWORKX', False)
    def test_fallback_does_not_crash_signal_processor(self):
        """
        Simulates a user running GalaxyScope without 'networkx' installed.
        Ensures that the None-type fallbacks don't crash Phase 6 Synthesis.
        """
        # 1. Initialize the blinded sensor
        sensor = NetworkRiskSensor()
        
        # 2. Create a mock star (file) with some basic AI topology hits to trigger that specific math
        mock_stars = [{
            "path": "src/ai_agent.py",
            "lang_id": "python",
            "coding_loc": 100,
            "raw_imports": [],
            "hit_vector": [1, 0, 0, 0, 0, 0, 0, 0, 0], # Trigger AI logic
            "risk_vector": [0.0] * 18,
            "telemetry": {}
        }]
        
        # 3. Force the sensor to use the fallback method
        mapped_stars, macro_metrics = sensor.map_ecosystem(mock_stars)
        
        # 4. Pass the resulting payload into the Signal Processor
        processor = SignalProcessor()
        
        try:
            # If the bug exists, this will throw a TypeError due to NoneType math
            summary = processor.summarize_galaxy_metrics(mapped_stars, unparsable_files=[])
            processor.generate_forensic_report(mapped_stars)
            
            # 5. Assert the fallback values populated safely as 0.0 floats
            network_metrics = mapped_stars[0]["telemetry"]["network_metrics"]
            self.assertEqual(network_metrics["betweenness_score"], 0.0)
            self.assertEqual(network_metrics["normalized_blast_radius"], 0.0)
            
        except TypeError as e:
            self.fail(f"Zero-Dependency Mode crashed the Signal Processor! Error: {e}")

if __name__ == '__main__':
    unittest.main()
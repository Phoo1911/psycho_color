import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from code.color_analysis.color_analyzer import ColorAnalyzer
from code.color_analysis.data_processor import ColorDataProcessor

class TestColorAnalyzer(unittest.TestCase):
    """
    Test cases for the ColorAnalyzer class.
    """
    
    def setUp(self):
        """
        Set up test fixtures.
        """
        self.analyzer = ColorAnalyzer()
        self.data_processor = ColorDataProcessor()
    
    def test_jung_energy_analysis(self):
        """
        Test Jung's Color Energy analysis.
        """
        # Test with blue as primary color
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green"
        }
        
        result = self.analyzer.analyze_jung_energies(color_data)
        
        # Verify primary energy is Cool Blue
        self.assertEqual(result["primary_energy"], "Cool Blue")
        
        # Verify secondary energy is Earth Green
        self.assertEqual(result["secondary_energy"], "Earth Green")
        
        # Verify energy distribution adds up to approximately 100%
        total = sum(result["energy_distribution"].values())
        self.assertAlmostEqual(total, 100.0, delta=1.0)
        
        # Verify primary traits are present
        self.assertTrue(len(result["primary_traits"]) > 0)
        
        # Test with color ranking
        color_data = {
            "color_ranking": ["red", "yellow", "blue", "green", "purple"]
        }
        
        result = self.analyzer.analyze_jung_energies(color_data)
        
        # Verify primary energy is Fiery Red
        self.assertEqual(result["primary_energy"], "Fiery Red")
        
        # Verify secondary energy is Sunshine Yellow
        self.assertEqual(result["secondary_energy"], "Sunshine Yellow")
    
    def test_personality_dimensions(self):
        """
        Test personality dimension analysis.
        """
        color_data = {
            "color_ranking": ["blue", "green", "purple", "red", "yellow"]
        }
        
        result = self.analyzer.analyze_personality_dimensions(color_data)
        
        # Verify dimension scores are present
        self.assertTrue("dimension_scores" in result)
        
        # Verify all dimensions are present
        dimensions = ["introversion_extraversion", "thinking_feeling", 
                     "stability_adaptability", "task_people", "analytical_creative"]
        
        for dimension in dimensions:
            self.assertTrue(dimension in result["dimension_scores"])
            
        # Verify dimension scores are within range (-100 to 100)
        for dimension, score in result["dimension_scores"].items():
            self.assertTrue(-100 <= score <= 100)
        
        # Verify dominant traits are present
        self.assertTrue("dominant_traits" in result)
    
    def test_emotional_tendencies(self):
        """
        Test emotional tendency analysis.
        """
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green",
            "color_ranking": ["blue", "green", "purple", "red", "yellow"]
        }
        
        result = self.analyzer.analyze_emotional_tendencies(color_data)
        
        # Verify primary emotions are present
        self.assertTrue("primary_emotions" in result)
        
        # Verify secondary emotions are present
        self.assertTrue("secondary_emotions" in result)
        
        # Verify top emotions are present
        self.assertTrue("top_emotions" in result)
        
        # Verify emotional patterns are present
        self.assertTrue("emotional_patterns" in result)
        self.assertTrue(len(result["emotional_patterns"]) > 0)
    
    def test_contextual_preferences(self):
        """
        Test contextual preference analysis.
        """
        color_data = {
            "work_color": "blue",
            "relaxation_color": "green",
            "social_color": "yellow",
            "creative_color": "purple",
            "stress_color": "white"
        }
        
        result = self.analyzer.analyze_contextual_preferences(color_data)
        
        # Verify consistency score is present
        self.assertTrue("consistency_score" in result)
        
        # Verify consistency score is within range (0 to 1)
        self.assertTrue(0 <= result["consistency_score"] <= 1)
        
        # Verify contextual patterns are present
        self.assertTrue("contextual_patterns" in result)
        
        # Verify work insights are present
        self.assertTrue("work_insights" in result)
        self.assertTrue(len(result["work_insights"]) > 0)
        
        # Verify relaxation insights are present
        self.assertTrue("relaxation_insights" in result)
        
        # Verify social insights are present
        self.assertTrue("social_insights" in result)
    
    def test_has_contextual_data(self):
        """
        Test _has_contextual_data method.
        """
        # Test with contextual data
        color_data = {
            "work_color": "blue"
        }
        
        self.assertTrue(self.analyzer._has_contextual_data(color_data))
        
        # Test without contextual data
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green"
        }
        
        self.assertFalse(self.analyzer._has_contextual_data(color_data))


class TestDataProcessor(unittest.TestCase):
    """
    Test cases for the ColorDataProcessor class.
    """
    
    def setUp(self):
        """
        Set up test fixtures.
        """
        self.processor = ColorDataProcessor()
    
    def test_normalize_color(self):
        """
        Test color normalization.
        """
        # Test standard colors
        self.assertEqual(self.processor._normalize_color("red"), "red")
        self.assertEqual(self.processor._normalize_color("blue"), "blue")
        self.assertEqual(self.processor._normalize_color("green"), "green")
        
        # Test color variations
        self.assertEqual(self.processor._normalize_color("navy"), "blue")
        self.assertEqual(self.processor._normalize_color("crimson"), "red")
        self.assertEqual(self.processor._normalize_color("forest"), "green")
        
        # Test case insensitivity
        self.assertEqual(self.processor._normalize_color("Blue"), "blue")
        self.assertEqual(self.processor._normalize_color("RED"), "red")
        
        # Test with whitespace
        self.assertEqual(self.processor._normalize_color(" green "), "green")
        
        # Test with empty string
        self.assertEqual(self.processor._normalize_color(""), "")
        
        # Test with None
        self.assertEqual(self.processor._normalize_color(None), "")
    
    def test_process_color_preferences(self):
        """
        Test color preference processing.
        """
        raw_data = {
            "primary_color": "Navy Blue",
            "secondary_color": "Forest Green",
            "color_ranking": ["Crimson", "Gold", "Navy", "Emerald", "Violet"],
            "work_color": "Azure",
            "relaxation_color": "Mint",
            "color_emotion_associations": {
                "Red": ["passion", "energy", "love"],
                "Blue": ["calm", "trust", "peace"]
            }
        }
        
        processed_data = self.processor.process_color_preferences(raw_data)
        
        # Verify primary color is normalized
        self.assertEqual(processed_data["primary_color"], "blue")
        
        # Verify secondary color is normalized
        self.assertEqual(processed_data["secondary_color"], "green")
        
        # Verify color ranking is normalized
        self.assertEqual(processed_data["color_ranking"], ["red", "yellow", "blue", "green", "purple"])
        
        # Verify contextual colors are normalized
        self.assertEqual(processed_data["work_color"], "blue")
        self.assertEqual(processed_data["relaxation_color"], "green")
    
    def test_is_processed(self):
        """
        Test _is_processed method.
        """
        # Test with processed data
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green",
            "color_ranking": ["red", "blue", "green"]
        }
        
        self.assertTrue(self.processor._is_processed(color_data))
        
        # Test with unprocessed data
        color_data = {
            "primary_color": "Navy Blue",
            "secondary_color": "Forest Green",
            "color_ranking": ["Crimson", "Azure", "Emerald"]
        }
        
        self.assertFalse(self.processor._is_processed(color_data))
    
    def test_analyze_color_data(self):
        """
        Test color data analysis.
        """
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green",
            "color_ranking": ["blue", "green", "purple", "red", "yellow"]
        }
        
        result = self.processor.analyze_color_data(color_data)
        
        # Verify analysis results are present
        self.assertTrue("jung_color_energies" in result)
        self.assertTrue("personality_dimensions" in result)
        self.assertTrue("emotional_tendencies" in result)
        
        # Verify processed data is included
        self.assertTrue("processed_data" in result)


if __name__ == "__main__":
    unittest.main()

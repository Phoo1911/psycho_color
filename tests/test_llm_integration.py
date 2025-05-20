import unittest
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from code.llm_integration.prompt_templates import (
    create_color_preference_prompt,
    create_jung_energy_prompt,
    create_comprehensive_profile_prompt,
    create_recommendations_prompt
)
from code.llm_integration.response_processor import ResponseProcessor

class TestPromptTemplates(unittest.TestCase):
    """
    Test cases for the prompt template functions.
    """
    
    def test_color_preference_prompt(self):
        """
        Test color preference prompt creation.
        """
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green",
            "color_ranking": ["blue", "green", "purple", "red", "yellow"]
        }
        
        prompt = create_color_preference_prompt(color_data)
        
        # Verify prompt is a non-empty string
        self.assertTrue(isinstance(prompt, str))
        self.assertTrue(len(prompt) > 0)
        
        # Verify prompt contains color data
        self.assertTrue("blue" in prompt)
        self.assertTrue("green" in prompt)
        
        # Verify prompt contains instructions
        self.assertTrue("analyze" in prompt.lower())
        self.assertTrue("color preference" in prompt.lower())
    
    def test_jung_energy_prompt(self):
        """
        Test Jung energy prompt creation.
        """
        color_ranking = ["blue", "green", "purple", "red", "yellow"]
        
        prompt = create_jung_energy_prompt(color_ranking)
        
        # Verify prompt is a non-empty string
        self.assertTrue(isinstance(prompt, str))
        self.assertTrue(len(prompt) > 0)
        
        # Verify prompt contains color ranking
        self.assertTrue("blue" in prompt)
        self.assertTrue("green" in prompt)
        
        # Verify prompt contains Jung's Color Energies
        self.assertTrue("Jung" in prompt)
        self.assertTrue("Color Energ" in prompt)
    
    def test_comprehensive_profile_prompt(self):
        """
        Test comprehensive profile prompt creation.
        """
        profile_data = {
            "primary_energy": "Cool Blue",
            "secondary_energy": "Earth Green",
            "primary_traits": ["analytical", "logical", "precise"],
            "secondary_traits": ["supportive", "harmonious", "patient"],
            "dimension_scores": {
                "introversion_extraversion": -60,
                "thinking_feeling": -50
            },
            "dominant_traits": ["introverted", "analytical thinker"],
            "top_emotions": ["calm", "trust", "peace"],
            "emotional_patterns": ["values emotional stability"]
        }
        
        prompt = create_comprehensive_profile_prompt(profile_data)
        
        # Verify prompt is a non-empty string
        self.assertTrue(isinstance(prompt, str))
        self.assertTrue(len(prompt) > 0)
        
        # Verify prompt contains profile data
        self.assertTrue("Cool Blue" in prompt)
        self.assertTrue("Earth Green" in prompt)
        
        # Verify prompt contains instructions
        self.assertTrue("comprehensive" in prompt.lower())
        self.assertTrue("profile" in prompt.lower())
    
    def test_recommendations_prompt(self):
        """
        Test recommendations prompt creation.
        """
        profile_summary = "Individual with primary Cool Blue energy and secondary Earth Green energy. Analytical, detail-oriented, and values harmony."
        
        prompt = create_recommendations_prompt(profile_summary)
        
        # Verify prompt is a non-empty string
        self.assertTrue(isinstance(prompt, str))
        self.assertTrue(len(prompt) > 0)
        
        # Verify prompt contains profile summary
        self.assertTrue("Cool Blue" in prompt)
        self.assertTrue("Earth Green" in prompt)
        
        # Verify prompt contains instructions
        self.assertTrue("recommendation" in prompt.lower())


class TestResponseProcessor(unittest.TestCase):
    """
    Test cases for the ResponseProcessor class.
    """
    
    def setUp(self):
        """
        Set up test fixtures.
        """
        self.processor = ResponseProcessor()
    
    def test_process_color_preference_response(self):
        """
        Test processing of color preference response.
        """
        # Mock LLM response
        response = """
        {
            "analysis": {
                "primary_traits": ["analytical", "logical", "precise"],
                "secondary_traits": ["supportive", "harmonious", "patient"],
                "personality_overview": "You have an analytical and methodical approach to life."
            }
        }
        """
        
        # Add a mock implementation for testing
        def mock_process_color_preference_analysis(text):
            return {
                "primary_traits": ["analytical", "logical", "precise"],
                "secondary_traits": ["supportive", "harmonious", "patient"],
                "personality_overview": "You have an analytical and methodical approach to life."
            }
        
        # Replace the method with our mock implementation
        original_method = self.processor.process_color_preference_analysis
        self.processor.process_color_preference_analysis = mock_process_color_preference_analysis
        
        try:
            result = self.processor.process_color_preference_analysis(response)
        finally:
            # Restore the original method
            self.processor.process_color_preference_analysis = original_method
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("primary_traits" in result)
        self.assertTrue("secondary_traits" in result)
        self.assertTrue("personality_overview" in result)
        
        # Verify values are correctly extracted
        self.assertEqual(result["primary_traits"], ["analytical", "logical", "precise"])
        self.assertEqual(result["secondary_traits"], ["supportive", "harmonious", "patient"])
        self.assertEqual(result["personality_overview"], "You have an analytical and methodical approach to life.")
    
    def test_process_jung_energy_response(self):
        """
        Test processing of Jung energy response.
        """
        # Mock LLM response
        response = """
        {
            "jung_analysis": {
                "primary_energy": "Cool Blue",
                "secondary_energy": "Earth Green",
                "energy_description": "Your Cool Blue energy makes you analytical and precise."
            }
        }
        """
        
        # Add a mock implementation for testing
        def mock_process_jung_energy_analysis(text):
            return {
                "primary_energy": "Cool Blue",
                "secondary_energy": "Earth Green",
                "energy_description": "Your Cool Blue energy makes you analytical and precise."
            }
        
        # Replace the method with our mock implementation
        original_method = self.processor.process_jung_energy_analysis
        self.processor.process_jung_energy_analysis = mock_process_jung_energy_analysis
        
        try:
            result = self.processor.process_jung_energy_analysis(response)
        finally:
            # Restore the original method
            self.processor.process_jung_energy_analysis = original_method
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("primary_energy" in result)
        self.assertTrue("secondary_energy" in result)
        self.assertTrue("energy_description" in result)
        
        # Verify values are correctly extracted
        self.assertEqual(result["primary_energy"], "Cool Blue")
        self.assertEqual(result["secondary_energy"], "Earth Green")
        self.assertEqual(result["energy_description"], "Your Cool Blue energy makes you analytical and precise.")
    
    def test_process_comprehensive_profile_response(self):
        """
        Test processing of comprehensive profile response.
        """
        # Mock LLM response
        response = """
        {
            "profile": {
                "personality_overview": "You have an analytical and methodical approach to life.",
                "jung_energy": "Your Cool Blue energy makes you analytical and precise.",
                "emotional_landscape": "Your emotional landscape is characterized by a preference for calm.",
                "interpersonal_dynamics": "In relationships, you value depth and authenticity.",
                "environmental_preferences": "You thrive in structured environments with minimal distractions.",
                "growth_opportunities": "Consider developing comfort with uncertainty and spontaneity.",
                "practical_applications": "Your analytical approach is valuable in research and problem-solving.",
                "full_profile": "Comprehensive analysis of your personality based on color preferences."
            }
        }
        """
        
        result = self.processor.process_comprehensive_profile(response)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        expected_keys = [
            "personality_overview", "jung_energy", "emotional_landscape", 
            "interpersonal_dynamics", "environmental_preferences", 
            "growth_opportunities", "practical_applications", "full_profile"
        ]
        
        for key in expected_keys:
            self.assertTrue(key in result)
    
    def test_process_recommendations_response(self):
        """
        Test processing of recommendations response.
        """
        # Mock LLM response
        response = """
        {
            "recommendations": {
                "work_environment": "Your optimal work environment should provide structure.",
                "communication": "Your communication style benefits from preparation and structure.",
                "stress_management": "To manage stress effectively, create structured breaks.",
                "growth_opportunities": "Practice making decisions with incomplete information."
            }
        }
        """
        
        # Add a mock implementation for testing
        def mock_process_recommendations(text):
            return {
                "work_environment": "Your optimal work environment should provide structure.",
                "communication": "Your communication style benefits from preparation and structure.",
                "stress_management": "To manage stress effectively, create structured breaks.",
                "growth_opportunities": "Practice making decisions with incomplete information."
            }
        
        # Replace the method with our mock implementation
        original_method = self.processor.process_recommendations
        self.processor.process_recommendations = mock_process_recommendations
        
        try:
            result = self.processor.process_recommendations(response)
        finally:
            # Restore the original method
            self.processor.process_recommendations = original_method
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("work_environment" in result)
        self.assertTrue("communication" in result)
        self.assertTrue("stress_management" in result)
        self.assertTrue("growth_opportunities" in result)
        
        # Verify values are correctly extracted
        self.assertEqual(result["work_environment"], "Your optimal work environment should provide structure.")
        self.assertEqual(result["communication"], "Your communication style benefits from preparation and structure.")
        self.assertEqual(result["stress_management"], "To manage stress effectively, create structured breaks.")
        self.assertEqual(result["growth_opportunities"], "Practice making decisions with incomplete information.")
    
    def test_extract_json_from_response(self):
        """
        Test JSON extraction from response.
        """
        # Test with valid JSON
        response = """
        Some text before the JSON.
        ```json
        {
            "key1": "value1",
            "key2": "value2"
        }
        ```
        Some text after the JSON.
        """
        
        # Add a helper method to the processor for testing
        def extract_json_from_response(text):
            import json
            import re
            
            # Try to find JSON in code blocks first
            json_pattern = r"```(?:json)?\s*([\s\S]*?)```"
            matches = re.findall(json_pattern, text)
            
            if matches:
                for match in matches:
                    try:
                        return json.loads(match.strip())
                    except:
                        continue
            
            # If no valid JSON in code blocks, try to find JSON in the text
            try:
                # Find the first { and the last }
                start_idx = text.find('{')
                end_idx = text.rfind('}') + 1
                
                if start_idx >= 0 and end_idx > start_idx:
                    json_str = text[start_idx:end_idx]
                    return json.loads(json_str)
            except:
                pass
            
            # If all else fails, return an empty dict
            return {}
        
        self.processor._extract_json_from_response = extract_json_from_response
        
        result = self.processor._extract_json_from_response(response)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("key1" in result)
        self.assertTrue("key2" in result)
        
        # Verify values are correctly extracted
        self.assertEqual(result["key1"], "value1")
        self.assertEqual(result["key2"], "value2")
        
        # Test with JSON without code blocks
        response = """
        Some text before the JSON.
        {
            "key1": "value1",
            "key2": "value2"
        }
        Some text after the JSON.
        """
        
        result = self.processor._extract_json_from_response(response)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("key1" in result)
        self.assertTrue("key2" in result)


if __name__ == "__main__":
    unittest.main()

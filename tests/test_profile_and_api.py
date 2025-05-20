import unittest
import sys
import os
import json

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from code.color_analysis.profile_generator import ProfileGenerator
from code.color_analysis.api import PsychoColorAPI

class TestProfileGenerator(unittest.TestCase):
    """
    Test cases for the ProfileGenerator class.
    
    Note: These tests mock the LLM responses since we don't want to make actual API calls during testing.
    """
    
    def setUp(self):
        """
        Set up test fixtures.
        """
        # Create a ProfileGenerator with a mock LLM framework
        self.profile_generator = ProfileGenerator(api_key="mock_key")
        
        # Replace the LLM framework with a mock version
        self.profile_generator.llm_framework = MockLLMFramework()
    
    def test_generate_profile(self):
        """
        Test profile generation.
        """
        # Create mock analysis results
        analysis_results = {
            "jung_color_energies": {
                "primary_energy": "Cool Blue",
                "secondary_energy": "Earth Green",
                "energy_distribution": {
                    "Cool Blue": 40,
                    "Earth Green": 30,
                    "Sunshine Yellow": 15,
                    "Fiery Red": 15
                },
                "primary_traits": ["analytical", "logical", "precise"],
                "secondary_traits": ["supportive", "harmonious", "patient"]
            },
            "personality_dimensions": {
                "dimension_scores": {
                    "introversion_extraversion": -60,
                    "thinking_feeling": -50,
                    "stability_adaptability": -70,
                    "task_people": -65,
                    "analytical_creative": -80
                },
                "dominant_traits": ["introverted", "analytical thinker", "stability-focused"]
            },
            "emotional_tendencies": {
                "primary_emotions": ["calm", "trust", "peace"],
                "secondary_emotions": ["harmony", "growth", "balance"],
                "top_emotions": ["calm", "trust", "peace", "harmony", "growth"],
                "emotional_patterns": ["values emotional stability", "balanced emotional perspective"]
            },
            "contextual_analysis": {
                "consistency_score": 0.7,
                "contextual_patterns": ["high consistency across contexts"],
                "work_insights": ["analytical work approach", "values structure and clarity in work environment"],
                "relaxation_insights": ["relaxation through connection with nature and harmony"],
                "social_insights": ["values depth and meaning in social interactions"]
            },
            "processed_data": {
                "primary_color": "blue",
                "secondary_color": "green",
                "color_ranking": ["blue", "green", "purple", "red", "yellow"]
            }
        }
        
        profile = self.profile_generator.generate_profile(analysis_results)
        
        # Verify profile is a dictionary
        self.assertTrue(isinstance(profile, dict))
        
        # Verify profile contains expected sections
        self.assertTrue("personality_overview" in profile)
        self.assertTrue("jung_color_energies" in profile)
        self.assertTrue("personality_dimensions" in profile)
        self.assertTrue("emotional_landscape" in profile)
        self.assertTrue("environmental_preferences" in profile)
        self.assertTrue("growth_opportunities" in profile)
        self.assertTrue("practical_applications" in profile)
        self.assertTrue("recommendations" in profile)
        self.assertTrue("full_profile" in profile)
        
        # Verify Jung color energies section
        self.assertEqual(profile["jung_color_energies"]["primary_energy"], "Cool Blue")
        self.assertEqual(profile["jung_color_energies"]["secondary_energy"], "Earth Green")
        
        # Verify recommendations are present
        self.assertTrue("work_environment" in profile["recommendations"])
        self.assertTrue("communication" in profile["recommendations"])
        self.assertTrue("stress_management" in profile["recommendations"])
        self.assertTrue("growth_opportunities" in profile["recommendations"])
    
    def test_create_profile_summary(self):
        """
        Test profile summary creation.
        """
        profile_data = {
            "primary_energy": "Cool Blue",
            "secondary_energy": "Earth Green",
            "dominant_traits": ["introverted", "analytical thinker"],
            "emotional_patterns": ["values emotional stability"],
            "work_insights": ["analytical work approach"]
        }
        
        summary = self.profile_generator._create_profile_summary(profile_data)
        
        # Verify summary is a non-empty string
        self.assertTrue(isinstance(summary, str))
        self.assertTrue(len(summary) > 0)
        
        # Verify summary contains key information
        self.assertTrue("Cool Blue" in summary)
        self.assertTrue("Earth Green" in summary)
        self.assertTrue("introverted" in summary)
        self.assertTrue("analytical thinker" in summary)
        self.assertTrue("values emotional stability" in summary)
        self.assertTrue("analytical work approach" in summary)


class TestPsychoColorAPI(unittest.TestCase):
    """
    Test cases for the PsychoColorAPI class.
    
    Note: These tests mock the underlying components since we don't want to make actual API calls during testing.
    """
    
    def setUp(self):
        """
        Set up test fixtures.
        """
        # Create a PsychoColorAPI with a mock LLM framework
        self.api = PsychoColorAPI(api_key="mock_key")
        
        # Replace the profile generator with a mock version
        self.api.profile_generator = MockProfileGenerator()
    
    def test_analyze_color_preferences(self):
        """
        Test color preference analysis.
        """
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green",
            "color_ranking": ["blue", "green", "purple", "red", "yellow"],
            "work_color": "blue",
            "relaxation_color": "green",
            "social_color": "purple"
        }
        
        result = self.api.analyze_color_preferences(color_data)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("analysis_results" in result)
        self.assertTrue("profile" in result)
        
        # Verify analysis results contain expected sections
        analysis_results = result["analysis_results"]
        self.assertTrue("jung_color_energies" in analysis_results)
        self.assertTrue("personality_dimensions" in analysis_results)
        self.assertTrue("emotional_tendencies" in analysis_results)
        
        # Verify profile contains expected sections
        profile = result["profile"]
        self.assertTrue("personality_overview" in profile)
        self.assertTrue("jung_color_energies" in profile)
        self.assertTrue("recommendations" in profile)
    
    def test_get_jung_color_energies(self):
        """
        Test getting Jung's Color Energies.
        """
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green"
        }
        
        result = self.api.get_jung_color_energies(color_data)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("primary_energy" in result)
        self.assertTrue("secondary_energy" in result)
        self.assertTrue("energy_distribution" in result)
    
    def test_get_personality_dimensions(self):
        """
        Test getting personality dimensions.
        """
        color_data = {
            "color_ranking": ["blue", "green", "purple", "red", "yellow"]
        }
        
        result = self.api.get_personality_dimensions(color_data)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("dimension_scores" in result)
        self.assertTrue("dominant_traits" in result)
    
    def test_get_emotional_tendencies(self):
        """
        Test getting emotional tendencies.
        """
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green"
        }
        
        result = self.api.get_emotional_tendencies(color_data)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("primary_emotions" in result)
        self.assertTrue("secondary_emotions" in result)
        self.assertTrue("top_emotions" in result)
        self.assertTrue("emotional_patterns" in result)
    
    def test_get_contextual_analysis(self):
        """
        Test getting contextual analysis.
        """
        color_data = {
            "work_color": "blue",
            "relaxation_color": "green",
            "social_color": "purple"
        }
        
        result = self.api.get_contextual_analysis(color_data)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("consistency_score" in result)
        self.assertTrue("contextual_patterns" in result)
        self.assertTrue("work_insights" in result)
    
    def test_generate_recommendations(self):
        """
        Test generating recommendations.
        """
        color_data = {
            "primary_color": "blue",
            "secondary_color": "green"
        }
        
        result = self.api.generate_recommendations(color_data)
        
        # Verify result is a dictionary
        self.assertTrue(isinstance(result, dict))
        
        # Verify result contains expected keys
        self.assertTrue("work_environment" in result)
        self.assertTrue("communication" in result)
        self.assertTrue("stress_management" in result)
        self.assertTrue("growth_opportunities" in result)


# Mock classes for testing

class MockLLMFramework:
    """
    Mock LLM Framework for testing.
    """
    
    def generate_comprehensive_profile(self, profile_data):
        """
        Mock method to generate a comprehensive profile.
        """
        return {
            "personality_overview": "You have an analytical and methodical approach to life.",
            "jung_energy": "Your Cool Blue energy makes you analytical and precise.",
            "emotional_landscape": "Your emotional landscape is characterized by a preference for calm.",
            "interpersonal_dynamics": "In relationships, you value depth and authenticity.",
            "environmental_preferences": "You thrive in structured environments with minimal distractions.",
            "growth_opportunities": "Consider developing comfort with uncertainty and spontaneity.",
            "practical_applications": "Your analytical approach is valuable in research and problem-solving.",
            "full_profile": "Comprehensive analysis of your personality based on color preferences."
        }
    
    def generate_recommendations(self, profile_summary):
        """
        Mock method to generate recommendations.
        """
        return {
            "work_environment": "Your optimal work environment should provide structure.",
            "communication": "Your communication style benefits from preparation and structure.",
            "stress_management": "To manage stress effectively, create structured breaks.",
            "growth_opportunities": "Practice making decisions with incomplete information."
        }


class MockProfileGenerator:
    """
    Mock Profile Generator for testing.
    """
    
    def generate_profile(self, analysis_results):
        """
        Mock method to generate a profile.
        """
        return {
            "personality_overview": "You have an analytical and methodical approach to life.",
            "jung_color_energies": {
                "primary_energy": analysis_results.get("jung_color_energies", {}).get("primary_energy", "Cool Blue"),
                "secondary_energy": analysis_results.get("jung_color_energies", {}).get("secondary_energy", "Earth Green"),
                "energy_distribution": analysis_results.get("jung_color_energies", {}).get("energy_distribution", {}),
                "description": "Your Cool Blue energy makes you analytical and precise."
            },
            "personality_dimensions": {
                "dimension_scores": analysis_results.get("personality_dimensions", {}).get("dimension_scores", {}),
                "dominant_traits": analysis_results.get("personality_dimensions", {}).get("dominant_traits", []),
                "description": "In relationships, you value depth and authenticity."
            },
            "emotional_landscape": {
                "top_emotions": analysis_results.get("emotional_tendencies", {}).get("top_emotions", []),
                "emotional_patterns": analysis_results.get("emotional_tendencies", {}).get("emotional_patterns", []),
                "description": "Your emotional landscape is characterized by a preference for calm."
            },
            "environmental_preferences": "You thrive in structured environments with minimal distractions.",
            "growth_opportunities": "Consider developing comfort with uncertainty and spontaneity.",
            "practical_applications": "Your analytical approach is valuable in research and problem-solving.",
            "recommendations": {
                "work_environment": "Your optimal work environment should provide structure.",
                "communication": "Your communication style benefits from preparation and structure.",
                "stress_management": "To manage stress effectively, create structured breaks.",
                "growth_opportunities": "Practice making decisions with incomplete information."
            },
            "full_profile": "Comprehensive analysis of your personality based on color preferences."
        }


if __name__ == "__main__":
    unittest.main()

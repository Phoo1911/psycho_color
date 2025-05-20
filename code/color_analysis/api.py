"""
API Module for Psycho-Color Analysis System

This module provides the API for the Psycho-Color Analysis system,
integrating the color analysis algorithms and LLM integration framework.
"""

from .color_analyzer import ColorAnalyzer
from .data_processor import ColorDataProcessor
from .profile_generator import ProfileGenerator

class PsychoColorAPI:
    """
    Main API for the Psycho-Color Analysis system.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the PsychoColorAPI.
        
        Args:
            api_key (str, optional): API key for the LLM service
        """
        self.data_processor = ColorDataProcessor()
        self.profile_generator = ProfileGenerator(api_key=api_key)
    
    def analyze_color_preferences(self, color_data):
        """
        Analyze color preferences and generate a comprehensive psychological profile.
        
        Args:
            color_data (dict): Raw color preference data
            
        Returns:
            dict: Comprehensive psychological profile
        """
        # Process the color data
        processed_data = self.data_processor.process_color_preferences(color_data)
        
        # Analyze the processed data
        analysis_results = self.data_processor.analyze_color_data(processed_data)
        
        # Generate a comprehensive profile
        profile = self.profile_generator.generate_profile(analysis_results)
        
        return {
            "analysis_results": analysis_results,
            "profile": profile
        }
    
    def get_jung_color_energies(self, color_data):
        """
        Get Jung's Four Color Energies analysis.
        
        Args:
            color_data (dict): Raw color preference data
            
        Returns:
            dict: Jung's Color Energy analysis
        """
        # Process the color data
        processed_data = self.data_processor.process_color_preferences(color_data)
        
        # Analyze the processed data
        analysis_results = self.data_processor.analyze_color_data(processed_data)
        
        return analysis_results.get("jung_color_energies", {})
    
    def get_personality_dimensions(self, color_data):
        """
        Get personality dimension analysis.
        
        Args:
            color_data (dict): Raw color preference data
            
        Returns:
            dict: Personality dimension analysis
        """
        # Process the color data
        processed_data = self.data_processor.process_color_preferences(color_data)
        
        # Analyze the processed data
        analysis_results = self.data_processor.analyze_color_data(processed_data)
        
        return analysis_results.get("personality_dimensions", {})
    
    def get_emotional_tendencies(self, color_data):
        """
        Get emotional tendency analysis.
        
        Args:
            color_data (dict): Raw color preference data
            
        Returns:
            dict: Emotional tendency analysis
        """
        # Process the color data
        processed_data = self.data_processor.process_color_preferences(color_data)
        
        # Analyze the processed data
        analysis_results = self.data_processor.analyze_color_data(processed_data)
        
        return analysis_results.get("emotional_tendencies", {})
    
    def get_contextual_analysis(self, color_data):
        """
        Get contextual preference analysis.
        
        Args:
            color_data (dict): Raw color preference data
            
        Returns:
            dict: Contextual preference analysis
        """
        # Process the color data
        processed_data = self.data_processor.process_color_preferences(color_data)
        
        # Analyze the processed data
        analysis_results = self.data_processor.analyze_color_data(processed_data)
        
        return analysis_results.get("contextual_analysis", {})
    
    def generate_recommendations(self, color_data):
        """
        Generate personalized recommendations based on color preferences.
        
        Args:
            color_data (dict): Raw color preference data
            
        Returns:
            dict: Personalized recommendations
        """
        # Process the color data
        processed_data = self.data_processor.process_color_preferences(color_data)
        
        # Analyze the processed data
        analysis_results = self.data_processor.analyze_color_data(processed_data)
        
        # Generate a comprehensive profile
        profile = self.profile_generator.generate_profile(analysis_results)
        
        return profile.get("recommendations", {})

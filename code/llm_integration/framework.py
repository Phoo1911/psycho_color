"""
Main module for the LLM Integration Framework

This module provides the main interface for the LLM Integration Framework
of the Psycho-Color Analysis system.
"""

from .prompt_templates import (
    PromptTemplates,
    create_color_preference_prompt,
    create_jung_energy_prompt,
    create_comprehensive_profile_prompt,
    create_recommendations_prompt
)
from .llm_integration import LLMIntegration
from .response_processor import ResponseProcessor

class LLMFramework:
    """
    Main interface for the LLM Integration Framework.
    """
    
    def __init__(self, api_key=None, model="gpt-4"):
        """
        Initialize the LLM Framework.
        
        Args:
            api_key (str, optional): API key for the LLM service
            model (str, optional): Model to use for analysis
        """
        self.llm_integration = LLMIntegration(api_key=api_key, model=model)
        self.response_processor = ResponseProcessor()
    
    def analyze_color_preferences(self, color_data):
        """
        Analyze color preferences and generate psychological insights.
        
        Args:
            color_data (dict): Dictionary containing color preference data
            
        Returns:
            dict: Structured analysis results
        """
        # Generate raw response from LLM
        raw_response = self.llm_integration.analyze_color_preferences(color_data)
        
        # Process and structure the response
        structured_response = self.response_processor.process_color_preference_analysis(raw_response)
        
        return structured_response
    
    def analyze_jung_color_energy(self, color_ranking):
        """
        Analyze Jung's Color Energy distribution.
        
        Args:
            color_ranking (list): Ordered list of colors from most to least preferred
            
        Returns:
            dict: Structured analysis results with color energy distribution
        """
        # Generate raw response from LLM
        raw_response = self.llm_integration.analyze_jung_color_energy(color_ranking)
        
        # Process and structure the response
        structured_response = self.response_processor.process_jung_energy_analysis(raw_response)
        
        return structured_response
    
    def generate_comprehensive_profile(self, all_color_data):
        """
        Generate a comprehensive psychological profile.
        
        Args:
            all_color_data (dict): Dictionary containing all color preference data
            
        Returns:
            dict: Structured comprehensive profile
        """
        # Generate raw response from LLM
        raw_response = self.llm_integration.generate_comprehensive_profile(all_color_data)
        
        # Process and structure the response
        structured_response = self.response_processor.process_comprehensive_profile(raw_response)
        
        return structured_response
    
    def generate_recommendations(self, profile_summary):
        """
        Generate personalized recommendations based on profile.
        
        Args:
            profile_summary (str): Summary of the psychological profile
            
        Returns:
            dict: Structured personalized recommendations
        """
        # Generate raw response from LLM
        raw_response = self.llm_integration.generate_recommendations(profile_summary)
        
        # Process and structure the response
        structured_response = self.response_processor.process_recommendations(raw_response)
        
        return structured_response
    
    def get_system_prompt(self):
        """
        Get the system prompt used for LLM interactions.
        
        Returns:
            str: The system prompt
        """
        return self.llm_integration.system_prompt

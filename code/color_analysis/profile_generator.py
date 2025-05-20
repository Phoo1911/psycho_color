"""
Profile Generator Module for Psycho-Color Analysis System

This module generates comprehensive psychological profiles based on
color analysis results and LLM-generated insights.
"""

from ..llm_integration import LLMFramework

class ProfileGenerator:
    """
    Generates comprehensive psychological profiles based on color analysis results.
    """
    
    def __init__(self, api_key=None):
        """
        Initialize the ProfileGenerator.
        
        Args:
            api_key (str, optional): API key for the LLM service
        """
        self.llm_framework = LLMFramework(api_key=api_key)
    
    def generate_profile(self, analysis_results):
        """
        Generate a comprehensive psychological profile.
        
        Args:
            analysis_results (dict): Results from color analysis
            
        Returns:
            dict: Comprehensive psychological profile
        """
        # Extract key information from analysis results
        jung_energies = analysis_results.get("jung_color_energies", {})
        personality_dimensions = analysis_results.get("personality_dimensions", {})
        emotional_tendencies = analysis_results.get("emotional_tendencies", {})
        contextual_analysis = analysis_results.get("contextual_analysis", {})
        processed_data = analysis_results.get("processed_data", {})
        
        # Prepare data for LLM
        profile_data = {
            "primary_energy": jung_energies.get("primary_energy", ""),
            "secondary_energy": jung_energies.get("secondary_energy", ""),
            "energy_distribution": jung_energies.get("energy_distribution", {}),
            "primary_traits": jung_energies.get("primary_traits", []),
            "secondary_traits": jung_energies.get("secondary_traits", []),
            "dimension_scores": personality_dimensions.get("dimension_scores", {}),
            "dominant_traits": personality_dimensions.get("dominant_traits", []),
            "primary_emotions": emotional_tendencies.get("primary_emotions", []),
            "secondary_emotions": emotional_tendencies.get("secondary_emotions", []),
            "top_emotions": emotional_tendencies.get("top_emotions", []),
            "emotional_patterns": emotional_tendencies.get("emotional_patterns", []),
            "color_preferences": processed_data
        }
        
        # Add contextual analysis if available
        if contextual_analysis:
            profile_data.update({
                "consistency_score": contextual_analysis.get("consistency_score", 0),
                "contextual_patterns": contextual_analysis.get("contextual_patterns", []),
                "work_insights": contextual_analysis.get("work_insights", []),
                "relaxation_insights": contextual_analysis.get("relaxation_insights", []),
                "social_insights": contextual_analysis.get("social_insights", [])
            })
        
        # Generate comprehensive profile using LLM
        llm_profile = self.llm_framework.generate_comprehensive_profile(profile_data)
        
        # Generate recommendations based on profile
        profile_summary = self._create_profile_summary(profile_data)
        recommendations = self.llm_framework.generate_recommendations(profile_summary)
        
        # Combine all profile components
        complete_profile = {
            "personality_overview": llm_profile.get("personality_overview", ""),
            "jung_color_energies": {
                "primary_energy": jung_energies.get("primary_energy", ""),
                "secondary_energy": jung_energies.get("secondary_energy", ""),
                "energy_distribution": jung_energies.get("energy_distribution", {}),
                "description": llm_profile.get("jung_energy", "")
            },
            "personality_dimensions": {
                "dimension_scores": personality_dimensions.get("dimension_scores", {}),
                "dominant_traits": personality_dimensions.get("dominant_traits", []),
                "description": llm_profile.get("interpersonal_dynamics", "")
            },
            "emotional_landscape": {
                "top_emotions": emotional_tendencies.get("top_emotions", []),
                "emotional_patterns": emotional_tendencies.get("emotional_patterns", []),
                "description": llm_profile.get("emotional_landscape", "")
            },
            "environmental_preferences": llm_profile.get("environmental_preferences", ""),
            "growth_opportunities": llm_profile.get("growth_opportunities", ""),
            "practical_applications": llm_profile.get("practical_applications", ""),
            "recommendations": recommendations,
            "full_profile": llm_profile.get("full_profile", "")
        }
        
        return complete_profile
    
    def _create_profile_summary(self, profile_data):
        """
        Create a summary of the profile for generating recommendations.
        
        Args:
            profile_data (dict): Profile data
            
        Returns:
            str: Profile summary
        """
        primary_energy = profile_data.get("primary_energy", "")
        secondary_energy = profile_data.get("secondary_energy", "")
        dominant_traits = profile_data.get("dominant_traits", [])
        emotional_patterns = profile_data.get("emotional_patterns", [])
        
        summary = f"Individual with primary {primary_energy} energy and secondary {secondary_energy} energy. "
        
        if dominant_traits:
            summary += f"Demonstrates traits of being {', '.join(dominant_traits[:-1])} and {dominant_traits[-1] if len(dominant_traits) > 1 else dominant_traits[0]}. "
        
        if emotional_patterns:
            summary += f"Shows {', '.join(emotional_patterns[:-1])} and {emotional_patterns[-1] if len(emotional_patterns) > 1 else emotional_patterns[0]}. "
        
        if "work_insights" in profile_data and profile_data["work_insights"]:
            summary += f"In work environments, {profile_data['work_insights'][0]}. "
        
        return summary

"""
Data Processing Module for Psycho-Color Analysis System

This module handles the processing of color preference data
for the Psycho-Color Analysis system.
"""

import re
import json
from .color_analyzer import ColorAnalyzer

class ColorDataProcessor:
    """
    Processes color preference data for analysis.
    """
    
    # Standard color names and their variations
    COLOR_MAPPINGS = {
        "red": ["red", "crimson", "scarlet", "maroon", "burgundy", "ruby"],
        "blue": ["blue", "navy", "teal", "cyan", "indigo", "azure", "cobalt"],
        "green": ["green", "olive", "sage", "mint", "emerald", "forest", "lime"],
        "yellow": ["yellow", "gold", "amber", "lemon", "mustard"],
        "purple": ["purple", "violet", "lavender", "plum", "magenta", "mauve"],
        "orange": ["orange", "peach", "coral", "amber", "tangerine"],
        "pink": ["pink", "rose", "fuchsia", "salmon", "blush"],
        "black": ["black", "charcoal", "onyx", "ebony"],
        "white": ["white", "ivory", "cream", "eggshell"],
        "brown": ["brown", "tan", "beige", "khaki", "chocolate", "coffee"],
        "gray": ["gray", "grey", "silver", "slate", "ash"]
    }
    
    def __init__(self):
        """
        Initialize the ColorDataProcessor.
        """
        self.color_analyzer = ColorAnalyzer()
    
    def process_color_preferences(self, raw_data):
        """
        Process raw color preference data.
        
        Args:
            raw_data (dict): Raw color preference data from user input
            
        Returns:
            dict: Processed color data ready for analysis
        """
        processed_data = {}
        
        # Process primary and secondary colors
        if "primary_color" in raw_data:
            processed_data["primary_color"] = self._normalize_color(raw_data["primary_color"])
        
        if "secondary_color" in raw_data:
            processed_data["secondary_color"] = self._normalize_color(raw_data["secondary_color"])
        
        # Process color ranking
        if "color_ranking" in raw_data:
            if isinstance(raw_data["color_ranking"], list):
                processed_data["color_ranking"] = [self._normalize_color(color) for color in raw_data["color_ranking"]]
            elif isinstance(raw_data["color_ranking"], str):
                colors = [c.strip() for c in raw_data["color_ranking"].split(",")]
                processed_data["color_ranking"] = [self._normalize_color(color) for color in colors]
        
        # Process contextual preferences
        contextual_keys = ["work_color", "relaxation_color", "social_color", "creative_color", "stress_color"]
        for key in contextual_keys:
            if key in raw_data:
                processed_data[key] = self._normalize_color(raw_data[key])
        
        # Process color-emotion associations
        if "color_emotion_associations" in raw_data:
            processed_data["color_emotion_associations"] = {}
            for color, emotions in raw_data["color_emotion_associations"].items():
                normalized_color = self._normalize_color(color)
                if isinstance(emotions, list):
                    processed_data["color_emotion_associations"][normalized_color] = emotions
                elif isinstance(emotions, str):
                    processed_data["color_emotion_associations"][normalized_color] = [e.strip() for e in emotions.split(",")]
        
        return processed_data
    
    def analyze_color_data(self, color_data):
        """
        Analyze processed color data.
        
        Args:
            color_data (dict): Processed color preference data
            
        Returns:
            dict: Analysis results
        """
        # Process the data if it hasn't been processed yet
        if not self._is_processed(color_data):
            color_data = self.process_color_preferences(color_data)
        
        # Analyze the processed data
        analysis_results = self.color_analyzer.analyze_color_preferences(color_data)
        
        # Add the processed data to the results
        analysis_results["processed_data"] = color_data
        
        return analysis_results
    
    def _normalize_color(self, color_name):
        """
        Normalize color names to standard forms.
        
        Args:
            color_name (str): Raw color name
            
        Returns:
            str: Normalized color name
        """
        if not color_name:
            return ""
        
        color_name = color_name.lower().strip()
        
        # Check if the color name is already a standard color
        for standard_color in self.COLOR_MAPPINGS:
            if color_name == standard_color:
                return standard_color
        
        # Check if the color name is a variation of a standard color
        for standard_color, variations in self.COLOR_MAPPINGS.items():
            if color_name in variations:
                return standard_color
        
        # If no match found, try to find the closest match
        for standard_color, variations in self.COLOR_MAPPINGS.items():
            for variation in variations:
                if variation in color_name or color_name in variation:
                    return standard_color
        
        # If still no match, return the original color name
        return color_name
    
    def _is_processed(self, color_data):
        """
        Check if the color data has already been processed.
        
        Args:
            color_data (dict): Color preference data
            
        Returns:
            bool: True if the data has been processed, False otherwise
        """
        # Check if primary color is normalized
        if "primary_color" in color_data:
            primary_color = color_data["primary_color"].lower()
            if primary_color not in self.COLOR_MAPPINGS and not any(primary_color in variations for variations in self.COLOR_MAPPINGS.values()):
                return False
        
        # Check if color ranking is normalized
        if "color_ranking" in color_data and isinstance(color_data["color_ranking"], list):
            for color in color_data["color_ranking"]:
                if color not in self.COLOR_MAPPINGS and not any(color in variations for variations in self.COLOR_MAPPINGS.values()):
                    return False
        
        return True

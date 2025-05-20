"""
Response Processing Module for Psycho-Color Analysis System

This module handles the processing and structuring of LLM responses
for the Psycho-Color Analysis system.
"""

class ResponseProcessor:
    """
    Processes and structures LLM responses for the Psycho-Color Analysis system.
    """
    
    def __init__(self):
        """
        Initialize the response processor.
        """
        pass
    
    def process_color_preference_analysis(self, raw_response):
        """
        Process and structure the raw LLM response for color preference analysis.
        
        Args:
            raw_response (str): The raw response from the LLM
            
        Returns:
            dict: Structured analysis results
        """
        # Extract key sections from the response
        personality_traits = self._extract_section(raw_response, "personality traits", "emotional tendencies")
        emotional_tendencies = self._extract_section(raw_response, "emotional tendencies", "behavioral patterns")
        behavioral_patterns = self._extract_section(raw_response, "behavioral patterns", "strengths")
        strengths = self._extract_section(raw_response, "strengths", "growth areas")
        growth_areas = self._extract_section(raw_response, "growth areas", "")
        
        # Create a structured dictionary
        structured_response = {
            "personality_traits": self._format_list(personality_traits),
            "emotional_tendencies": self._format_list(emotional_tendencies),
            "behavioral_patterns": self._format_list(behavioral_patterns),
            "strengths": self._format_list(strengths),
            "growth_areas": self._format_list(growth_areas),
            "full_analysis": raw_response
        }
        
        return structured_response
    
    def process_jung_energy_analysis(self, raw_response):
        """
        Process and structure the raw LLM response for Jung's Color Energy analysis.
        
        Args:
            raw_response (str): The raw response from the LLM
            
        Returns:
            dict: Structured analysis results
        """
        # Extract primary and secondary color energies
        primary_energy = self._extract_value(raw_response, "Primary Color Energy:", "\n")
        secondary_energy = self._extract_value(raw_response, "Secondary Color Energy:", "\n")
        
        # Extract different aspects of the analysis
        communication_style = self._extract_section(raw_response, "Communication Style:", "Decision-making Approach:")
        decision_making = self._extract_section(raw_response, "Decision-making Approach:", "Relationship Dynamics:")
        relationship_dynamics = self._extract_section(raw_response, "Relationship Dynamics:", "Work Preferences:")
        work_preferences = self._extract_section(raw_response, "Work Preferences:", "Stress Responses:")
        stress_responses = self._extract_section(raw_response, "Stress Responses:", "")
        
        # Create a structured dictionary
        structured_response = {
            "primary_energy": primary_energy,
            "secondary_energy": secondary_energy,
            "energy_distribution": {
                "communication_style": communication_style,
                "decision_making": decision_making,
                "relationship_dynamics": relationship_dynamics,
                "work_preferences": work_preferences,
                "stress_responses": stress_responses
            },
            "full_analysis": raw_response
        }
        
        return structured_response
    
    def process_comprehensive_profile(self, raw_response):
        """
        Process and structure the raw LLM response for comprehensive profile analysis.
        
        Args:
            raw_response (str): The raw response from the LLM
            
        Returns:
            dict: Structured comprehensive profile
        """
        # Extract different sections of the profile
        personality_overview = self._extract_section(raw_response, "## 1. Personality Overview", "## 2.")
        jung_energy = self._extract_section(raw_response, "## 2. Jung Color Energy Distribution", "## 3.")
        emotional_landscape = self._extract_section(raw_response, "## 3. Emotional Landscape", "## 4.")
        interpersonal_dynamics = self._extract_section(raw_response, "## 4. Interpersonal Dynamics", "## 5.")
        environmental_preferences = self._extract_section(raw_response, "## 5. Environmental Preferences", "## 6.")
        growth_opportunities = self._extract_section(raw_response, "## 6. Growth Opportunities", "## 7.")
        practical_applications = self._extract_section(raw_response, "## 7. Practical Applications", "")
        
        # Extract primary and secondary energies from Jung energy section
        primary_energy = self._extract_value(jung_energy, "Primary Energy:", "\n")
        secondary_energy = self._extract_value(jung_energy, "Secondary Energy:", "\n")
        
        # Create a structured dictionary
        structured_response = {
            "personality_overview": personality_overview,
            "jung_energy": {
                "primary_energy": primary_energy,
                "secondary_energy": secondary_energy,
                "full_description": jung_energy
            },
            "emotional_landscape": emotional_landscape,
            "interpersonal_dynamics": interpersonal_dynamics,
            "environmental_preferences": environmental_preferences,
            "growth_opportunities": growth_opportunities,
            "practical_applications": practical_applications,
            "full_profile": raw_response
        }
        
        return structured_response
    
    def process_recommendations(self, raw_response):
        """
        Process and structure the raw LLM response for recommendations.
        
        Args:
            raw_response (str): The raw response from the LLM
            
        Returns:
            dict: Structured recommendations
        """
        # Extract different recommendation sections
        work_environment = self._extract_section(raw_response, "## 1. Optimal Work Environment", "## 2.")
        communication = self._extract_section(raw_response, "## 2. Communication Strategies", "## 3.")
        decision_making = self._extract_section(raw_response, "## 3. Decision-Making Approaches", "## 4.")
        stress_management = self._extract_section(raw_response, "## 4. Stress Management Techniques", "## 5.")
        personal_development = self._extract_section(raw_response, "## 5. Personal Development Opportunities", "## 6.")
        relationship_dynamics = self._extract_section(raw_response, "## 6. Relationship Dynamics", "## 7.")
        daily_practices = self._extract_section(raw_response, "## 7. Daily Practices for Well-Being", "")
        
        # Extract color recommendations from work environment section
        colors = self._extract_section(work_environment, "**Colors:**", "**Layout:**")
        
        # Create a structured dictionary
        structured_response = {
            "environment": {
                "colors": colors,
                "layout": self._extract_section(work_environment, "**Layout:**", "**Lighting:**"),
                "lighting": self._extract_section(work_environment, "**Lighting:**", "")
            },
            "communication_strategies": self._format_list(communication),
            "decision_making_approaches": self._format_list(decision_making),
            "stress_management": self._format_list(stress_management),
            "personal_development": self._format_list(personal_development),
            "relationship_dynamics": self._format_list(relationship_dynamics),
            "daily_practices": self._format_list(daily_practices),
            "full_recommendations": raw_response
        }
        
        return structured_response
    
    def _extract_section(self, text, start_marker, end_marker):
        """
        Extract a section of text between two markers.
        
        Args:
            text (str): The text to extract from
            start_marker (str): The marker indicating the start of the section
            end_marker (str): The marker indicating the end of the section
            
        Returns:
            str: The extracted section
        """
        try:
            start_idx = text.lower().index(start_marker.lower())
            start_idx = start_idx + len(start_marker)
            
            if end_marker:
                try:
                    end_idx = text.lower().index(end_marker.lower(), start_idx)
                    return text[start_idx:end_idx].strip()
                except ValueError:
                    return text[start_idx:].strip()
            else:
                return text[start_idx:].strip()
        except ValueError:
            return ""
    
    def _extract_value(self, text, label, delimiter):
        """
        Extract a labeled value from text.
        
        Args:
            text (str): The text to extract from
            label (str): The label preceding the value
            delimiter (str): The delimiter after the value
            
        Returns:
            str: The extracted value
        """
        try:
            start_idx = text.index(label) + len(label)
            try:
                end_idx = text.index(delimiter, start_idx)
                return text[start_idx:end_idx].strip()
            except ValueError:
                return text[start_idx:].strip()
        except ValueError:
            return ""
    
    def _format_list(self, text):
        """
        Format a text section as a list of items.
        
        Args:
            text (str): The text to format
            
        Returns:
            list: A list of items extracted from the text
        """
        # Split by newlines and look for list markers
        lines = text.split('\n')
        items = []
        
        for line in lines:
            line = line.strip()
            # Check for bullet points, dashes, or numbered lists
            if line.startswith('- ') or line.startswith('• ') or line.startswith('* '):
                items.append(line[2:].strip())
            elif line.startswith('1. ') or line.startswith('2. ') or line.startswith('3. '):
                items.append(line[3:].strip())
            elif line and not any(c in line for c in [':', '**', '#']):
                # Add non-empty lines that don't look like headers
                items.append(line)
        
        # If no list items were found, return the whole text as one item
        if not items and text.strip():
            return [text.strip()]
        
        return items

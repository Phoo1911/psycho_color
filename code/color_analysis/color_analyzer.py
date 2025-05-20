"""
Color Analysis Module for Psycho-Color Analysis System

This module contains the core algorithms for analyzing color preferences
and generating psychological insights based on color psychology frameworks.
"""

class ColorAnalyzer:
    """
    Core class for analyzing color preferences and generating psychological insights.
    """
    
    # Jung's Four Color Energies
    JUNG_COLORS = {
        "Cool Blue": {
            "traits": ["analytical", "objective", "detached", "logical", "methodical", "precise"],
            "colors": ["blue", "navy", "teal", "cyan", "indigo"]
        },
        "Earth Green": {
            "traits": ["supportive", "harmonious", "calming", "nurturing", "patient", "reliable"],
            "colors": ["green", "olive", "sage", "mint", "emerald"]
        },
        "Sunshine Yellow": {
            "traits": ["enthusiastic", "sociable", "dynamic", "persuasive", "optimistic", "creative"],
            "colors": ["yellow", "gold", "amber", "lemon", "mustard"]
        },
        "Fiery Red": {
            "traits": ["decisive", "assertive", "bold", "competitive", "direct", "action-oriented"],
            "colors": ["red", "crimson", "scarlet", "maroon", "burgundy"]
        }
    }
    
    # Color-Emotion Associations
    COLOR_EMOTIONS = {
        "red": ["passion", "excitement", "love", "anger", "energy", "danger"],
        "blue": ["calm", "trust", "wisdom", "peace", "loyalty", "sadness"],
        "green": ["growth", "harmony", "nature", "balance", "fertility", "envy"],
        "yellow": ["joy", "optimism", "happiness", "intellect", "attention", "anxiety"],
        "purple": ["creativity", "mystery", "spirituality", "luxury", "ambition", "introspection"],
        "orange": ["enthusiasm", "warmth", "sociability", "energy", "stimulation", "aggression"],
        "pink": ["love", "nurturing", "femininity", "compassion", "playfulness", "immaturity"],
        "black": ["power", "elegance", "formality", "death", "evil", "mystery"],
        "white": ["purity", "innocence", "cleanliness", "simplicity", "sterility", "emptiness"],
        "brown": ["reliability", "stability", "earthiness", "warmth", "dullness", "heaviness"]
    }
    
    # Personality Dimensions
    PERSONALITY_DIMENSIONS = {
        "introversion_extraversion": {
            "introversion": ["blue", "purple", "green", "black", "brown"],
            "extraversion": ["red", "orange", "yellow", "pink"]
        },
        "thinking_feeling": {
            "thinking": ["blue", "black", "white", "gray"],
            "feeling": ["red", "pink", "purple", "green"]
        },
        "stability_adaptability": {
            "stability": ["blue", "green", "brown", "black"],
            "adaptability": ["yellow", "orange", "red", "purple"]
        },
        "task_people": {
            "task_oriented": ["blue", "black", "red", "white"],
            "people_oriented": ["green", "pink", "yellow", "purple"]
        },
        "analytical_creative": {
            "analytical": ["blue", "black", "white", "gray"],
            "creative": ["purple", "yellow", "orange", "pink"]
        }
    }
    
    def __init__(self):
        """
        Initialize the ColorAnalyzer.
        """
        pass
    
    def analyze_color_preferences(self, color_data):
        """
        Analyze color preferences and generate psychological insights.
        
        Args:
            color_data (dict): Dictionary containing color preference data
            
        Returns:
            dict: Analysis results
        """
        results = {}
        
        # Analyze Jung's Color Energies
        results["jung_color_energies"] = self.analyze_jung_energies(color_data)
        
        # Analyze personality dimensions
        results["personality_dimensions"] = self.analyze_personality_dimensions(color_data)
        
        # Analyze emotional tendencies
        results["emotional_tendencies"] = self.analyze_emotional_tendencies(color_data)
        
        # Analyze contextual preferences
        if self._has_contextual_data(color_data):
            results["contextual_analysis"] = self.analyze_contextual_preferences(color_data)
        
        return results
    
    def analyze_jung_energies(self, color_data):
        """
        Analyze Jung's Four Color Energies based on color preferences.
        
        Args:
            color_data (dict): Dictionary containing color preference data
            
        Returns:
            dict: Jung's Color Energy analysis
        """
        # Extract color preferences
        primary_color = color_data.get("primary_color", "").lower()
        secondary_color = color_data.get("secondary_color", "").lower()
        
        # If color ranking is available, use it instead
        color_ranking = color_data.get("color_ranking", [])
        if color_ranking:
            if isinstance(color_ranking, str):
                color_ranking = [c.strip().lower() for c in color_ranking.split(",")]
            else:
                color_ranking = [c.lower() for c in color_ranking]
            
            if len(color_ranking) >= 1:
                primary_color = color_ranking[0]
            if len(color_ranking) >= 2:
                secondary_color = color_ranking[1]
        
        # Calculate energy scores
        energy_scores = {
            "Cool Blue": 0,
            "Earth Green": 0,
            "Sunshine Yellow": 0,
            "Fiery Red": 0
        }
        
        # Score based on primary and secondary colors
        for energy, data in self.JUNG_COLORS.items():
            if primary_color in data["colors"]:
                energy_scores[energy] += 10
            if secondary_color in data["colors"]:
                energy_scores[energy] += 5
        
        # Score based on color ranking if available
        if color_ranking:
            for i, color in enumerate(color_ranking[:5]):  # Consider top 5 colors
                weight = 10 - (i * 2)  # 10, 8, 6, 4, 2
                for energy, data in self.JUNG_COLORS.items():
                    if color in data["colors"]:
                        energy_scores[energy] += weight
        
        # Determine primary and secondary energies
        sorted_energies = sorted(energy_scores.items(), key=lambda x: x[1], reverse=True)
        primary_energy = sorted_energies[0][0]
        secondary_energy = sorted_energies[1][0]
        
        # Calculate energy distribution percentages
        total_score = sum(energy_scores.values())
        if total_score > 0:
            energy_distribution = {energy: (score / total_score) * 100 for energy, score in energy_scores.items()}
        else:
            energy_distribution = {energy: 25 for energy in energy_scores}
        
        # Get traits for primary and secondary energies
        primary_traits = self.JUNG_COLORS[primary_energy]["traits"]
        secondary_traits = self.JUNG_COLORS[secondary_energy]["traits"]
        
        return {
            "primary_energy": primary_energy,
            "secondary_energy": secondary_energy,
            "energy_distribution": energy_distribution,
            "primary_traits": primary_traits,
            "secondary_traits": secondary_traits
        }
    
    def analyze_personality_dimensions(self, color_data):
        """
        Analyze personality dimensions based on color preferences.
        
        Args:
            color_data (dict): Dictionary containing color preference data
            
        Returns:
            dict: Personality dimension analysis
        """
        # Extract color preferences
        primary_color = color_data.get("primary_color", "").lower()
        secondary_color = color_data.get("secondary_color", "").lower()
        
        # If color ranking is available, use it
        color_ranking = color_data.get("color_ranking", [])
        if color_ranking:
            if isinstance(color_ranking, str):
                color_ranking = [c.strip().lower() for c in color_ranking.split(",")]
            else:
                color_ranking = [c.lower() for c in color_ranking]
        else:
            color_ranking = []
            if primary_color:
                color_ranking.append(primary_color)
            if secondary_color:
                color_ranking.append(secondary_color)
        
        # Calculate dimension scores
        dimension_scores = {}
        
        for dimension, poles in self.PERSONALITY_DIMENSIONS.items():
            pole1, pole2 = list(poles.keys())
            pole1_score = 0
            pole2_score = 0
            
            # Score based on color ranking
            for i, color in enumerate(color_ranking[:5]):  # Consider top 5 colors
                weight = 10 - (i * 2)  # 10, 8, 6, 4, 2
                if color in poles[pole1]:
                    pole1_score += weight
                if color in poles[pole2]:
                    pole2_score += weight
            
            # Calculate dimension value (-100 to +100)
            total = pole1_score + pole2_score
            if total > 0:
                dimension_value = ((pole2_score - pole1_score) / total) * 100
            else:
                dimension_value = 0
            
            dimension_scores[dimension] = dimension_value
        
        # Determine dominant traits
        dominant_traits = []
        
        if dimension_scores["introversion_extraversion"] < -20:
            dominant_traits.append("introverted")
        elif dimension_scores["introversion_extraversion"] > 20:
            dominant_traits.append("extraverted")
        
        if dimension_scores["thinking_feeling"] < -20:
            dominant_traits.append("analytical thinker")
        elif dimension_scores["thinking_feeling"] > 20:
            dominant_traits.append("empathetic feeler")
        
        if dimension_scores["stability_adaptability"] < -20:
            dominant_traits.append("stability-focused")
        elif dimension_scores["stability_adaptability"] > 20:
            dominant_traits.append("adaptability-focused")
        
        if dimension_scores["task_people"] < -20:
            dominant_traits.append("task-oriented")
        elif dimension_scores["task_people"] > 20:
            dominant_traits.append("people-oriented")
        
        if dimension_scores["analytical_creative"] < -20:
            dominant_traits.append("methodical")
        elif dimension_scores["analytical_creative"] > 20:
            dominant_traits.append("creative")
        
        return {
            "dimension_scores": dimension_scores,
            "dominant_traits": dominant_traits
        }
    
    def analyze_emotional_tendencies(self, color_data):
        """
        Analyze emotional tendencies based on color preferences.
        
        Args:
            color_data (dict): Dictionary containing color preference data
            
        Returns:
            dict: Emotional tendency analysis
        """
        # Extract color preferences
        primary_color = color_data.get("primary_color", "").lower()
        secondary_color = color_data.get("secondary_color", "").lower()
        
        # Get color ranking if available
        color_ranking = color_data.get("color_ranking", [])
        if color_ranking:
            if isinstance(color_ranking, str):
                color_ranking = [c.strip().lower() for c in color_ranking.split(",")]
            else:
                color_ranking = [c.lower() for c in color_ranking]
        else:
            color_ranking = []
            if primary_color:
                color_ranking.append(primary_color)
            if secondary_color:
                color_ranking.append(secondary_color)
        
        # Get color-emotion associations
        primary_emotions = self.COLOR_EMOTIONS.get(primary_color, [])
        secondary_emotions = self.COLOR_EMOTIONS.get(secondary_color, [])
        
        # Calculate emotion scores
        emotion_scores = {}
        
        for color in color_ranking[:5]:  # Consider top 5 colors
            weight = 10 - color_ranking.index(color) * 2  # 10, 8, 6, 4, 2
            emotions = self.COLOR_EMOTIONS.get(color, [])
            
            for emotion in emotions:
                if emotion in emotion_scores:
                    emotion_scores[emotion] += weight
                else:
                    emotion_scores[emotion] = weight
        
        # Get top emotions
        sorted_emotions = sorted(emotion_scores.items(), key=lambda x: x[1], reverse=True)
        top_emotions = [emotion for emotion, score in sorted_emotions[:5]]  # Top 5 emotions
        
        # Determine emotional patterns
        emotional_patterns = []
        
        # Check for balance between positive and negative emotions
        positive_emotions = ["love", "joy", "optimism", "happiness", "calm", "trust", "peace", "growth", "harmony"]
        negative_emotions = ["anger", "sadness", "anxiety", "envy", "aggression", "fear"]
        
        positive_score = sum(emotion_scores.get(emotion, 0) for emotion in positive_emotions)
        negative_score = sum(emotion_scores.get(emotion, 0) for emotion in negative_emotions)
        
        if positive_score > negative_score * 2:
            emotional_patterns.append("predominantly positive emotional outlook")
        elif negative_score > positive_score * 2:
            emotional_patterns.append("tendency toward emotional caution")
        else:
            emotional_patterns.append("balanced emotional perspective")
        
        # Check for specific patterns
        if "calm" in top_emotions and "peace" in top_emotions:
            emotional_patterns.append("values emotional stability")
        
        if "passion" in top_emotions and "energy" in top_emotions:
            emotional_patterns.append("emotionally expressive")
        
        if "trust" in top_emotions and "loyalty" in top_emotions:
            emotional_patterns.append("values emotional consistency in relationships")
        
        return {
            "primary_emotions": primary_emotions,
            "secondary_emotions": secondary_emotions,
            "top_emotions": top_emotions,
            "emotional_patterns": emotional_patterns
        }
    
    def analyze_contextual_preferences(self, color_data):
        """
        Analyze contextual color preferences.
        
        Args:
            color_data (dict): Dictionary containing color preference data
            
        Returns:
            dict: Contextual preference analysis
        """
        # Extract contextual preferences
        work_color = color_data.get("work_color", "").lower()
        relaxation_color = color_data.get("relaxation_color", "").lower()
        social_color = color_data.get("social_color", "").lower()
        creative_color = color_data.get("creative_color", "").lower()
        stress_color = color_data.get("stress_color", "").lower()
        
        # Analyze consistency across contexts
        colors = [c for c in [work_color, relaxation_color, social_color, creative_color, stress_color] if c]
        unique_colors = set(colors)
        consistency_score = 1 - (len(unique_colors) - 1) / max(1, len(colors) - 1)
        
        # Determine contextual patterns
        contextual_patterns = []
        
        if consistency_score > 0.7:
            contextual_patterns.append("high consistency across contexts")
        elif consistency_score < 0.3:
            contextual_patterns.append("strong contextual adaptation")
        
        # Analyze work environment preferences
        work_insights = []
        if work_color in self.JUNG_COLORS["Cool Blue"]["colors"]:
            work_insights.append("analytical work approach")
            work_insights.append("values structure and clarity in work environment")
        elif work_color in self.JUNG_COLORS["Earth Green"]["colors"]:
            work_insights.append("supportive work approach")
            work_insights.append("values harmony and collaboration in work environment")
        elif work_color in self.JUNG_COLORS["Sunshine Yellow"]["colors"]:
            work_insights.append("enthusiastic work approach")
            work_insights.append("values creativity and stimulation in work environment")
        elif work_color in self.JUNG_COLORS["Fiery Red"]["colors"]:
            work_insights.append("decisive work approach")
            work_insights.append("values efficiency and results in work environment")
        
        # Analyze relaxation preferences
        relaxation_insights = []
        if relaxation_color in self.JUNG_COLORS["Cool Blue"]["colors"]:
            relaxation_insights.append("mental relaxation through intellectual activities")
        elif relaxation_color in self.JUNG_COLORS["Earth Green"]["colors"]:
            relaxation_insights.append("relaxation through connection with nature and harmony")
        elif relaxation_color in self.JUNG_COLORS["Sunshine Yellow"]["colors"]:
            relaxation_insights.append("relaxation through social and stimulating activities")
        elif relaxation_color in self.JUNG_COLORS["Fiery Red"]["colors"]:
            relaxation_insights.append("relaxation through physical activities and challenges")
        
        # Analyze social preferences
        social_insights = []
        if social_color in self.JUNG_COLORS["Cool Blue"]["colors"]:
            social_insights.append("values depth and meaning in social interactions")
        elif social_color in self.JUNG_COLORS["Earth Green"]["colors"]:
            social_insights.append("values harmony and connection in social settings")
        elif social_color in self.JUNG_COLORS["Sunshine Yellow"]["colors"]:
            social_insights.append("values enthusiasm and energy in social settings")
        elif social_color in self.JUNG_COLORS["Fiery Red"]["colors"]:
            social_insights.append("values directness and action in social settings")
        
        return {
            "consistency_score": consistency_score,
            "contextual_patterns": contextual_patterns,
            "work_insights": work_insights,
            "relaxation_insights": relaxation_insights,
            "social_insights": social_insights
        }
    
    def _has_contextual_data(self, color_data):
        """
        Check if the color data contains contextual preferences.
        
        Args:
            color_data (dict): Dictionary containing color preference data
            
        Returns:
            bool: True if contextual data is available, False otherwise
        """
        contextual_keys = ["work_color", "relaxation_color", "social_color", "creative_color", "stress_color"]
        return any(key in color_data for key in contextual_keys)

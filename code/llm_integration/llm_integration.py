"""
LLM Integration Module for Psycho-Color Analysis System

This module handles the integration with Large Language Models for
generating psychological insights based on color preference data.
"""

import json
import requests
from .prompt_templates import (
    PromptTemplates,
    create_color_preference_prompt,
    create_jung_energy_prompt,
    create_comprehensive_profile_prompt,
    create_recommendations_prompt
)

class LLMIntegration:
    """
    Handles integration with Large Language Models for psychological analysis.
    """
    
    def __init__(self, api_key=None, model="gpt-4"):
        """
        Initialize the LLM integration.
        
        Args:
            api_key (str, optional): API key for the LLM service
            model (str, optional): Model to use for analysis
        """
        self.api_key = api_key
        self.model = model
        self.system_prompt = PromptTemplates.SYSTEM_PROMPT
    
    def analyze_color_preferences(self, color_data):
        """
        Analyze color preferences using the LLM.
        
        Args:
            color_data (dict): Dictionary containing color preference data
            
        Returns:
            dict: Analysis results
        """
        prompt = create_color_preference_prompt(color_data)
        response = self._generate_response(prompt)
        return self._parse_color_preference_analysis(response)
    
    def analyze_jung_color_energy(self, color_ranking):
        """
        Analyze Jung's Color Energy distribution.
        
        Args:
            color_ranking (list): Ordered list of colors from most to least preferred
            
        Returns:
            dict: Analysis results with color energy distribution
        """
        prompt = create_jung_energy_prompt(color_ranking)
        response = self._generate_response(prompt)
        return self._parse_jung_energy_analysis(response)
    
    def generate_comprehensive_profile(self, all_color_data):
        """
        Generate a comprehensive psychological profile.
        
        Args:
            all_color_data (dict): Dictionary containing all color preference data
            
        Returns:
            dict: Comprehensive profile analysis
        """
        prompt = create_comprehensive_profile_prompt(all_color_data)
        response = self._generate_response(prompt)
        return self._parse_comprehensive_profile(response)
    
    def generate_recommendations(self, profile_summary):
        """
        Generate personalized recommendations based on profile.
        
        Args:
            profile_summary (str): Summary of the psychological profile
            
        Returns:
            dict: Personalized recommendations
        """
        prompt = create_recommendations_prompt(profile_summary)
        response = self._generate_response(prompt)
        return self._parse_recommendations(response)
    
    def _generate_response(self, prompt):
        """
        Generate a response from the LLM.
        
        Args:
            prompt (str): The prompt to send to the LLM
            
        Returns:
            str: The LLM's response
        """
        # This is a placeholder for actual API integration
        # In a real implementation, this would make an API call to the LLM service
        
        # Simulated response for development purposes
        return self._simulate_llm_response(prompt)
    
    def _simulate_llm_response(self, prompt):
        """
        Simulate an LLM response for development purposes.
        
        Args:
            prompt (str): The prompt sent to the LLM
            
        Returns:
            str: Simulated response
        """
        # This is a placeholder that would be replaced with actual API calls
        # For now, we'll return template responses based on the prompt content
        
        if "Jung color energy" in prompt:
            return """
            Based on the color preference ranking provided, the user's Jung's Four Color Energy distribution is as follows:
            
            Primary Color Energy: Cool Blue
            Secondary Color Energy: Earth Green
            
            The user shows a strong preference for analytical and methodical approaches (Cool Blue) with a secondary tendency toward supportive and harmonious interactions (Earth Green). Their Sunshine Yellow and Fiery Red energies appear to be less dominant.
            
            This energy distribution manifests in the following ways:
            
            Communication Style:
            The user likely communicates in a clear, logical, and structured manner. They prefer to provide complete information and may sometimes go into more detail than necessary. They value accuracy and precision in communication and may become frustrated with vague or emotional arguments.
            
            Decision-making Approach:
            The user tends to approach decisions methodically, gathering all relevant information before proceeding. They likely value evidence-based reasoning and may take longer to reach conclusions as they carefully weigh all options. Their secondary Earth Green energy suggests they also consider the impact of decisions on people and relationships.
            
            Relationship Dynamics:
            In relationships, the user likely values honesty, reliability, and depth. They may take time to open up to others, preferring to establish trust gradually. Their combination of Cool Blue and Earth Green suggests they are a loyal and thoughtful friend or partner who provides both practical support and emotional stability.
            
            Work Preferences:
            The user likely thrives in environments that allow for careful analysis, planning, and attention to detail. They probably prefer clear structures, processes, and expectations. Their secondary Earth Green energy suggests they also value harmonious work environments and may excel in collaborative settings where their supportive nature can benefit the team.
            
            Stress Responses:
            Under stress, the user may become withdrawn, overthink problems, or become excessively critical. Their Cool Blue energy may lead them to analyze stressful situations extensively, sometimes to the point of analysis paralysis. Their Earth Green energy may manifest as a reluctance to confront issues directly, preferring to maintain harmony even at personal cost.
            """
        
        elif "comprehensive psychological profile" in prompt:
            return """
            # Comprehensive Psychological Profile
            
            ## 1. Personality Overview
            
            Based on the color preference data provided, this individual demonstrates a personality that balances analytical thinking with empathetic understanding. They show a methodical approach to life with a preference for structure and clarity, while also valuing harmony and meaningful connections. Their color preferences suggest someone who is thoughtful, detail-oriented, and values depth over breadth in their experiences and relationships.
            
            ## 2. Jung Color Energy Distribution
            
            **Primary Energy: Cool Blue (Analytical)**
            The dominant Cool Blue energy indicates someone who approaches situations with careful analysis and logical reasoning. They value accuracy, precision, and thoroughness. This energy manifests as a methodical approach to problem-solving and a desire to understand systems and processes in depth.
            
            **Secondary Energy: Earth Green (Supportive)**
            The secondary Earth Green energy reveals a caring, supportive nature that values harmony and meaningful connections. This balances the analytical Cool Blue by adding emotional intelligence and consideration for others' needs and feelings.
            
            **Tertiary Energies:**
            - Sunshine Yellow appears moderately, suggesting some capacity for enthusiasm and idea generation
            - Fiery Red is least prominent, indicating that decisive action and results-focus may not be natural strengths
            
            ## 3. Emotional Landscape
            
            The individual's emotional patterns show a preference for calm, stable emotional states over intense or volatile ones. Their emotional responses tend to be measured and proportionate to situations. They likely:
            
            - Process emotions internally before expressing them
            - Value emotional authenticity but may struggle with spontaneous expression
            - Experience deep but controlled emotional responses
            - Prefer emotional consistency in relationships
            - May need time to process complex emotional situations
            
            ## 4. Interpersonal Dynamics
            
            In relationships and communication, this individual likely:
            
            - Listens attentively and values thoughtful exchanges
            - Prefers depth over breadth in relationships
            - Communicates with precision and clarity
            - Values reliability and consistency in others
            - May take time to warm up in new social situations
            - Offers support and practical help to those they care about
            - Prefers small groups or one-on-one interactions over large gatherings
            
            ## 5. Environmental Preferences
            
            Optimal settings for this individual's productivity and well-being include:
            
            - Organized, uncluttered spaces with minimal distractions
            - Color schemes featuring blues and greens that promote focus and calm
            - Adequate private space for concentration and reflection
            - Natural elements that provide connection to the outdoors
            - Consistent routines with some flexibility
            - Clear boundaries between work and relaxation spaces
            
            ## 6. Growth Opportunities
            
            Areas for personal development based on this color profile include:
            
            - Developing more comfort with spontaneity and uncertainty
            - Practicing more direct expression of needs and opinions
            - Building confidence in quick decision-making without extensive analysis
            - Expanding comfort with larger social settings and networking
            - Balancing analytical thinking with intuitive insights
            - Learning to delegate rather than handling everything personally
            
            ## 7. Practical Applications
            
            Actionable insights for daily life include:
            
            - Structure complex tasks into clear, manageable steps
            - Allow buffer time between activities for mental processing
            - Create dedicated spaces for different types of activities
            - Use color strategically in the environment to support different mental states
            - Schedule regular time for meaningful one-on-one connections
            - Practice mindfulness to balance analytical thinking with present-moment awareness
            - Use written reflection to process emotions and experiences
            """
        
        elif "recommendations" in prompt:
            return """
            # Personalized Recommendations
            
            ## 1. Optimal Work Environment
            
            **Colors:**
            - Primary: Soft blues to promote focus and clear thinking
            - Accents: Touches of green to create balance and reduce stress
            - Avoid: Excessive red or orange which may create unnecessary tension
            
            **Layout:**
            - Organized workspace with minimal clutter
            - Dedicated zones for different types of tasks
            - Visual barriers to reduce distractions when needed
            - Natural light source positioned to avoid screen glare
            
            **Lighting:**
            - Natural light supplemented with cool-temperature lighting
            - Task lighting for detailed work
            - Adjustable lighting options for different times of day
            
            ## 2. Communication Strategies
            
            - Lead with data and logical frameworks when presenting ideas
            - Allow processing time before expecting responses to complex questions
            - Use written communication for detailed or important information
            - Balance factual content with acknowledgment of people's feelings
            - Practice active listening to strengthen your Earth Green energy
            - Prepare talking points for important conversations
            
            ## 3. Decision-Making Approaches
            
            - Leverage your analytical strengths by creating decision matrices
            - Set time limits for analysis to avoid overthinking
            - Balance data-driven decisions with consideration of impact on people
            - Practice making small decisions more quickly to build comfort with uncertainty
            - Consider using structured frameworks like SWOT analysis or Eisenhower Matrix
            - Document decision rationale to build confidence in your process
            
            ## 4. Stress Management Techniques
            
            - Schedule regular breaks for mental reset (e.g., Pomodoro Technique)
            - Create a dedicated "wind-down" space with calming blue and green elements
            - Practice progressive muscle relaxation to release physical tension
            - Maintain a decision journal to prevent rumination on past choices
            - Use nature walks to engage your Earth Green energy
            - Develop clear boundaries between work and personal time
            
            ## 5. Personal Development Opportunities
            
            - Join small group activities that require spontaneity
            - Practice expressing opinions directly in low-stakes situations
            - Take a course in creative thinking to balance analytical tendencies
            - Volunteer for leadership roles that require decisive action
            - Develop comfort with networking through structured events
            - Practice delegating tasks that don't require your personal attention
            
            ## 6. Relationship Dynamics
            
            - Seek connections with individuals who appreciate depth and authenticity
            - Balance relationships with analytical thinkers and more spontaneous individuals
            - Communicate your need for processing time in close relationships
            - Schedule regular quality time with close connections
            - Express appreciation explicitly rather than assuming it's understood
            - Look for shared activities that engage both your analytical and nurturing sides
            
            ## 7. Daily Practices for Well-Being
            
            - Begin the day with structured planning to reduce decision fatigue
            - Incorporate blue and green elements in your personal spaces
            - Practice mindfulness meditation to balance analytical thinking
            - Maintain a reflection journal to process experiences
            - Create transition rituals between different activities
            - Engage in nature-based activities to nurture your Earth Green energy
            - Schedule regular time for deep learning in areas of interest
            """
        
        else:
            return """
            Based on the user's color preferences, I can provide the following psychological analysis:
            
            The preference for blue as a primary color suggests an analytical, thoughtful personality with a tendency toward logical reasoning and careful consideration. Blue preference is often associated with reliability, trustworthiness, and a methodical approach to challenges. This individual likely values clarity, precision, and depth in their thinking and communications.
            
            The secondary preference for green indicates a balancing element of empathy, harmony, and growth-orientation. This suggests the individual values relationships and emotional well-being alongside intellectual pursuits. The combination of blue and green as top preferences points to someone who approaches situations with both careful analysis and consideration for human factors.
            
            The contextual preferences reveal interesting patterns. The preference for blue in work environments reinforces the analytical approach to professional tasks, suggesting the individual thrives in settings that allow for methodical problem-solving and attention to detail. The preference for green in relaxation spaces indicates a need for harmony and natural elements when unwinding, possibly connecting to nature as a restorative practice.
            
            The social setting preference for purple suggests a desire for meaningful, authentic connections rather than superficial interactions. Purple in social contexts often indicates someone who values depth in conversations and relationships, preferring quality over quantity in their social circle.
            
            In terms of Jung's color energies, this profile strongly suggests a primary Cool Blue energy (analytical, detail-oriented, thoughtful) with a secondary Earth Green energy (supportive, harmony-seeking, relationship-focused). This combination typically manifests as someone who approaches problems methodically while remaining sensitive to the human elements involved.
            
            Potential strengths include:
            - Thorough analysis and attention to detail
            - Reliability and consistency in approach
            - Balanced consideration of logical and emotional factors
            - Thoughtful communication style
            - Ability to create harmonious environments
            
            Areas for growth might include:
            - Developing comfort with spontaneity and uncertainty
            - Building confidence in quick decision-making
            - Expressing emotions more readily
            - Taking action without complete information
            - Embracing change and disruption as opportunities
            
            This color profile suggests someone who would thrive in environments that provide structure while allowing for meaningful connections, and in roles that value both analytical thinking and interpersonal sensitivity.
            """
    
    def _parse_color_preference_analysis(self, response):
        """
        Parse the LLM's response to color preference analysis.
        
        Args:
            response (str): The LLM's response
            
        Returns:
            dict: Structured analysis results
        """
        # In a real implementation, this would parse the response into a structured format
        # For now, we'll return a simple dictionary
        return {
            "personality_traits": self._extract_section(response, "Potential strengths include:", "Areas for growth might include:"),
            "emotional_tendencies": self._extract_section(response, "emotional", "strengths"),
            "behavioral_patterns": self._extract_section(response, "This color profile suggests", "thrive in environments"),
            "strengths": self._extract_section(response, "Potential strengths include:", "Areas for growth might include:"),
            "growth_areas": self._extract_section(response, "Areas for growth might include:", "This color profile suggests"),
            "full_analysis": response
        }
    
    def _parse_jung_energy_analysis(self, response):
        """
        Parse the LLM's response to Jung's Color Energy analysis.
        
        Args:
            response (str): The LLM's response
            
        Returns:
            dict: Structured analysis results
        """
        # Extract primary and secondary color energies
        primary_energy = self._extract_value(response, "Primary Color Energy:", "\n")
        secondary_energy = self._extract_value(response, "Secondary Color Energy:", "\n")
        
        # Extract different aspects of the analysis
        communication_style = self._extract_section(response, "Communication Style:", "Decision-making Approach:")
        decision_making = self._extract_section(response, "Decision-making Approach:", "Relationship Dynamics:")
        relationship_dynamics = self._extract_section(response, "Relationship Dynamics:", "Work Preferences:")
        work_preferences = self._extract_section(response, "Work Preferences:", "Stress Responses:")
        stress_responses = self._extract_section(response, "Stress Responses:", "")
        
        return {
            "primary_energy": primary_energy,
            "secondary_energy": secondary_energy,
            "communication_style": communication_style,
            "decision_making": decision_making,
            "relationship_dynamics": relationship_dynamics,
            "work_preferences": work_preferences,
            "stress_responses": stress_responses,
            "full_analysis": response
        }
    
    def _parse_comprehensive_profile(self, response):
        """
        Parse the LLM's response to comprehensive profile analysis.
        
        Args:
            response (str): The LLM's response
            
        Returns:
            dict: Structured comprehensive profile
        """
        # Extract different sections of the profile
        personality_overview = self._extract_section(response, "## 1. Personality Overview", "## 2.")
        jung_energy = self._extract_section(response, "## 2. Jung Color Energy Distribution", "## 3.")
        emotional_landscape = self._extract_section(response, "## 3. Emotional Landscape", "## 4.")
        interpersonal_dynamics = self._extract_section(response, "## 4. Interpersonal Dynamics", "## 5.")
        environmental_preferences = self._extract_section(response, "## 5. Environmental Preferences", "## 6.")
        growth_opportunities = self._extract_section(response, "## 6. Growth Opportunities", "## 7.")
        practical_applications = self._extract_section(response, "## 7. Practical Applications", "")
        
        return {
            "personality_overview": personality_overview,
            "jung_energy": jung_energy,
            "emotional_landscape": emotional_landscape,
            "interpersonal_dynamics": interpersonal_dynamics,
            "environmental_preferences": environmental_preferences,
            "growth_opportunities": growth_opportunities,
            "practical_applications": practical_applications,
            "full_profile": response
        }
    
    def _parse_recommendations(self, response):
        """
        Parse the LLM's response to recommendations.
        
        Args:
            response (str): The LLM's response
            
        Returns:
            dict: Structured recommendations
        """
        # Extract different recommendation sections
        work_environment = self._extract_section(response, "## 1. Optimal Work Environment", "## 2.")
        communication = self._extract_section(response, "## 2. Communication Strategies", "## 3.")
        decision_making = self._extract_section(response, "## 3. Decision-Making Approaches", "## 4.")
        stress_management = self._extract_section(response, "## 4. Stress Management Techniques", "## 5.")
        personal_development = self._extract_section(response, "## 5. Personal Development Opportunities", "## 6.")
        relationship_dynamics = self._extract_section(response, "## 6. Relationship Dynamics", "## 7.")
        daily_practices = self._extract_section(response, "## 7. Daily Practices for Well-Being", "")
        
        return {
            "work_environment": work_environment,
            "communication": communication,
            "decision_making": decision_making,
            "stress_management": stress_management,
            "personal_development": personal_development,
            "relationship_dynamics": relationship_dynamics,
            "daily_practices": daily_practices,
            "full_recommendations": response
        }
    
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
            start_idx = text.index(start_marker) + len(start_marker)
            if end_marker:
                end_idx = text.index(end_marker, start_idx)
                return text[start_idx:end_idx].strip()
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
            end_idx = text.index(delimiter, start_idx)
            return text[start_idx:end_idx].strip()
        except ValueError:
            return ""

"""
Prompt Templates for Psycho-Color Analysis System

This module contains prompt templates for the LLM integration layer.
These templates are used to construct effective prompts for the LLM
based on color preference data and psychological frameworks.
"""

class PromptTemplates:
    """
    A collection of prompt templates for different analysis types.
    """
    
    SYSTEM_PROMPT = """
    You are a psychological analysis assistant specializing in color psychology.
    Your task is to analyze color preferences and provide insights into personality traits,
    emotional tendencies, and behavioral patterns based on established color psychology frameworks.
    
    Use the following frameworks in your analysis:
    1. Jung's Four Color Energies (Cool Blue, Earth Green, Sunshine Yellow, Fiery Red)
    2. Color-Emotion Associations
    3. Color-Personality Correlations
    4. Color-in-Context Theory
    
    Provide thoughtful, nuanced analysis that considers the complexity of human psychology.
    Avoid overgeneralizations and acknowledge the limitations of color psychology.
    Focus on providing actionable insights that can help the individual understand themselves better.
    """
    
    COLOR_PREFERENCE_ANALYSIS = """
    Based on the user's color preferences:
    
    Primary color preference: {primary_color}
    Secondary color preference: {secondary_color}
    Least preferred color: {least_preferred_color}
    
    Context-specific preferences:
    - Work environment: {work_color}
    - Relaxation space: {relaxation_color}
    - Social settings: {social_color}
    
    Please analyze what these preferences suggest about the user's personality traits,
    emotional tendencies, and behavioral patterns. Consider:
    
    1. What do these preferences suggest about their dominant Jung color energy?
    2. What personality traits are associated with these color preferences?
    3. What emotional tendencies might these preferences indicate?
    4. How might these preferences influence their behavior in different contexts?
    5. What strengths and potential growth areas do these preferences suggest?
    
    Provide a comprehensive analysis with specific insights rather than general statements.
    """
    
    JUNG_COLOR_ENERGY_ANALYSIS = """
    Based on the user's color preference data, analyze their Jung's Four Color Energy distribution:
    
    Color preference ranking: {color_ranking}
    
    Please determine:
    
    1. The user's primary color energy (Cool Blue, Earth Green, Sunshine Yellow, or Fiery Red)
    2. Their secondary color energy
    3. The balance between the four energies
    4. How this energy distribution might manifest in their:
       - Communication style
       - Decision-making approach
       - Relationship dynamics
       - Work preferences
       - Stress responses
    
    Provide specific insights about how their color energy distribution influences their
    psychological functioning and interpersonal dynamics.
    """
    
    COLOR_EMOTION_ANALYSIS = """
    Based on the user's color-emotion associations:
    
    {color_emotion_associations}
    
    Please analyze:
    
    1. What these associations reveal about the user's emotional landscape
    2. Any patterns in their emotional responses
    3. How their emotional tendencies might influence their decision-making
    4. Potential emotional strengths and challenges
    5. Strategies for emotional well-being based on these associations
    
    Provide specific insights about how their color-emotion associations relate to
    their psychological functioning and emotional patterns.
    """
    
    CONTEXTUAL_COLOR_ANALYSIS = """
    Based on the user's contextual color preferences:
    
    Work environment: {work_color}
    Relaxation space: {relaxation_color}
    Social settings: {social_color}
    Creative activities: {creative_color}
    Stressful situations: {stress_color}
    
    Please analyze:
    
    1. What these contextual preferences reveal about their adaptability
    2. How their psychological needs differ across contexts
    3. Potential strengths and challenges in different environments
    4. Optimal environmental conditions for their well-being
    5. Strategies for creating supportive environments based on these preferences
    
    Provide specific insights about how their contextual color preferences relate to
    their psychological functioning in different situations.
    """
    
    COMPREHENSIVE_PROFILE = """
    Based on all the color preference data provided:
    
    {all_color_data}
    
    Please generate a comprehensive psychological profile that includes:
    
    1. Personality Overview: Key traits and tendencies
    2. Jung Color Energy Distribution: Primary and secondary energies
    3. Emotional Landscape: Emotional patterns and tendencies
    4. Interpersonal Dynamics: Communication and relationship styles
    5. Environmental Preferences: Optimal settings for productivity and well-being
    6. Growth Opportunities: Areas for personal development
    7. Practical Applications: Actionable insights for daily life
    
    Provide a detailed, nuanced analysis that integrates insights from multiple
    color psychology frameworks while acknowledging the complexity of human psychology.
    """
    
    RECOMMENDATIONS = """
    Based on the psychological profile derived from color preferences:
    
    {profile_summary}
    
    Please provide specific recommendations for:
    
    1. Optimal work environment (colors, layout, lighting)
    2. Communication strategies that align with their color energy
    3. Decision-making approaches that leverage their strengths
    4. Stress management techniques suited to their profile
    5. Personal development opportunities based on their color psychology
    6. Relationship dynamics they might find most fulfilling
    7. Daily practices that could enhance their well-being
    
    Provide practical, actionable recommendations that the user can implement
    to optimize their environments and interactions.
    """

def format_prompt(template, **kwargs):
    """
    Format a prompt template with the provided keyword arguments.
    
    Args:
        template (str): The prompt template to format
        **kwargs: Keyword arguments to fill in the template
        
    Returns:
        str: The formatted prompt
    """
    return template.format(**kwargs)

def create_color_preference_prompt(color_data):
    """
    Create a prompt for color preference analysis.
    
    Args:
        color_data (dict): Dictionary containing color preference data
        
    Returns:
        str: Formatted prompt for color preference analysis
    """
    return format_prompt(
        PromptTemplates.COLOR_PREFERENCE_ANALYSIS,
        primary_color=color_data.get('primary_color', 'Unknown'),
        secondary_color=color_data.get('secondary_color', 'Unknown'),
        least_preferred_color=color_data.get('least_preferred_color', 'Unknown'),
        work_color=color_data.get('work_color', 'Unknown'),
        relaxation_color=color_data.get('relaxation_color', 'Unknown'),
        social_color=color_data.get('social_color', 'Unknown')
    )

def create_jung_energy_prompt(color_ranking):
    """
    Create a prompt for Jung's Color Energy analysis.
    
    Args:
        color_ranking (list): Ordered list of colors from most to least preferred
        
    Returns:
        str: Formatted prompt for Jung's Color Energy analysis
    """
    return format_prompt(
        PromptTemplates.JUNG_COLOR_ENERGY_ANALYSIS,
        color_ranking=', '.join(color_ranking)
    )

def create_comprehensive_profile_prompt(all_color_data):
    """
    Create a prompt for comprehensive psychological profile.
    
    Args:
        all_color_data (dict): Dictionary containing all color preference data
        
    Returns:
        str: Formatted prompt for comprehensive profile analysis
    """
    # Convert the dictionary to a formatted string
    data_str = '\n'.join([f"{k}: {v}" for k, v in all_color_data.items()])
    
    return format_prompt(
        PromptTemplates.COMPREHENSIVE_PROFILE,
        all_color_data=data_str
    )

def create_recommendations_prompt(profile_summary):
    """
    Create a prompt for personalized recommendations.
    
    Args:
        profile_summary (str): Summary of the psychological profile
        
    Returns:
        str: Formatted prompt for recommendations
    """
    return format_prompt(
        PromptTemplates.RECOMMENDATIONS,
        profile_summary=profile_summary
    )

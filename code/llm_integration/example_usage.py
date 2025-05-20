"""
Example usage of the LLM Integration Framework

This script demonstrates how to use the LLM Integration Framework
for the Psycho-Color Analysis system.
"""

import json
from llm_integration import LLMFramework

def main():
    """
    Demonstrate the usage of the LLM Integration Framework.
    """
    # Initialize the LLM Framework
    # In a production environment, you would provide an actual API key
    framework = LLMFramework(api_key="your_api_key_here")
    
    # Example color preference data
    color_data = {
        "primary_color": "Blue",
        "secondary_color": "Green",
        "least_preferred_color": "Orange",
        "work_color": "Blue",
        "relaxation_color": "Green",
        "social_color": "Purple",
        "creative_color": "Yellow",
        "stress_color": "White"
    }
    
    # Example color ranking
    color_ranking = ["Blue", "Green", "Purple", "Yellow", "Red", "Pink", "Black", "White", "Orange", "Brown"]
    
    # Analyze color preferences
    preference_analysis = framework.analyze_color_preferences(color_data)
    print("Color Preference Analysis:")
    print(json.dumps(preference_analysis, indent=2))
    print("\n" + "-"*50 + "\n")
    
    # Analyze Jung's Color Energy
    jung_analysis = framework.analyze_jung_color_energy(color_ranking)
    print("Jung's Color Energy Analysis:")
    print(json.dumps(jung_analysis, indent=2))
    print("\n" + "-"*50 + "\n")
    
    # Generate comprehensive profile
    profile = framework.generate_comprehensive_profile(color_data)
    print("Comprehensive Profile:")
    print(json.dumps(profile, indent=2))
    print("\n" + "-"*50 + "\n")
    
    # Generate recommendations
    profile_summary = "Individual with primary Cool Blue energy and secondary Earth Green energy. Analytical, detail-oriented, and values harmony."
    recommendations = framework.generate_recommendations(profile_summary)
    print("Recommendations:")
    print(json.dumps(recommendations, indent=2))

if __name__ == "__main__":
    main()

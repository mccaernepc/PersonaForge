import json
import random

def generate_persona():
    """Generates a basic persona with random attributes."""

    categories = ["Legal", "Medical", "Auto Repair", "Business", "Finance", "Marketing", "Technology", "Education"]
    category = random.choice(categories)

    # For now, we'll just use a placeholder for sub_category
    sub_category = "Placeholder" 

    core_attributes = {
        "name": "John Doe",  # We'll use a placeholder name for now
        "age": random.randint(25, 60),
        "description": "A generic persona description.",
        "personality_traits": {
            "openness": random.choice(["High", "Low"]),
            "conscientiousness": random.choice(["High", "Low"]),
            "agreeableness": random.choice(["High", "Low"]),
            "neuroticism": random.choice(["High", "Low"])
        },
        "motivations": ["Placeholder motivation"],
        "background": {
            "education": "Placeholder education",
            "life_experiences": "Placeholder life experiences"
        },
        "skills": ["Placeholder skill"]
    }

    category_specific_attributes = {}  # Empty for now

    persona = {
        "category": category,
        "sub_category": sub_category,
        "core_attributes": core_attributes,
        "category_specific_attributes": category_specific_attributes
    }

    return persona

def main():
    """Generates a specified number of personas and saves them to a JSON file."""

    num_personas = 5  # Change this to generate more or fewer personas
    personas = []
    for _ in range(num_personas):
        personas.append(generate_persona())

    with open("personas.json", "w") as f:
        json.dump(personas, f, indent=4)

if __name__ == "__main__":
    main()

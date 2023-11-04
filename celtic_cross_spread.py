import os
import random
import google.generativeai as palm
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

# Define your API key as a constant
API_KEY = os.getenv("PaLM_API_KEY")

# Check if the API key is provided
if not API_KEY:
    print("Please provide your PaLM API key.")
    exit(1)

# Configure the API with your API key
palm.configure(api_key=API_KEY)

# List available models and select the one with 'generateText' method
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]

if not models:
    print("No models with 'generateText' method found.")
    exit(1)

model = models[0].name

# List of tarot card names
tarot_cards = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgment", "The World", "Ace of Wands", "Two of Wands", "Three of Wands",
    "Four of Wands", "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands",
    "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands",
    "King of Wands", "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups",
    "Five of Cups", "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups",
    "Ten of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups",
    "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords",
    "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords",
    "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords",
    "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles",
    "Five of Pentacles", "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles",
    "Nine of Pentacles", "Ten of Pentacles", "Page of Pentacles", "Knight of Pentacles",
    "Queen of Pentacles", "King of Pentacles"
]

def generate_random_tarot_cards(num_cards=10):
    return random.sample(tarot_cards, num_cards)

def generate_celtic_cross_reading(cards):
    positions = [
        "Your current situation",
        "Obstacles or challenges",
        "Potential opportunities",
        "Foundation of the situation",
        "The past",
        "The future",
        "Your attitude towards the situation",
        "Other people’s attitudes",
        "Your hopes and fears",
        "The likely outcome"
    ]

    console = Console()
    console.print()
    table = Table(title="Celtic Cross Tarot Spread Reading")
    table.add_column("Position", style="bold")
    table.add_column("Card")

    for i, position in enumerate(positions):
        table.add_row(f"{position + ':':<30}", cards[i])  # Left-align the position label with padding

    console.print(table)

    # Use f-strings to create the prompt
    prompt = f"Celtic Cross Tarot Spread Reading:\n\n"
    
    for i, position in enumerate(positions):
        prompt += f"\n{position}: {cards[i]}"  # Newline before each position label

    prompt += """\nProvide insights and guidance based on these cards in the tarot world. 
    In addition, please provide a summary and one thing to be grateful for according to the cards.
    """

    try:
        # Generate text
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0.7,  # You can adjust the temperature for more varied responses
            max_output_tokens=10000,
        )
        
        console.print()
        print("\nGenerated Celtic Cross Tarot Reading:\n")
        #print(completion.result)

        text = Markdown(completion.result)
        console.print(text)

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    
    console = Console()
    console.print("\nCeltic Cross Layout:\n")
    console.print("        ---                   ---- ")
    console.print("       | 3 |                 | 10 |")
    console.print("        ---                   ---- ")
    console.print("  ---   ---    ---    ---     ---  ")
    console.print(" | 5 | | 1 |--| 2 |  | 6 |   | 9 | ")
    console.print("  ---   ---    ---    ---     ---  ")
    console.print("        ---                   ---  ")
    console.print("       | 4 |                 | 8 | ")
    console.print("        ---                   ---  ")
    console.print("                              ---  ")
    console.print("                             | 7 | ")
    console.print("                              ---  ")
    console.print("Remember the two is placed sideways on top of the one")

    # Check if the user wants to generate random tarot cards
    choice = input("Do you want to generate random tarot cards (y/n)? ").strip().lower()
    
    if choice == 'y':
        num_cards = 10  # You can change this to the number of cards you want
        random_cards = generate_random_tarot_cards(num_cards)
        print(f"Randomly generated tarot cards: {', '.join(random_cards)}")
        generate_celtic_cross_reading(random_cards)
    else:
        generate_celtic_cross_reading([])

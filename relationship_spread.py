import os
import google.generativeai as palm
import random
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
import pprint

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

def generate_random_tarot_cards(num_cards):
    return random.sample(tarot_cards, num_cards)

def generate_relationship_tarot_reading(cards):
    console = Console()
    
    # Create a table for the tarot cards and positions
    print()
    table = Table(title="Relationship Tarot Card Reading")
    table.add_column("Position", style="bold")
    table.add_column("Card")

    # Define the positions and their meanings
    positions = [
        "How you view your partner",
        "How your partner views you",
        "Your needs",
        "Your partners needs",
        "Current state of relationship",
        "The path you would like your relationship to follow",
        "The path your partner would like to see your relationship follow",
        "Aspects of your relationship to consider",
        "Question outcome (if theres a question)"
    ]

    for i, position in enumerate(positions):
        if i < len(cards):
            table.add_row(f"{position}:", cards[i])
        else:
            table.add_row(f"{position}:", "No card provided")

    console.print(table)
    
    # Use f-strings to create the prompt
    card_list = ', '.join(cards)
    prompt = f"""\n
    Provide insights and guidance based on these cards in the tarot world. The cards are """ + card_list + """.
    Please use the rider-waite interpretation of the spreads. This is the relationship spread.
    In addition, please provide a summary and one thing to be grateful for according to the cards.
    """
    
    try:
        # Generate text
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0.9,
            max_output_tokens=10000,
        )
        
        console.print()
        console.print("\n[bold magenta]Relationship Tarot Reading:[/bold magenta]")
        console.print()
        
        # Format the generated text as Markdown style
        markdown_output = Markdown(completion.result)
        console.print(markdown_output)

    except Exception as e:
        console.print(f"Error: {str(e)}")

if __name__ == "__main__":

    console = Console()
    console.print("\n[bold magenta]The Relationship Spread Layout:[/bold magenta]\n")
    console.print("         ---   ")
    console.print("        | 9 |  ")
    console.print("         ---   ")
    console.print("   ---   ---   ---   ---    ")
    console.print("  | 5 | | 6 | | 7 | | 8 |   ")
    console.print("   ---   ---   ---   ---    ")
    console.print("         ---   ")
    console.print("        | 4 |  ")
    console.print("         ---   ")
    console.print("         ---   ")
    console.print("        | 3 |  ")
    console.print("         ---   ")
    console.print("         ---   ")
    console.print("        | 2 |  ")
    console.print("         ---   ")
    console.print("         ---   ")
    console.print("        | 1 |  ")
    console.print("         ---   ")

    # Check if the user wants to generate random cards or enter their own
    print()
    choice = input("Do you want to generate random tarot cards (y/n)? ").strip().lower()
    console = Console()
    
    if choice == 'y':
        num_cards = 9  # Nine cards for The Relationship Spread
        random_cards = generate_random_tarot_cards(num_cards)
        console.print(f"Randomly generated tarot cards: {', '.join(random_cards)}")
        generate_relationship_tarot_reading(random_cards)
    else:
        user_cards = input("Enter your seven tarot cards (comma-separated): ").strip().split(',')
        generate_relationship_tarot_reading(user_cards)


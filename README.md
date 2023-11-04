# TarotBytes
Performs tarot readings using PaLM, Google's large language model.

## Spreads 

### The Three-Card Spread
The Three-Card Tarot Spread is a fundamental and widely used layout in tarot card reading. It consists of drawing three cards from the tarot deck and arranging them in a row. Each card in this spread has a specific significance:

The First Card: This card represents the past and provides insight into the events, influences, or circumstances that have led up to the current situation or question.

The Second Card: This card represents the present and offers guidance or insights into the current state of affairs or the energies surrounding the situation.

The Third Card: This card represents the future and provides glimpses into potential outcomes, paths, or developments based on the current circumstances and choices made.

### The Celtic Cross
The Celtic Cross Tarot Spread is a complex and in-depth layout that provides a comprehensive view of a situation or question. It consists of ten cards arranged in a specific pattern, and each card has a unique role:

1.  The First Card (The Significator): This card represents the person or situation in question and is placed in the center of the spread.
    
2.  The Second Card (The Crossing Card): This card is laid across the first card and represents challenges or obstacles the individual or situation is facing.
    
3.  The Third Card (The Foundation): This card represents the past influences or events that have led to the current situation.
    
4.  The Fourth Card (The Recent Past): This card sheds light on recent events or influences that are affecting the present.
    
5.  The Fifth Card (The Crown): This card represents the current state of affairs and what is currently on the individual's mind.
    
6.  The Sixth Card (The Near Future): This card provides insights into the near future and what is likely to occur in the coming weeks or months.
    
7.  The Seventh Card (The Self): This card reflects the individual's attitude, feelings, and approach to the situation.
    
8.  The Eighth Card (External Influences): This card signifies external factors, such as people or events, that may impact the situation.
    
9.  The Ninth Card (Hopes and Fears): This card reveals the individual's hopes, fears, or expectations regarding the outcome.
    
10.  The Tenth Card (The Outcome): This final card offers insights into the potential outcome of the situation based on current circumstances and choices made.

## How to use
Note: These instructions are for a MAC
1. Create an PaLM API key [PaLM API Key Generator](https://developers.generativeai.google/tutorials/setup)
 2.  Add this key to your bash_profile
    
   $ `vi ~/.bash_profile`

   $ `export PaLM_API_KEY='your-api-key-here'`
   
   $ `source ~/.bash_profile`

2. Set up your environment
	1. Install the latest version of python [python website](https://www.python.org/downloads/)
	2. Set up a virtual environment (optional)
    
		$ `python -m venv PaLM-env`

		$ `source PaLM-env/bin/activate`

3. Install the PaLM library
   
	$ `pip install -q google-generativeai`

5. Install the python rich library for pretty outputs [rich library](https://github.com/Textualize/rich)

	$ `python -m pip install rich`

7.  Now choose your desired spread.
		
	For a three-card reading:

	$ `python3 three_card_spread.py`

	For a celtic cross reading:

	$ `python3 celtic_cross_spread.py`

	The code will show you how to layout your cards in the correct position for the spread and then will ask if you want to your own tarot cards or randomly generated ones. 
	The output is your very own tarot reading.

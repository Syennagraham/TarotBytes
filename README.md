# TarotBytes
Performs tarot readings using PaLM, Google's large language model.

## Spreads 

### The Three-Card Spread
The Three-Card Tarot Spread is a fundamental and widely used layout in tarot card reading. It consists of drawing three cards from the tarot deck and arranging them in a row. Each card in this spread has a specific significance:

The First Card: This card represents the past and provides insight into the events, influences, or circumstances that have led up to the current situation or question.

The Second Card: This card represents the present and offers guidance or insights into the current state of affairs or the energies surrounding the situation.

The Third Card: This card represents the future and provides glimpses into potential outcomes, paths, or developments based on the current circumstances and choices made.

### The Celtic Cross

The Celtic Cross Tarot Spread is a complex and comprehensive layout in tarot card reading, consisting of ten cards arranged in a specific pattern. Each card in this spread has a distinct significance:

1. Your Current Situation: This card represents your present circumstances or the central issue you're facing, providing insight into what's currently happening in your life.

2. Obstacles or Challenges: This card highlights potential hurdles, difficulties, or obstacles that you may encounter as you navigate your current situation.

3. Potential Opportunities: This card reveals opportunities or positive aspects that can arise from your current circumstances, offering guidance on how to make the most of them.

4. Foundation of the Situation: This card delves into the underlying factors or roots of your situation, helping you understand the core elements at play.

5. The Past: This card offers insights into past events or influences that have contributed to your current situation, shedding light on how you got here.

6. The Future: This card provides glimpses into potential outcomes and developments based on your current path and choices.

7. Your Attitude Towards the Situation: This card reflects your attitude, feelings, or approach to the situation, helping you understand your own perspective.

8. Other People’s Attitudes: This card explores how others may perceive or influence the situation, offering insights into external perspectives or influences.

9. Your Hopes and Fears: This card reveals your hopes and fears related to the situation, helping you acknowledge and address your inner desires and concerns.

10. The Likely Outcome: This final card provides an indication of the most probable outcome or resolution based on the current circumstances and choices made.


### Relationship Spread
The Relationship Spread, often based on the 9-card Rider-Waite spread, is a specialized layout designed to provide insights into the dynamics of a romantic relationship or partnership. Each card in this spread has a specific role:

 1. How You View Your Partner: This card reflects your perspective on
    your partner and how you perceive them in the relationship.
    
 2. How Your Partner Views You: This card represents your partner's
    perspective on you and their perception of your role in the
    relationship.
    
   3. Your Needs: This card reveals your emotional, physical, or
    psychological needs within the relationship.
    
4. Your Partner's Needs: This card shows your partner's needs, desires,
    or expectations within the relationship.
    
5. Current State of Relationship: This card provides insights into the
    present state of your relationship, including its strengths and
    challenges.
    
6. The Path You Would Like Your Relationship to Follow: This card
    indicates your desires and intentions for the future of the
    relationship.
    
7. The Path Your Partner Would Like to See Your Relationship Follow:
    This card represents your partner's hopes and aspirations for the
    future of the relationship.
    
8. Aspects of Your Relationship to Consider: This card highlights
    important aspects or themes within your relationship that you should
    pay attention to.
    
9. Question Outcome (If There's a Question): If you have a specific
    question or concern related to the relationship, this card provides
    guidance or an answer.

The Relationship Spread is a valuable tool for gaining a deeper understanding of the dynamics between you and your partner. It can help identify areas of alignment and potential areas for growth or improvement. This spread can be particularly useful for those seeking clarity and guidance in their romantic relationships or partnerships.


## How to use
Note: These instructions are for a MAC and are perfomed in the MAC terminal 
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

7.  Choose your desired spread
		
	For example, a three-card reading:

	$ `python3 three_card_spread.py`

	The code will show you how to layout your cards in the correct position for the spread and then will ask if you want to your own tarot cards or randomly generated ones. 	
	
	The output is your very own tarot reading.

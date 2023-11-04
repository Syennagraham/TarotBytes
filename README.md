# TarotBytes
Performs tarot readings using PaLM, Google's large language model.

## Spreads 

### The Three-Card Spread
The Three-Card Spread is a simple yet versatile tarot card layout that involves drawing three cards from the deck and arranging them in a row. Each card in this spread signifies the past, present, or future, providing quick and focused insights into a situation or question. It's an excellent choice for both beginners and experienced readers, offering a concise snapshot of key influences and potential outcomes.
| Card Number   | Significance                                            | Description                                                                                                 |
| ------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1             | The First Card (Past)                                  | Represents the past and provides insight into the events, influences, or circumstances leading to the current situation or question. |
| 2             | The Second Card (Present)                             | Represents the present and offers guidance or insights into the current state of affairs or the energies surrounding the situation. |
| 3             | The Third Card (Future)                               | Represents the future and provides glimpses into potential outcomes, paths, or developments based on the current circumstances and choices made. |


### The Celtic Cross
The Celtic Cross Tarot Spread is a renowned and comprehensive layout consisting of ten cards arranged in a specific pattern. It provides deep insights into complex situations, addressing various aspects of a question or situation, including the past, present, future, internal and external influences, perspectives, and potential outcomes. It is a versatile tool widely used for personal growth, relationship matters, career decisions, and spiritual guidance.

| Card Number   | Significance                                          | Description                                                                                                   |
| ------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 1             | Your Current Situation                               | Represents your present circumstances or the central issue you're facing, offering insight into what's currently happening in your life. |
| 2             | Obstacles or Challenges                              | Highlights potential hurdles, difficulties, or obstacles that you may encounter as you navigate your current situation. |
| 3             | Potential Opportunities                               | Reveals opportunities or positive aspects that can arise from your current circumstances, providing guidance on how to make the most of them. |
| 4             | Foundation of the Situation                           | Delves into the underlying factors or roots of your situation, helping you understand the core elements at play. |
| 5             | The Past                                             | Offers insights into past events or influences that have contributed to your current situation, shedding light on how you got here. |
| 6             | The Future                                           | Provides glimpses into potential outcomes and developments based on your current path and choices. |
| 7             | Your Attitude Towards the Situation                   | Reflects your attitude, feelings, or approach to the situation, aiding in understanding your own perspective. |
| 8             | Other People’s Attitudes                             | Explores how others may perceive or influence the situation, offering insights into external perspectives or influences. |
| 9             | Your Hopes and Fears                                 | Reveals your hopes and fears related to the situation, helping you acknowledge and address your inner desires and concerns. |
| 10            | The Likely Outcome                                   | This final card provides an indication of the most probable outcome or resolution based on the current circumstances and choices made. |


### Relationship Spread
The Relationship Spread, often based on the 9-card Rider-Waite spread, is a specialized layout designed to provide insights into the dynamics of a romantic relationship or partnership. Each card in this spread has a specific role:

| Card Number   | Significance                                          | Description                                                                                                           |
| ------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1             | How You View Your Partner                             | Reflects your perspective on your partner and how you perceive them in the relationship.                                |
| 2             | How Your Partner Views You                            | Represents your partner's perspective on you and their perception of your role in the relationship.                   |
| 3             | Your Needs                                           | Reveals your emotional, physical, or psychological needs within the relationship.                                      |
| 4             | Your Partner's Needs                                 | Shows your partner's needs, desires, or expectations within the relationship.                                          |
| 5             | Current State of Relationship                         | Provides insights into the present state of your relationship, including its strengths and challenges.                 |
| 6             | The Path You Would Like Your Relationship to Follow   | Indicates your desires and intentions for the future of the relationship.                                               |
| 7             | The Path Your Partner Would Like to See Your Relationship Follow | Represents your partner's hopes and aspirations for the future of the relationship.                    |
| 8             | Aspects of Your Relationship to Consider              | Highlights important aspects or themes within your relationship that you should pay attention to.                     |
| 9             | Question Outcome (If There's a Question)              | If you have a specific question or concern related to the relationship, this card provides guidance or an answer.     |



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

4. Install the python rich library for pretty outputs [rich library](https://github.com/Textualize/rich)

	$ `python -m pip install rich`

5.  Clone this repo onto your computer

	$`git clone https://github.com/Syennagraham/TarotBytes.git`
	
7. Navigate into the repo and choose your desired spread
		
	For example, a three-card reading:
	
	$ `python3 three_card_spread.py`

	The code will show you how to layout your cards in the correct position for the spread and then will ask if you want to your own tarot cards or randomly generated ones. 	
	
	The output is your very own tarot reading.


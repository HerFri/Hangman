# Hangman Game

Visit the deployed application on [Heroku](https://hangman-by-herfri-1d96d392125d.herokuapp.com/)

Hangman is a terminal based game where players compete against the computer by guessing the right letters of a random word chosen by the computer. Within six tries, players have to guess all letters of the word to win the game. When the game is started, for each letter of the word an underscore ( _ ) is displayed. When the player guesses a letter that is included in the word, the respective underscore is replaced by the correctly guessed letter. For every wrong letter guessed, the player loses one try and an additional bodypart of the hangman is displayed on the rope. When all six tries have been used by the player, the final stage of the hanging man is displayed and the game is lost.

## User Experience
# User Stories
* As a new player who never played the game before, I want to learn the rules of the game by reading easily understandable instructions.
* As a player, I want to find understandable instructions, providing information on how to start the game or read the rules
* As a player, I want to find interactive elements, like buttons, that allow me to restart the application whenever I feel like it
* As a player, I want to be informed what input is needed to play the game correctly
* As a player, I want to receive a notification when my input is not valid

# Preplanning and Structure
For a comprehensible visualization of the application structure I made this flowchart on the [Lucidchart website](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20chart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=kwd-55720648523&km_CPC_Country=9044294&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjw84anBhCtARIsAISI-xdxDXtOxQFpn7lv1WJ7UmkNvllJ2ZjPF05InfeNfMNl2-dFll3VTHEaAsT0EALw_wcB):

![flowchart](https://github.com/HerFri/hangman/blob/main/readmeimages/flowchart.png?raw=true)

## Features
# Terminal Landing Page
![landingpage](https://github.com/HerFri/hangman/blob/main/readmeimages/landingpage.PNG?raw=true)

By visiting the Heroko website that was used to deploy the application, the first thing that is displayed to the user is the terminal landing page. By entering the side, the application is initialized and waits for the input of the user. On the very top is the ´RUN PROGRAM´ button that allows to restart the application at any time. On the top of the terminal the running startup command is displayed that runs the code of the application. Under the ASCII art that displays the title  'Hangman' and a stick figure hanging on a rope, the user finds a text that greets visiting users and asks, if the game wants to be played, which can be answered by typing in ´Y´ for Yes and ´N´ for No. The input here is not case-sensitive. Moreover, if users do not know the rules of the game, the text suggests to type in ´R´ to display the rules of the game. By typing in different letters or characters other than ´Y´, ´N´ or ´Y´ , like ´F´, and pressing the enter key, a message will be displayed that points out that an invalid answer has been typed in, followed by the display of the same display of ASCII art and text like in the beginning when starting the application, which gives once again opportunity to the user to provide a valid input:

![wronganswer](https://github.com/HerFri/hangman/blob/main/readmeimages/wronganswer.PNG?raw=true)

# Rules
![rules]

By giving the input of ´R´, the rules of the game are presented to the user. At the end, the user is asked, if he or she is ready to play, which can be answered by the input of ´Y´ for Yes and ´N´ for No. Once again, if invalid input is provided, the user will be shown an error message, followed by the same question asking if the user is ready to play:

![notvalidanswer]

By giving the input of ´N´ for No, the 
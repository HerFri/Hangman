# Hangman Game

Visit the deployed application on [Heroku](https://hangman-by-herfri-1d96d392125d.herokuapp.com/)

Hangman is a terminal based game where players compete against the computer by guessing the right letters of a random word chosen by the computer. Within six tries, players have to guess all letters of the word to win the game. When the game is started, for each letter of the word a underscore ( _ ) is displayed. When the player guesses a letter that is included in the word, the respective underscore is replaced by the correctly guessed letter. For every wrong letter guessed, the player loses one try and an additional bodypart of the hangman is displayed on the rope. When all six tries have been used by the player, the final stage of the hanging man is displayed and the game is lost.

# User Experience
## User Stories
* As a new player who never played the game before, I want to learn the rules of the game by reading easily understandable instructions
* As a player, I want to find understandable instructions, providing information on how to start the game or read the rules
* As a player, I want to find interactive elements, like buttons, that allow me to restart the application whenever I feel like it
* As a player, I want to be informed what input is needed to play the game correctly
* As a player, I want to be informed when my input is not valid
* As a player, I want to enjoy a fun little game

# Preplanning and Structure
For a comprehensible visualization of the application structure I made this flowchart on the [Lucidchart website](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20chart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=kwd-55720648523&km_CPC_Country=9044294&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjw84anBhCtARIsAISI-xdxDXtOxQFpn7lv1WJ7UmkNvllJ2ZjPF05InfeNfMNl2-dFll3VTHEaAsT0EALw_wcB):

![flowchart](https://github.com/HerFri/hangman/blob/main/readmeimages/flowchart.png?raw=true)

# Features
## Terminal Landing Page
![landingpage](https://github.com/HerFri/hangman/blob/main/readmeimages/landingpage.PNG?raw=true)

By visiting the Heroko website that was used to deploy the application, the first thing that is displayed to the user is the terminal landing page. By entering the side, the application is initialized and waits for the input of the user. On the very top is the `RUN PROGRAM` button that allows to restart the application at any time. On the top of the terminal the running startup command is displayed that runs the code of the application. Under the ASCII art that displays the title  'Hangman' and a stick figure hanging on a rope, the user finds a text that greets visiting users and asks, if the game wants to be played, which can be answered by typing in `Y` for Yes and `N` for No. The input here is not case-sensitive. Moreover, if users do not know the rules of the game, the text suggests to type in `R` to display the rules of the game. By typing in different letters or characters other than `Y`, `N` or `Y` , like `F`, and pressing the enter key, a message will be displayed that points out that an invalid answer has been typed in, followed by the display of the same display of ASCII art and text like in the beginning when starting the application, which gives once again opportunity to the user to provide a valid input:

![wronganswer](https://github.com/HerFri/hangman/blob/main/readmeimages/wronganswer.PNG?raw=true)

## Game Rules
![rules](https://github.com/HerFri/hangman/blob/main/readmeimages/rules.PNG?raw=true)

By giving the input of `R`, the rules of the game are presented to the user. At the end, the user is asked, if he or she is ready to play, which can be answered by the input of `Y` for Yes and `N` for No. Once again, if invalid input is provided, the user will be shown an error message, followed by the same question asking if the user is ready to play:

![notvalidanswer](https://github.com/HerFri/hangman/blob/main/readmeimages/notvalidanswer.PNG?raw=true)

By giving the input of `N` for No, a message is displayed that the execution of the program ends and that the application can be restarted by pressing the `RUN PROGRAM` button above: 

![answerno](https://github.com/HerFri/hangman/blob/main/readmeimages/answerno.PNG?raw=true)

By giving the input of `Y` for Yes, the game is started and the player can start guessing a letter.

## Playing the Game

When the player agrees to play the game, the game starts and the program picks a random word from the wordlist provided in the code. For each letter of the word a underscore is displayed. Under the underscores, the player can see how many tries he or she has left and is asked to type in a letter for the first guess. 

![startgame](https://github.com/HerFri/hangman/blob/main/readmeimages/startgame.PNG?raw=true)

By providing invalid inputs and inputs that are not usual letters of the English alphabet, like numbers or 'umlauts', the player receives an error message:

![error](https://github.com/HerFri/hangman/blob/main/readmeimages/error.PNG?raw=true)

When providing valid input, the application checks if the letter is in the random chosen word or not. When the guess is correct, the player receives a positive feedback message that states that the guessed letter is in the secret word. The guessed letter will then be revealed in all positions the letter is found in the secret word and the respective underscores disappear. Moreover, from now on, all guessed letters will be displayed in alphabetical order right under the counter of the tries the player has left:

![correctguess](https://github.com/HerFri/hangman/blob/main/readmeimages/correctguess.PNG?raw=true)

As long as the player has at least one try left, the application will ask the player to guess another letter. If the guessed letter is not in the word, a message that states this will be printed out and the hangman stage will be displayed, depending on how many letters the player already guessed incorrectly. In the following screenshot the player guessed a letter the first time incorrectly:

![incorrectguess](https://github.com/HerFri/hangman/blob/main/readmeimages/incorrectguess.PNG?raw=true)

When the player used all tries and there are still letters to be guessed, the game is lost and the hanging man is displayed. A ASCII art display of 'You lost!' is displayed, followed by a text, stating that the game is lost and revealing the secret word. Moreover, the player is asked, if she or he wants to play again, which can be answered by the input of `Y` for Yes and `N` for No. Just like in the instances before, by providing an invalid input that is not `Y` or `N`, the player receives an error message that the provided input is not a valid answer. By answering `Y`, a new round of the game is started. By answering `N`, a message is displayed that the execution of the program ends and that the application can be restarted by pressing the `RUN PROGRAM` button above. In the following screenshots the player won the game and decided to play another round of Hangman. The message 'Let's play another round!' informs the player that a new round has been started. Note how when winning the game not all body parts in the hangman display are shown and the ASCII art display differs from when losing the game:

![playerwins](https://github.com/HerFri/hangman/blob/main/readmeimages/playerwins.PNG?raw=true)
![startnewround](https://github.com/HerFri/hangman/blob/main/readmeimages/startnewround.PNG?raw=true)

# Testing
# Code Institute Python Linter Testing
After breaking the lines for some print statements and comments that had more than 80 characters in one line, the linter showed no more errors:

![linterresults](https://github.com/HerFri/hangman/blob/main/readmeimages/linterresults.PNG?raw=true)

## Manual Testing


## Testing User Stories
| As a new player who never played the game before, I want to learn the rules of the game by reading easily understandable instructions | As a new player, I can read the rules at the beginning of the game. The rules are written in a very easily understandable manner.                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a player, I want to find understandable instructions, providing information on how to start the game or read the rules              | As a player, the terminal based application is always providing sufficient instructions what inputs are needed to execute certain actions, like starting the game or reading the rules |
| As a player, I want to find interactive elements, like buttons, that allow me to restart the application whenever I feel like it       | As a player, I can find the button 'RUN PROGRAM' to restart the application whenever I feel like it                                                                                    
| As a player, I want to be informed what input is needed to play the game correctly                                                     | The application is always providing sufficient instructions what inputs are needed to play the game correctly and informs when an input is not correct
| As a player, I want to be informed when my input is not valid. | The application is always informing the player when an invalid input has been provided 
| As a player, I want to enjoy a fun little game                 | As a player, I can enjoy a fun little game                                             
|                                                                |                                                                                        
|                                                                |                                                                                             
# Bugs
## Resolved Bugs
Before deploying the final application, users were able to give inputs of characters longer than one character and other invalid inputs like numbers and 'umlauts'. I fixed this issue by adding if conditions including error messages in the code that, that will not allow and inform the user about the invalid input:

![ifconditions](https://github.com/HerFri/hangman/blob/main/readmeimages/ifconditions.PNG?raw=true)


## Unresolved Bugs
No unresolved bugs remain.

# Technologies used 
Following technologies have been used for my application:
* Visual Studio Code for writting the code
* GitHub for version control
* Heroku for deploying the application

# Deployment
Following steps were undertaken to deploy the application on Heroku:
* Create a new account, log in and create a new application by clicking `New` --> `Create new app` in the dashboard.
* Find a unique name for the app, select region and press `Create app`
* Go to `Settings` --> `Config Vars.` and add following values: `PORT`:`8000`, `KEY`: `VALUE`
* Add buildpacks in following order: `Python` and `NodeJS`
* Go to `Deploy` --> `Deployment method`, connect GitHub account to Heroku and select the correct repository of the project in GitHub
* Go to `Manual deploy`, select the branch the project was worked on and click `Deploy Branch`

# Credits
# Acknowledegments
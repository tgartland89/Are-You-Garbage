# Flatiron Phase 3 CLI Project- Are you Garbage? 

## About the Game?

Are you Garbage is a CLI mini game based on the popular podcast hosted by comedians H.Foley and Kevin Ryan. 
Each week they sit down with guests and ask them a series of questions to determine if they are "Classy", "Trashy", or "Garbage" 
The game is in the name of fun even with some wild questions and in this version, players have a bit more simplified process. 

## Dependencies

The following dependencies are required to run the game:

- ipdb
- sqlalchemy
- alembic

Make sure you have these dependencies installed before running the game.

## Installation: 

- Clone the repository: "git clone git@github.com:GH userid/Are-You-Garbage.git"
- Change into the project directory: "cd are-you-garbage"
- Change into the lib/db directory: "cd lib/db” 
- Install the required dependencies using pipenv: "pipenv install"
- Activate the virtual environment: "pipenv shell" 
- Once in the pipenv shell, enter command "cli.py start (Your Name)", hit enter and the game will start. 
- To play the game you answer the 10 "yes or no" questions to generate 1 of 3 results 
- After the quiz, you can add a question to the game that could come up in the next round for a new player. 

## How to get add your question to the next round: 

-  If you chose to enter a question, remember to make it Yes or No.
-  Once you've entered the question, run "python seed.py" in your terminal to seed that question into the questions table, making it playable for the next round! 

## Resources used to build this project 
-  Flatiron School - Sign up. (n.d.). Flatiron School. https://learning.flatironschool.com/courses/6444/pages/intro-to-sql?module_item_id=574902
-  Flatiron School - Sign up. (n.d.-b). Flatiron School. https://learning.flatironschool.com/courses/6444/pages/intro-to-table-relations-in-sql? module_item_id=574917
-  Flatiron School - Sign up. (n.d.-c). Flatiron School. https://learning.flatironschool.com/courses/6444/pages/mapping-database-records-to-python-objects?module_item_id=574928
 - Flatiron School - Sign up. (n.d.-d). Flatiron School. https://learning.flatironschool.com/courses/6444/pages/principles-of-object-oriented-design?module_item_id=574858
-  Are You Garbage, Official Online Store. (n.d.). Are You Garbage? | Official Website & Onine Store. https://areyougarbage.com/

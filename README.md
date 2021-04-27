# Quiz Game GUI
## OVERVIEW:
#### Maths Quiz game. It has 3 difficulties for the user to do the quiz. At the end of the quiz it will save the name, difficulty and score into an enternal .JSON file.
#### Another program is for the user to:
* view the rules
* change the rules
* view the results of the pupils

## SPECIFICATION:


### [MAIN](https://github.com/ilhamhoque/quiz-game-gui/blob/main/main.py): 

1. the pupils must have the ability to enter their name before they start their Maths Quiz
2. the pupil must be able to choose the difficulty level of the quiz as "EASY", "STANDARD" or "HARD"
3. each Maths Quiz must consist of 10 questions
4. each arithmetic question during the Maths Quiz, should have two random numbers, which must be either added, subtracted or multiplied
5. the range of random numbers used within each question must be set according to difficulty
6. the pupil should be prompted to enter the correct answer for each question when asked; to a maximum number of attempts per question
7. the program should give the correct answer to a question if the pupil gets it wrong after all attempts
8. at the end of the Maths Quiz, the pupil should be told their score out of 10
9. the teacher would like to store the difficulty level and quiz results for each pupil, and have a way to view all of these results after the quizzes have been completed
10. menus choices should be used to help navigate the program.

### [Admin/Teacher's only](https://github.com/ilhamhoque/quiz-game-gui/blob/main/admin.py):

1. The admin can change the rules without changing the rules from source code.
2. The admin can View the Rules and Results of the users.
3. The Admin will be able to change the Range of values for each difficulties.
4. The Admin will be able to change how many questions from each operator but the questions must add upto 10.
5. The Admin will be able to change how many attempts a user can get for each difficulty.

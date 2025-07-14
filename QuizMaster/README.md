# 🧠 QuizMaster 

QuizMaster is a console-based application that lets you create, save, and solve multiple-choice quizzes. Each question includes 3 choices, one correct answer, and a difficulty level (easy, medium, or hard). You can generate custom quizzes based on difficulty and number of questions, and the program will calculate the score once the quiz is completed.

## 📌 Features
### 1.  Add Questions to the Master List
You can add questions to the master question list using:  
add < id >;< text >;<choice_a>;<choice_b>;<choice_c>;<correct_choice>;<difficulty>  
Where:
- `id`: unique numeric ID
- `difficulty`: one of `easy`, `medium`, or `hard`  

 Example: add 5;Which of the following numbers is prime?;5;56;75;5;easy

### 2.  Create Quiz
Generate a quiz from the master list:  
create <difficulty> <number_of_questions> <file>  
Where:
- `difficulty` = easy, medium, or hard  
- `number_of_questions` = how many questions to include  
- `file` = name of the file to save the quiz  

 Example: create easy 10 quiz1.txt

### 3.  Start Quiz
Start solving a quiz from a saved file:
- The program displays questions **one by one**, from **easiest to hardest**
- The user selects an answer and proceeds to the next question
- Answer options (a, b, c) are shown

### 4.  Finish & Scoring
Once all questions are answered:
- The user’s score is calculated:
  -  +1 point = correct answer to an *easy* question
  -  +2 points = correct answer to a *medium* question
  -  +3 points = correct answer to a *hard* question

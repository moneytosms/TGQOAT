# Quiz Application Documentation

Welcome to the **TGQOAT**! This application allows you to play a fun and interactive quiz with lifelines with local leaderboard tracking and userbase ! The core logic of the application resides in the `Main.py` file, while `Functionsq.py`, `GraphicsV2/`, and `Mysqlf.py` provide the necessary support for quiz functions, graphics, and database handling, respectively.

## Table of Contents

- [Installation Steps](#installation-steps)
- [Database Configuration](#database-configuration)
- [Folder Structure](#folder-structure)
- [Running the Quiz](#running-the-quiz)
- [Adding New Topics and Questions](#add-new-categories)
- [License](#license)

---

## Installation Steps
Before you start using the Quiz Application, you need to ensure that the necessary components are set up. Follow the steps below to get started:

### 1. Install MySQL Database

To run the application, the MySQL database is required to store and manage quiz questions. Follow these steps to set up MySQL:

- Download and install MySQL from [the official MySQL website](https://dev.mysql.com/downloads/installer/).
- During installation, make sure to install the MySQL Workbench and MySQL Server.
- After installation, set up a MySQL instance and make sure the server is running.

## Database Configuration

### 2. Configure MySQL Credentials

The `Mysqlf.py` file is responsible for interacting with the MySQL database. You need to configure the database connection in this file by setting the correct username and password.

1. Open the `Mysqlf.py` file.
2. Locate the section where the username and password are defined:
   ```python
   username = 'your_mysql_username'
   password = 'your_mysql_password'
   ```
3. Update these values with your MySQL credentials.

### 3. Install Required Libraries
Ensure that you have installed any necessary libraries or dependencies. If the project uses specific Python libraries for database or graphics handling, make sure to install them using `pip`.
```bash
pip install mysql-connector-python
pip install <other-libraries>
```

## Folder Structure
The application’s folders and files are organized as follows:
```bash
/TGQOAT
├── Main.py              # Main application logic (starting point for the quiz)
├── Functionsq.py        # Functions related to quiz logic
├── GraphicsV2/          # Folder containing graphical assets (including turtle graphics)
│   ├── graphics.py      # Support for quiz graphics
├── Mysqlf.py            # Database interaction for storing and retrieving quiz data
├── Questions/           # Folder containing quiz question files
│   ├── Computer_Q.txt
│   ├── Math_Q.txt
│   ├── Science_Q.txt
│   └── ...              # More question files
```
Important Notes:

- Graphics: The GraphicsV2/ folder contains the turtle code used for graphical interactions in the quiz. This includes any visual aspects of the quiz, like displaying questions, user interactions, etc.
- Questions: The quiz questions are stored in the Questions/ folder as text files like Computer_Q.txt, Math_Q.txt, etc. You can easily add new topics and questions by adding new text files to this folder.
**Please do not change the folder structure as the application relies on these paths to function correctly.**

## Running the Quiz
Once everything is set up, you can run the application and enjoy the quiz. Follow these steps:
1. Navigate to the Main.py file in your terminal or IDE.
2. Make sure the MySQL server is running.
3. Run the Main.py file to start the quiz:
```bash
python3 Main.py
```
4. The application will load the quiz and ask you a series of questions along with the instructions. Answer the questions and use the lifelines carefully to play the quiz and enjoy!
## How to Add More Topics and Questions

To expand the quiz with new categories or questions, follow these steps:

## Add New Categories and questions :
### 1. Adding New Categories
   - Open `Main.py` and locate the function `Category_Selector(c)` where categories are defined.
   - Add a new `if` condition for the new category you wish to add. For example, to add a "History" category, you could add:
     ```python
     if c == '6':
         category = "Questions/History_Q.txt"
     ```

   - This will create a new category option in the quiz that the user can select.

### 2. **Add Questions to Existing Categories**:
   - In the `aq()` function, after selecting a category, the user is prompted to enter a new question and the correct option.
   - The question is added to the appropriate text file in the `Questions/` folder.

### 3. **Add Questions Dynamically**:
To add new questions to a selected category:
- Run the `aq()` function.
- Select the category by entering the corresponding number.
- Enter the question and the correct option when prompted.
- The new question will automatically be appended to the appropriate category's text file.

### 4. **Editing or Deleting Questions**:
- Open the respective category text file inside the `Questions/` folder (e.g., `Math_Q.txt`).
- Modify or delete questions directly in the file. Each question and its correct answer are stored in the format:
  ```
  #Question:Answer
  ```
- To delete a question, simply remove the corresponding line from the file.

## How to Use the Lifelines

During the quiz, you can use one of three lifelines per question:
1. **50:50**: This lifeline will remove two incorrect options, leaving you with two possible answers.
2. **Audience Poll**: The audience provides their opinions on the most likely correct answer.
3. **Skip Question**: This option allows you to skip the current question without answering.

You can use only one lifeline per question.

## Conclusion

You can easily expand and customize the quiz by adding new topics and questions. By editing the respective text files and using the provided functions, you can make the quiz system more engaging and personalized. Enjoy playing and learning with the quiz!

Thank you for using TGQOAT !

## License
This project is licensed under the MIT License. See the LICENSE file for details

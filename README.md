---

# **The Greatest Quiz of All Time (TGQOAT)**

Welcome to **The Greatest Quiz Of All Time** (TGQOAT), a Python-based interactive quiz platform that combines learning with fun. This project uses **MySQL** for database management and incorporates **Turtle Graphics** for graphical elements, providing a comprehensive and engaging user experience.

---

## **Features**

- **User Management**: 
  - Registration and login functionality.
  - Profile management: View, update, or delete your profile.

- **Quiz Gameplay**:
  - Multiple categories: General Knowledge, Pop Culture, Mathematics, Science, and Computer Technology.
  - Lifelines and rules for a challenging experience.
  - Dynamic question selection and scoring.

- **Admin Functionality**:
  - View users and question database.
  - Add new questions to the quiz.

- **Leaderboard**:
  - Track and display high scores for competitive play.

---

## **Technologies Used**

- **Python**: Core programming language.
- **MySQL**: Database management for storing user profiles, questions, and scores.
- **Turtle Graphics**: Enhances the visual appeal of the game.
- **Time Module**: Adds pauses and delays for better user interaction.

---

## **Getting Started**

### Prerequisites

- Python 3.x installed.
- MySQL server installed and running.
- Required Python libraries:
  ```bash
  pip install mysql-connector-python
  ```

### Setup

Please visit [Documentation](Documentation.md) for detailed instructions on how to set this up.
---

## **How to Play**

1. **Choose to Register or Login**:
   - Register to create a new user profile.
   - Login with an existing profile.

2. **Admin Access**:
   - Use the password `admin` for admin privileges.
   - Admins can view or modify the question database and user table.

3. **Select a Quiz Category**:
   - Choose from five categories.
   - Answer questions and use lifelines wisely.

4. **View Leaderboard**:
   - Check your rank and compare scores with other players.

---

## **Game Rules**

1. **Lives and Lifelines**:
   - Start with 3 lives; incorrect answers deduct a life.
   - Use up to 3 lifelines during the game.

2. **Breaks**:
   - Take breaks after every 5 questions to secure your score.

3. **High Scores**:
   - Beat the highest score to become the champion.

---

## **Database Schema**

- **Users Table**:
  - Stores user information such as username, password, and scores.
- **Questions Table**:
  - Contains quiz questions categorized by topic.

---

Let me know if you'd like to customize this further!

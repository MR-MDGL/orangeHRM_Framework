# Selenium Data-Driven Testing Framework (My Project)

Hi! This is my automation testing project using Python, Selenium, and MySQL. I made this to learn how to do data-driven testing and automate web applications. Here's how it works and how you can run it too!

## What My Project Does

- I automate login and other features of the OrangeHRM demo site using Selenium.
- I use the Page Object Model (POM) for better code structure.
- I support data-driven testing with both Excel and MySQL database.
- I take screenshots if something goes wrong.
- I handle browser popups and alerts.

## How My Project Works

1. **Page Object Model (POM):**
   - I created separate Python classes for each page (like login, PIM, etc.) so my code is easy to manage.

2. **Data-Driven Testing:**
   - I can run tests with different usernames and passwords from an Excel file or directly from a MySQL database table.
   - My test reads each row from the database and tries to log in with those credentials.

3. **MySQL Integration:**
   - My test connects to a MySQL database (`orange_hrm`) and fetches test users from the `test_users` table.
   - I can set expected results for each user and my test will compare them with what actually happens.

4. **Error Handling:**
   - If login fails or a popup appears, my test handles it and saves a screenshot for me to check later.

## How I Set Up My Project

1. **Clone or Download the Project**
   - I put it anywhere on my computer.

2. **Install Requirements**
   - I make sure I have Python 3.8+ installed.
   - I install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - I use Chrome and ChromeDriver (or update the code for my browser).

3. **Set Up MySQL Database**
   - I create a database and table using these commands:
     ```sql
     CREATE DATABASE orange_hrm;
     USE orange_hrm;
     CREATE TABLE test_users (
         id INT AUTO_INCREMENT PRIMARY KEY,
         username VARCHAR(255) NOT NULL,
         password VARCHAR(255) NOT NULL,
         expected_result VARCHAR(10),
         actual_result VARCHAR(10)
     );
     -- Add my test users:
     INSERT INTO test_users (username, password, expected_result) VALUES
     ('Admin', 'admin123', 'PASS'),
     ('user1', 'admin123', 'FAIL'),
     ('user2', 'password2', 'FAIL');
     ```

4. **Configure the Project**
   - I edit `configuration/config.ini` to set the correct URL, username, and password for my OrangeHRM site.
   - I update MySQL credentials in the test files if needed.

5. **Run the Tests**
   - To run all tests:
     ```bash
     pytest
     ```
   - To run a specific test (like the SQL login test):
     ```bash
     pytest TestCases/login/test_login_sql.py
     ```
   - Screenshots for failed logins are saved in the project folder.

## What I Learned

- I learned how to use Selenium for web automation.
- I learned how to connect Python with MySQL and use real test data.
- I learned how to structure code using POM.
- I learned how to handle popups and errors in browser automation.

## Extra Notes

- I can add more test cases or pages by following the same structure.
- If I want to use Excel for data-driven testing, I check the `test_login_ddt.py` file.
- If I get stuck, I check the screenshots or the console output for errors.

---

Thanks for checking out my project! If you have any questions or want to see more, just ask!

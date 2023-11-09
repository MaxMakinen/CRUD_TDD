# CRUD_TDD

### FULL DISCLOSURE: 
I asked ChatGPT to give me an outline of how to plan a full-stack CRUD application that's tested using ROBOT framework and Jenkins. I asked for a plan usingg TDD methodologies.<br>
I will have the plan itself saved in a file called "the_plan.txt"<br>
The following is written by Chat-GPT as an example of a readme.

#### Full-Stack CRUD Application with Test-Driven Development

This project demonstrates my proficiency in building a full-stack CRUD application using JavaScript for the frontend and Python with Flask for the backend. The development process follows a Test-Driven Development (TDD) approach, ensuring the reliability and maintainability of the codebase.

### Features:

- **Frontend:**
  - Simple HTML, CSS, and JavaScript structure.
  - CRUD functionalities for managing items.
  - Test cases written using Jest for TDD.

- **Backend:**
  - Flask application handling API endpoints for CRUD operations.
  - SQLite database for data storage.
  - API tests written using pytest for TDD.

- **Testing:**
  - End-to-end testing using Robot Framework.
  - Jenkins integration for automated testing and continuous integration.

### Setup Instructions:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/full-stack-crud-app.git
   ```

2. Setup the frontend:

   ```bash
   cd full-stack-crud-app/frontend
   ```

   - Open `index.html` in your browser to interact with the application.

3. Setup the backend:

   ```bash
   cd ../backend
   ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Run the Flask application:

     ```bash
     python app.py
     ```

   - The backend will be running at `http://localhost:5000`.

4. Run tests:

   - Frontend tests:

     ```bash
     cd ../frontend
     npm test
     ```

   - Backend tests:

     ```bash
     cd ../backend
     pytest
     ```

   - Robot Framework tests:

     ```bash
     cd ../robot-framework-tests
     robot test-frontend.robot
     robot test-backend.robot
     ```

5. Jenkins Integration:

   - Configure a Jenkins job to pull and test the project. Refer to the Jenkinsfile for setup.

### License:

This project is licensed under the [MIT License](LICENSE).

### Conclusion:

This repository serves as a comprehensive demonstration of my skills in building a full-stack CRUD application, emphasizing best practices, testing, and continuous integration. Feel free to explore the code and test the application to witness the seamless integration between frontend and backend components. Your feedback is appreciated!

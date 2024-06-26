﻿# recipe-api
Recipe Application Enhancement for Production Deployment
Introduction:
We are upgrading our existing recipe application to ensure it's ready for production deployment. This task aims to evaluate your skills in software development, particularly in back-end development, DevOps practices, and asynchronous task handling.

Objective:
Enhance the functionality and reliability of the recipe application, preparing it for scalable and maintainable production deployment.

Requirements:
Docker Integration: Containerize the application using Docker for simplified deployment and consistency across environments.
Testing and Coverage Report: Write comprehensive test cases for all APIs and generate a coverage report to ensure robustness.
Asynchronous Task Handling with Celery: Integrate Celery to manage asynchronous tasks, particularly for background processing.
Email Queue Implementation: Build an email queue to send notifications asynchronously, including a daily notification to authors about the likes received on their recipes.
Logging Framework (Bonus): Implement a logging framework to capture and log execution details into files for debugging and monitoring purposes.
API Improvements (Bonus): Update APIs to use Viewsets and implement pagination for list APIs to enhance performance and usability.
Performance Optimization (Bonus): Optimize the performance of querysets to improve the application’s efficiency.
Technologies and Tools:
Docker, Celery, Django Rest Framework, and any other technologies suitable for the tasks.

Deliverables:
A GitHub repository containing the upgraded application code.
A Postman collection for testing all the endpoints.
Setup and Running Instructions:
Prerequisites:
Python 3.x installed on your system
Docker installed (optional, for containerization)
Postman installed (for testing the API endpoints)
Installation:
Clone the repository to your local machine:
git clone https://github.com/your_username/recipe-application.git
Navigate to the project directory:
cd recipe-application
Install the Python dependencies:

pip install -r requirements.txt
Running the Application:
Set up the Django database by running migrations:

python manage.py migrate
Start the Django development server:

python manage.py runserver
The application will be accessible at http://localhost:8000/
Testing the API Endpoints:
Import the provided Postman collection (Recipe_Application_Postman_Collection.json) into Postman.
Use the imported collection to test all the API endpoints.
Ensure that the application is running locally before testing the endpoints.
Additional Notes:
Customize the application as needed for your specific use case.
Ensure email settings are configured in the Django settings file for email notifications to work properly.
Follow Docker documentation for containerization and deployment if opting for Docker integration.
Explore Celery documentation for asynchronous task handling implementation.
Optimize the performance of querysets as per the project requirements.

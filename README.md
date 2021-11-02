# Backend API Automation using Python

This is an example of Backend API automation project, written using Python tytest.

# Purpose

This project was developed by me to demonstrate how to perform Backend API automation in which system communicate with the database and APIs and verify the results using assertions.

# Technology Stack

- Python
- Pytest
- Wordpress
- Assertions

# Prerequisites & Versions

- Python - Language & Virtual enviroment
- Pycharm - IDE
- SQL workbench - Database of wordpress

# Test Execution

Following command is used to run all tests marked as smoke.

pytest -m smoke

# Project Structure

This is the sample project for Backend API Automation that communicate with the API and Database and verify the results using Assertions. I have created its framework in a way that user can perform reusability, scalibility & maintability easily. Its structure is created in a way that all the config related files present in config folder, files related to communication with the database are present in dao folder, for functions that can be reuse are present in Helpers folder, Methods that are used to calls API are present in Utilities folder & All the test files the will be executed are present in test folder. You can navigate inside project folder to learn more about project structure.

# Test Reports

You can find all the generated test reports in the following location

./apiautotest/reports/

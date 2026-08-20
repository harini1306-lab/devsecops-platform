# DevSecOps Pipeline for Secure Software Delivery Platform

## Project Overview

This project demonstrates a DevSecOps pipeline for secure software development and delivery. It integrates version control, automated testing, containerization, continuous integration, and security scanning.

## Technologies Used

- HTML, CSS and JavaScript – Frontend
- Python and FastAPI – Backend
- SQLite – Application database
- PostgreSQL 16 – Docker database service
- pytest – Automated testing
- Git and GitHub – Version control
- Docker – Containerization
- Docker Compose – Multi-container management
- GitHub Actions – Continuous Integration
- Trivy – Docker image security scanning

## Project Structure

devsecops-platform/
├── frontend/
├── backend/
├── database/
├── tests/
├── .github/workflows/
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md

## Installation

Install the required Python dependencies:

pip install -r backend/requirements.txt

## Run the Backend

Start the FastAPI backend using:

uvicorn backend.main:app --reload

Open the API documentation at:

http://localhost:8000/docs

## Run Automated Tests

Run the test cases using:

python3 -m pytest

The project currently contains three automated API tests.

## Run Using Docker

Build and start the containers using:

docker compose up --build

Check running containers using:

docker ps

Stop the containers using:

docker compose down

## API Endpoints

GET / - Checks whether the backend is running.

GET /api/status - Returns the DevSecOps pipeline status.

GET /api/commit - Returns commit information.

## CI/CD and Security

GitHub Actions is used for Continuous Integration. The workflow automatically performs testing, dependency auditing, Docker image building, and Trivy vulnerability scanning.

## Future Improvements

- Connect the backend fully with PostgreSQL.
- Add more automated test cases.
- Restrict CORS configuration.
- Add exception handling.
- Retrieve Git commit information dynamically.
- Use environment variables and GitHub Secrets.
- Improve frontend and backend integration.

## Conclusion

The project demonstrates the use of Git, Docker, FastAPI, automated testing, GitHub Actions, and security scanning to create a basic secure software delivery pipeline.
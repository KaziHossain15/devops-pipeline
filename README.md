# DevOps Pipeline: Flask App with GitHub Actions CI/CD

This repository contains a simple Python Flask web application integrated with a GitHub Actions Continuous Integration (CI) workflow. The workflow automatically runs tests on every push to the `main` branch or when triggered manually.

---

## Project Overview

- **Flask app:** A minimal web server returning a greeting message.
- **CI pipeline:** Automatically installs dependencies and runs tests using GitHub Actions.
- **Testing:** Unit tests are written with `pytest`.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git

### Running Locally

1. Clone the repository:
   
   git clone https://github.com/KaziHossain15/devops-pipeline.git

   cd devops-pipeline

3.  Create and activate a virtual environment:

   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows

3. Install dependencies:

   pip install -r requirements.txt

4. Run the app:

   python app.py

5.  Running Tests

   Run tests locally with:
   pytest test_app.py


## GitHub Actions Workflow
The CI workflow is located in .github/workflows/python-app.yml. It runs:

On every push to the main branch

When manually triggered from GitHub UI

The workflow installs dependencies and runs tests using pytest

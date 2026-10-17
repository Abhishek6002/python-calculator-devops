# Python Calculator DevOps Project

A Python-based calculator application demonstrating Docker containerization, automated unit testing, version control, and Continuous Integration (CI) using GitHub Actions.

## Overview

This project implements a simple calculator that performs:

- Addition
- Subtraction
- Multiplication

It demonstrates how developers can automate testing and validate code changes whenever they push commits to GitHub.

## Technologies Used

- **Python**: Application logic and unit testing
- **Docker**: Containerization
- **Git and GitHub**: Version control and source code management
- **GitHub Actions**: Automated CI workflow
- **Markdown**: Project documentation

## Project Structure

```text
python-calculator-devops/
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── architecture.md
│   └── runbook.md
├── calculator.py
├── test_calculator.py
├── Dockerfile
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Install or configure the following tools:

- Python 3
- Git
- Docker Desktop

### Clone the Repository

```bash
git clone https://github.com/Abhishek6002/python-calculator-devops.git
cd python-calculator-devops
```

### Run Unit Tests

On Windows PowerShell:

```powershell
py -m unittest -v
```

On systems using the `python3` command:

```bash
python3 -m unittest -v
```

### Build the Docker Image

Ensure the Docker engine is running, then execute:

```bash
docker build -t python-calculator .
```

### Run the Docker Container

```bash
docker run --rm python-calculator
```

The container behavior depends on the command configured in the Dockerfile.

## Continuous Integration with GitHub Actions

The CI workflow is configured in `.github/workflows/ci.yml`.

The workflow is triggered by the configured GitHub events and automates the relevant build and testing steps.

Typical workflow:

1. A developer commits and pushes code to GitHub.
2. GitHub Actions starts the configured workflow.
3. The Docker image is built.
4. Automated tests are executed.
5. The workflow reports success or failure.

If a test fails, the workflow fails and displays logs to help identify the problem. Once the issue is fixed and pushed, a new workflow run validates the correction.

## Testing CI Failure Handling

The failure-handling mechanism was tested by deliberately changing an expected test result to an incorrect value.

- The unit test failed.
- GitHub Actions reported a failed workflow.
- The expected value was restored.
- A subsequent workflow completed successfully.

This demonstrates how automated testing can detect regressions before code changes are accepted.

## Documentation

- [Architecture and Workflow](docs/architecture.md)
- [Runbook and Troubleshooting](docs/runbook.md)

## Project Scope

This project focuses on local development, Docker-based containerization, automated testing, Git-based version control, and Continuous Integration.

AWS deployment and Continuous Deployment are outside the current implementation scope.

## Author

Abhishek Kumar


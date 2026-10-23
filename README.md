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

## Advanced GitHub Actions CI Workflow

### 1. Triggers

The workflow runs on:
- Pull requests targeting `master`.
- Pushes to `master`.

This helps validate proposed changes before merging and checks changes pushed to the default branch.

### 2. Job Architecture

The workflow contains two jobs:

**Test**
- Runs on Ubuntu.
- Uses a matrix to test Python 3.10 and Python 3.12.
- Runs unit tests and generates XML test reports.
- Uses `fail-fast: false` so both Python versions can report their results.

**Build Docker Image**
- Runs only after the test matrix succeeds.
- Builds the Docker image.
- Runs unit tests inside the container.

This dependency prevents the Docker job from running when the test job fails.

### 3. Test Reports and Artifacts

The workflow uses `unittest-xml-reporting` to generate XML test reports.

Reports are uploaded as GitHub Actions artifacts:
- `test-report-python-3.10`
- `test-report-python-3.12`

Artifacts are retained for seven days. The upload step uses `if: always()` so reports can also be uploaded when tests fail, provided report files were generated.

### 4. Efficiency Improvements

**Pip caching**

The workflow enables pip caching through `actions/setup-python` and uses `requirements.txt` as the cache dependency file. This allows dependencies to be reused when the cache key matches.

**Concurrency control**

The workflow uses a concurrency group with `cancel-in-progress: true`. Newer runs in the same group can cancel obsolete runs, reducing unnecessary CI work.

The trade-off is that an earlier run may be cancelled before finishing, so the latest run must still complete successfully.

### 5. Security

- Workflow permissions are restricted to `contents: read`.
- The workflow uses `pull_request`, not `pull_request_target`.
- No custom repository secrets or personal access tokens are required for this workflow.
- Third-party actions use version tags, such as `actions/checkout@v4` and `actions/setup-python@v5`.

**Further hardening:** Pinning third-party actions to verified full commit SHAs would provide stronger protection against changes to action tags. Full SHA pinning is not currently implemented.

### 6. Merge Gate and Validation Evidence

Branch protection is configured for `master` to require:
- Python 3.10 test check.
- Python 3.12 test check.
- Docker build check.

A successful pull request demonstrated that all required checks can pass. A separate test pull request deliberately introduced an incorrect assertion. GitHub blocked merging while required checks failed. After correcting the assertion, all three checks passed again.

Evidence:
- Successful PR: https://github.com/Abhishek6002/python-calculator-devops/pull/1
- Failing-check PR: https://github.com/Abhishek6002/python-calculator-devops/pull/2

### 7. Efficiency Summary

Compared with the earlier workflow, the updated workflow adds:
- Testing across multiple Python versions.
- XML test reports and downloadable artifacts.
- Dependency caching.
- Cancellation of obsolete workflow runs.
- A required-check merge gate.

These changes improve test coverage, troubleshooting, and CI resource usage.

### 8. Limitations

- The workflow builds and tests the Docker image but does not publish it or deploy the application.
- Workflow artifacts are retained for seven days.
- Full SHA pinning of third-party actions remains a potential security improvement.

## Author

Abhishek Kumar




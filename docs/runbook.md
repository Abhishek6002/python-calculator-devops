# Python Calculator DevOps Project: Runbook

## 1. Purpose

This runbook describes how to set up, run, test, containerize, and troubleshoot the Python calculator project.

## 2. Prerequisites

- Python with the `py` launcher available on Windows, or Python 3 installed on other operating systems.
- Git.
- Docker Desktop with the Docker engine running.
- A GitHub account for accessing the repository and workflow runs.

## 3. Get the Source Code

Clone the repository:

```powershell
git clone https://github.com/Abhishek6002/python-calculator-devops.git
cd python-calculator-devops
```

## 4. Run Unit Tests Locally

On Windows, run:

```powershell
py -m unittest -v
```

On systems where `python3` is the available Python command, run:

```bash
python3 -m unittest -v
```

Confirm that all tests pass before committing changes.

## 5. Build the Docker Image

Ensure Docker Desktop is running, then execute:

```powershell
docker build -t python-calculator .
```

This builds an image using the project's Dockerfile.

## 6. Run the Container

The appropriate command depends on the Dockerfile's configured startup command. For a calculator that runs tests by default, for example:

```powershell
docker run --rm python-calculator
```

The `--rm` option removes the container after it exits. Use the command appropriate to the actual application configuration.

## 7. Run the CI Workflow

1. Modify the source code or tests.
2. Run the tests locally.
3. Stage and commit the changes:

   ```powershell
   git add .
   git commit -m "Describe the change"
   ```

4. Push the commit:

   ```powershell
   git push
   ```

5. Open the repository's Actions tab:

   https://github.com/Abhishek6002/python-calculator-devops/actions

6. Inspect the workflow result and its logs.

## 8. Troubleshooting

### Unit tests fail

- Read the assertion failure.
- Compare the actual and expected results.
- Correct the application or test as appropriate.
- Run the tests again.

### Docker engine is unavailable

- Open Docker Desktop.
- Wait for the engine to start.
- Check availability with:

  ```powershell
  docker info
  ```

### Docker image build fails

- Confirm that `Dockerfile` exists in the project root.
- Check the build output for missing files, invalid instructions, or dependency errors.

### GitHub Actions fails

- Open the failed workflow run.
- Select the failed job and inspect its logs.
- Identify the failing step.
- Fix the issue, test locally, commit, and push again.

## 9. Cleanup

Remove the local Docker image when it is no longer needed:

```powershell
docker image rm python-calculator
```

Docker may refuse to remove the image while containers still depend on it. Inspect existing containers before removing anything.

## 10. Expected Outcome

The project should run its calculator tests locally, build successfully as a Docker image, and execute the configured GitHub Actions CI workflow. Failed tests should cause the workflow to fail, and corrected tests should allow it to pass.

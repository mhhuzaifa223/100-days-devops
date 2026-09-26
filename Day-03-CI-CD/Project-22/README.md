# Project 22 — Automated Unit Testing Pipeline

## Objective

Build an automated unit testing pipeline using Python, pytest, and GitHub Actions.

The pipeline automatically runs unit tests whenever changes are pushed to the main branch or a pull request targets main.

## Technologies

- Python
- pytest
- Git
- GitHub
- GitHub Actions
- Linux

## Project Structure

    100-days-devops/
    ├── .github/
    │   └── workflows/
    │       ├── ci.yml
    │       └── project-22-tests.yml
    │
    └── Day-03-CI-CD/
        └── Project-22/
            ├── app.py
            ├── test_app.py
            └── README.md

## Application

The application contains four simple functions:

- add()
- subtract()
- multiply()
- divide()

The divide() function also handles division by zero by raising a ValueError.

## Unit Tests

Five tests were created:

    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()

Local test command:

    pytest -v

Successful result:

    5 passed

## CI Workflow

The GitHub Actions workflow performs the following steps:

    Code Push / Pull Request
            ↓
    GitHub Actions
            ↓
    Checkout Repository
            ↓
    Set Up Python
            ↓
    Install pytest
            ↓
    Run Unit Tests
            ↓
    PASS / FAIL

The workflow is stored at the repository root:

    .github/workflows/project-22-tests.yml

GitHub Actions requires workflow files to be located inside the repository-level .github/workflows directory.

## Workflow Configuration

    name: Automated Unit Testing

    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main

    jobs:
      test:
        runs-on: ubuntu-latest

        steps:
          - name: Checkout repository
            uses: actions/checkout@v4

          - name: Set up Python
            uses: actions/setup-python@v5
            with:
              python-version: '3.11'

          - name: Install pytest
            run: pip install pytest

          - name: Run Unit Tests
            run: pytest -v Day-03-CI-CD/Project-22

## Troubleshooting

### Problem 1 — Python Virtual Environment Creation Failed

Initially:

    python3 -m venv venv

failed because the python3-venv package was missing.

The package was installed with:

    sudo apt update
    sudo apt install -y python3-venv

The virtual environment was then recreated successfully.

### Problem 2 — python Command Not Found

The system provided python3 rather than python.

Before activating the virtual environment:

    python3

was used.

After activating the virtual environment:

    source venv/bin/activate

the python command became available through the virtual environment.

### Problem 3 — Unit Test Failure

The divide-by-zero test initially contained:

    pytest.raises(ValueErro)

The correct exception is:

    pytest.raises(ValueError)

After fixing the typo:

    5 passed

### Problem 4 — Intentionally Broken Test

The add test was intentionally changed from:

    assert add(2, 3) == 5

to:

    assert add(2, 3) == 6

The application returned:

    5

while the test expected:

    6

pytest correctly reported:

    AssertionError

Four tests passed and one failed.

### Problem 5 — CI Did Not Initially Show the Expected Failure

The repository contained two GitHub Actions workflows:

    .github/workflows/ci.yml
    .github/workflows/project-22-tests.yml

Both workflows were triggered by pushes to main.

The Project 21 workflow could therefore appear green even when Project 22 was failing.

The correct workflow was checked under:

    Automated Unit Testing

After checking the correct workflow, Project 22 correctly showed a failed test.

### Problem 6 — Workflow Configuration Errors

The Project 22 workflow initially contained:

    python:-version: '3.11'

The correct configuration is:

    python-version: '3.11'

The workflow also initially used an incorrect path:

    Day-03-CI-CD/project-22

Linux paths are case-sensitive.

The correct path is:

    Day-03-CI-CD/Project-22

The workflow was corrected and the failure was successfully detected.

## Failure Testing

The project intentionally demonstrated a complete CI failure scenario:

    Correct test
        ↓
    Break expected result
        ↓
    Local pytest failure
        ↓
    Commit and push
        ↓
    GitHub Actions failure
        ↓
    Fix test
        ↓
    Push fix
        ↓
    GitHub Actions green

## Virtual Environment

The Python virtual environment is used only for local development.

It should not be committed to Git.

GitHub Actions creates its own clean Python environment during CI execution.

## Key Concepts Learned

- Unit testing
- pytest
- Assertions
- Expected vs actual results
- Exception testing
- ValueError
- Python virtual environments
- GitHub Actions
- CI test automation
- GitHub Actions runners
- actions/checkout
- actions/setup-python
- Workflow triggers
- YAML configuration
- Repository-relative paths
- Linux case sensitivity
- CI failure detection
- Troubleshooting failed pipelines
- Local testing vs CI testing

## Result

The Automated Unit Testing Pipeline successfully:

- Runs five unit tests.
- Detects failing tests.
- Reports failures through GitHub Actions.
- Allows fixes to be validated automatically.
- Returns to a green CI state after the tests are corrected.

Project 22 demonstrates a complete automated testing workflow from local development through CI validation.


# Amazon Nova Act for QA Automation

Nova Act QA demonstrates how to use [Amazon Nova Act](https://novs.amazon.com/act) to automate quality assurance (QA) and end-to-end testing in a web browser. Using the [Amazon Nova Act SDK](https://github.com/aws/nova-act), this project leverages [pytest](https://docs.pytest.org/en/stable/) for parallel test execution with custom HTML report generation via the [pytest-html-nova-act](https://pypi.org/project/pytest-html-nova-act/) plugin.

## Repository Structure

```
sample-nova-act-qa/
├── pyproject.toml  # Project dependencies and pytest config
├── .env.sample     # Sample .env file to copy
└── src/
    └── nova_act_qa/
        ├── config/  # Configuration management
        ├── tests/   # Test suite directory
        │   ├── conftest.py  # Pytest fixtures
        └── utils/   # Utility functions and types
```

## Pytest Plugins

The project uses several pytest plugins to enhance testing capabilities:

1. [pytest-html](https://pypi.org/project/pytest-html):

   - Generates HTML test reports
   - Includes test results, durations, and failure details

2. [pytest-html-nova-act](https://pypi.org/project/pytest-html-nova-act):

   - Integrates the Nova Act SDK screenshots and log output with the pytest-html report

3. [pytest-xdist](https://pypi.org/project/pytest-xdist):

   - Enables parallel test execution
   - Distributes tests across multiple CPU cores

These plugins are automatically installed with the project dependencies. No additional configuration is required.

## Nova Act Test Methods

This project extends the base Nova Act SDK `NovaAct` class with enhanced testing capabilities:

1. `test()`

   - Flexible assertion with schema validation
   - Supports exact matching and contains operators
   - Handles primitive types and complex JSON structures

2. `test_bool()`

   - Simplified boolean assertions
   - Default expectation of True

3. `test_str()`

   - String-specific assertions
   - Supports exact and partial matching

Example usage:

```python
nova.test_bool("Am I on the landing page?")
nova.test_str("Text input validation message", "Please enter a valid email address")
nova.test(
    "Product price tiers",
    [
        {"name": "Bronze", "price": 0.99},
        {"name": "Silver", "price": 4.99},
        {"name": "Gold", "price": 9.99}
    ],
    {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "price": {"type": "number"}
            }
        }
    })
```

See `src/nova_act_qa/utils/nova_act.py` for complete reference

## Project Usage

### Prerequisites

- Python 3.11 or higher
- pip 23.0 or higher
- Operating system:
  - macOS (Sierra or later)
  - Ubuntu (22.04 LTS or later)
  - Windows:
    - Windows 10 or later
    - Windows Subsystem for Linux 2 (WSL2)
- Nova Act API key
  - Visit [Nova Act home page](https://nova.amazon.com/act) to generate your API key

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd nova-act-qa

# Install dependencies using pip
pip install .
```

### Environment setup

1. Create a .env file based on the provided template:

```bash
cp .env.sample .env
```

2. Edit your new `.env` file to include your `NOVA_ACT_API_KEY`
   - Visit [Nova Act home page](https://nova.amazon.com/act) to generate your API key

### Quick start

1. Run the test suite:

```bash
pytest
```

2. View test HTML report:

```bash
open reports/report.html
```

## Test Output

### Nova Act SDK logs

The project creates a `.nova_act` directory structure for each test in the project root. These directories include the Nova Act SDK HTML log output and browser user data directories:

```
.nova_act/
├── logs/                 # Test execution logs
│   └── {module}/{test}/  # Logs organized by module and test name
└── user-data-dir/        # Browser user data directories
    └── {module}/{test}/  # Separate profile per test
```

See [the Nova Act SDK documentation](https://github.com/aws/nova-act?tab=readme-ov-file#viewing-act-traces) for more details on logging.

### Test report

An HTML report is automatically generated in the `reports` directory at the project root for each test run as configured in `pyproject.toml`. The report includes:

- Test results and durations
- Failure details and stack traces
- Nova Act SDK screenshots and logs

See the [pytest-html](https://pytest-html.readthedocs.io/en/latest/) documentation for more details.

## Test Configuration

The `pyproject.toml` file has a `[tool.pytest.ini_options]` section which defines the pytest configuration for the tests. This can be extended to customize your tests as needed.

## Test Automation

This project contains a [GitHub Actions workflow](https://docs.github.com/en/actions/about-github-actions/understanding-github-actions) template to automate running pytest and report generation when pull requests are made to the main branch.

The workflow file can be found in the root of the project: `~/.github/workflows/nova-act-qa.yml`.

### Prerequisites

The workflow requires configuring a [GitHub Secret](https://docs.github.com/en/actions/security-for-github-actions/security-guides/about-secrets) to store your Nova Act API Key:

1. Go to your Repository Settings
2. Navigate to `Secrets and variables > Actions`
3. Create a new Repository secret named `NOVA_ACT_API_KEY`
4. Input your API key value

More details can be found in the [GitHub Documentation](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository).

### Workflow details

#### Trigger

The workflow is triggered on pull requests targeting the `main` branch

#### Jobs and steps

The workflow consists of a single job named `test` with multiple steps:

1. **Checkout repo**

   - Uses `actions/checkout@v4` to fetch the repository code

2. **Install Python 3.11**

   - Uses `actions/setup-python@v5` to set up Python 3.11
   - Configures pip caching using pyproject.toml

3. **Install Python dependencies**

   - Upgrades pip
   - Installs the project dependencies
   - Installs Nova Act package (version 1.x)

4. **Playwright Setup**

   - Gets installed Playwright version for caching
   - Caches Playwright using `actions/cache@v4`
   - Installs Playwright OS dependencies and Chromium if cache miss
   - Installs only OS dependencies if cache hit

5. **Generate test identifier**

   - Creates a unique identifier for the test run using timestamp and run ID

6. **Run tests**

   - Sets up environment variables for the Nova Act SDK
   - Runs pytest with HTML report generation
   - Spread parallel tests out equally across available CPUs

7. **Upload report**

   - Uses `actions/upload-artifact@v4` to upload test results as [GitHub artifacts](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/storing-and-sharing-data-from-a-workflow)
   - The report can be downloaded by navigating to this step in the workflow run summary

8. **Check test results**
   - Workflow fails if tests do not pass

## Next Steps

Extend this repo and write your own tests in `src/noca_act_qa/tests`!

## Additional Resources

- [Amazon Nova Act](https://novs.amazon.com/act)
- [Amazon Nova Act SDK](https://github.com/aws/nova-act)
- [pytest-html-nova-act](https://pypi.org/project/pytest-html-nova-act/)

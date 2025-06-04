# Amazon Nova Act for QA Automation

Nova Act QA demonstrates how to use Amazon Nova Act to automate quality assurance (QA) and end-to-end testing in a web browser. Using the Nova Act SDK, this project leverages [pytest](https://docs.pytest.org/en/stable/) for parallel test execution with custom HTML report generation.

## Repository Structure

```
nova-act-qa/
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

1. pytest-xdist:

   - Enables parallel test execution
   - Distributes tests across multiple CPU cores

2. pytest-html:

   - Generates HTML test reports
   - Includes test results, durations, and failure details

3. pytest-html-nova-act:

   - Integrates the Nova Act SDK screenshots and log output with the pytest-html report

These plugins are automatically installed with the project dependencies. No additional configuration is required.

## NovaAct Test Methods

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

## Project Usage Instructions

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

### Environment Setup

1. Create a .env file based on the provided template:

```bash
# Copy the sample environment file
cp .env.sample .env

# Edit .env file and update your API key
# NOVA_ACT_API_KEY=your_api_key_here
```

### Quick Start

1. Run the test suite:

```bash
pytest
```

2. View test HTML report:

```bash
open reports/report.html
```

## Test output

### Nova Act SDK Logs

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

## Test configuration

The `pyproject.toml` file has a `[tool.pytest.ini_options]` section which defines the pytest configuration for the tests. This can be extended to customize your tests as needed.


## Next steps

Extend this repo and write your own tests in `src/noca_act_qa/tests`!

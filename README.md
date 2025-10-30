# UI Tests for Twitch Mobile Web

This project contains UI automation tests for the mobile web version of `m.twitch.tv` using Selenium and Pytest.

![demo](demo.gif)

## Project Structure

```
.
├── element/                # Custom Element wrapper for a fluent API (e.g., element.should.be_visible())
├── pages/                  # Page Object classes for different pages of the application
├── tests/                  # Test suites
│   ├── conftest.py         # Pytest fixtures and configurations (e.g., WebDriver setup)
│   └── test_*.py           # Test cases
├── utils/                  # Utility modules (e.g., logger, waits, JS helpers, screenshots)
├── .gitignore              # Files and directories to be ignored by Git
├── pytest.ini              # Pytest configuration file
├── README.md               # This file
└── requirements.txt        # Project dependencies
```


## Tech Stack

* **Python 3.11+**
* **Selenium**
* **Pytest**
* **Page Object Model**

## Setup

1. **Clone repository and navigate to project root**

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   ```

   Then, activate it:
    - **On macOS/Linux:**
      ```bash
      source .venv/bin/activate
      ```
    - **On Windows:**
      ```powershell
      .venv\Scripts\activate
      ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To run all tests, execute the following command from the project root:

```bash
pytest
```

### Command-line Options

* `--device`: Specify the device for mobile emulation (default: `"Pixel 2"`).

**Example:**

```bash
pytest --device "Nexus 5"
```
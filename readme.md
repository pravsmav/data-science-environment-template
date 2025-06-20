# Python Data Science Environment Template

This repository provides a simple, reproducible template for setting up a Python virtual environment with essential data science and machine learning libraries. It's designed to help you quickly get started on new projects without worrying about dependency conflicts.

## Features

* **Isolated Environment:** Uses `venv` to create a clean, dedicated environment for your project.
* **Essential Libraries:** Includes `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, and `jupyter` in `requirements.txt`.
* **Automated Setup:** A simple batch script (`setup_env.bat`) for quick environment creation and activation on Windows.
* **Verification Script:** A small `simpleMLProject.py` script to confirm your environment is correctly configured for basic machine learning tasks.

## Getting Started

### Prerequisites

* Python 3.x installed on your system and added to your PATH.

### Setup on Windows

1.  **Clone this repository** (or [download the ZIP](https://github.com/pravsmav/data-science-environment-template/archive/refs/heads/main.zip) and extract it):
    ```bash
    git clone https://github.com/pravsmav/data-science-environment-template.git
    cd data-science-environment-template
    ```
2.  **Run the setup script:**
    ```powershell
    .\setup_env.bat
    ```
    This script will:
    * Create a `.venv` virtual environment.
    * Activate it.
    * Install all libraries listed in `requirements.txt`.

### Verify Your Environment

Once the `setup_env.bat` script completes, your virtual environment will be active. You can then run the test script:

```powershell
python simpleMLProject.py
```

You should see output confirming successful library imports and a basic machine learning operation.

### Deactivating the Environment
When you're done working on the project, you can deactivate the virtual environment by simply typing:
```powershell
deactivate
```

## Learn More

For a detailed explanation of why virtual environments are crucial for data science and a deeper dive into this setup, check out my blog post:
[Link to MY blog post here - will update once deployed!]

## License

This project is open-source and available under the MIT License.

## Usage

### 1. Install Python
#### Mac
- Mac computers usually come with Python pre-installed. Open a terminal and type `python3 --version` to check the installed version. If Python is not installed, you can install it using [Homebrew](https://brew.sh/):
    ```bash
    brew install python
    ```
    Verify the installation by typing `python3 --version`.

#### Windows
- Download the latest version of Python from the [official website](https://www.python.org/downloads/).
- During installation, make sure to check the box that says "Add Python to PATH."
- Open a Command Prompt and type `python --version` or `python -V` to verify the installation.

### 2. Install pip3
#### Mac
- If Python is installed via Homebrew, pip (package installer for Python) is included. You can verify it by typing:
    ```bash
    pip3 --version
    ```

#### Windows
- Pip should be installed with Python on Windows. Verify by typing:
    ```bash
    pip --version
    ```

### 3. Install Dependencies
- Navigate to the script's directory using the terminal or Command Prompt and run:
    ```bash
    pip install os shutil datetime selenium requests urllib
    ```

### 4. Change the parameters in the script to your needs
- Change the following variables:

```bash
BASE_URL = "https://www.domain.com"
urls = [
        "url_1",
        "url_2",
        "...",
    ]
target_html_element_id = "main"
```

### 4. Run the Script
- Navigate to the directory containing the script in the terminal or Command Prompt.
- Run the script using the following command:
    ```bash
    python3 download_images.py 
    ```
    Replace `download_images.py ` with the actual name of your Python script.

### 5. Script Execution
- The script will start running and display progress messages in the terminal or Command Prompt.
- Once the script finishes, it will print a success message and provide the location of the zipped images.

### Note:
- Ensure you have an active internet connection, as the script fetches images from the specified website.
- Adjust the `BASE_URL` variable in the script if you want to target a different website.


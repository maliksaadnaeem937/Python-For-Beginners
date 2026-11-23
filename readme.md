# Python Project Setup

### 0. Create a Project Folder

Create a project folder example `python-course`. This folder is also called as root folder or root directory.

### 1. Create a Virtual Environment

Using command:

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

Using command:

```bash
venv/scripts/activate
```

### 3. Create `requirements.txt`

Create a file called `requirements.txt` in root folder and write all dependencies you need.

Dependencies are extra libraries that you want to use in your code but they are not available in Python by default.

So you have to install them on your own. Like to perform array operations you need library called "numpy".

Libraries provide builtin functions that makes it simpler for you to write code.

**Example:**

```text
pydantic
pydantic-settings
python-dotenv
```

Install all requirements using command:

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a file called `.env` in root of your project.

Root means directly inside your main project folder.

Write environment variables inside it.

Environment variables are the secret values which you dont want to directly in your code.

**Example:**

```env
APP_NAME=My Python Project
```

### 5. Create `config.py`

Create a file named as `config.py` inside your root folder. Again root means directly inside main project folder.

Write this code inside in `config.py`:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
```

The purpose of `config.py` is to load environment variables into "settings" object in our case so that we can use them inside your code using `settings.VARIABLE_NAME`.

### 6. Create `main.py`

Create a file named as `main.py` inside your root folder and write:

```python
from config import settings

print(settings.APP_NAME)
```

Then run this code using command:

```bash
python main.py
```

You will see output:

```text
My Python Project
```

0) Create a project folder example "python-course" this folder is also called as root folder or
   root directory.
1) Create virtual environment using command:
   python -m venv venv
2) Activate virtual environment using command:
   venv/scripts/activate
3) Create a file called  requirements.txt in root folder and write all dependencies you need.
   Dependencies are extra libraries that you want to use in your code but they are
   not available in python by default.
   So you have to install them on your own. Like to perform array operations you need
   library called "numpy".
   Libraries provide builtin functions that makes it simpler for you to write code.
   Example:
   pydantic
   pydantic-settings
   python-dotenv
   Install all requirements  using command : "pip install -r requirements.txt"

4) Create a file called .env in root of your project. 
   Root means directly inside your main project folder. 
   Write environment variables inside it.
   Environment variables are the secret values which you dont  want  to directly 
   in your code. 
   Example 
   APP_NAME=My Python Project

5) Create a file named as config.py inside your root folder. Again root means
   directly inside  main project folder.
   Write this code inside in config.py:

   
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


   The purpose of config.py is to load environment variables into "settings"
   object in our case so that we can
   use them inside your code using "settings.VARIABLE_NAME"

6) Create a file named as main.py inside your root folder
   and write :
   ```python
   from config import settings
   print(settings.APP_NAME)
   ```
   Then run this code using comamnd "python main.py" in terminal.
   you will see output : My Python Project



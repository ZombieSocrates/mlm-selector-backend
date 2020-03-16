# mlm-selector-backend
Backend API to power selection of ChIDEO MLM host

# dependencies
- python 3.6.10
- postgreSQL

# set up

Make a Python 3.6.10 virtual environment and install the requirements at the root of this repo. I use pyenv and pyenv-virtualenvwrapper, so for me this looks like

```
pyenv virtualenv 3.6.10 <NAME-OF-YOUR-VIRTUALENV>
pyenv activate <NAME-OF-YOUR-VIRTUALENV>
pip install -r requirements.txt
```

_For local development purposes only_: Create a `.env` file that looks something like this

```
ENV_NAME="DEVELOPMENT"
DEV_DB_URI="postgresql://<BASH-USERNAME>@localhost:5432/<NAME-OF-LOCAL-DB>"
```

Then, create the actual postgres database on your machine and populate it like so ...
```
createdb <NAME-OF-LOCAL-DB>
python load_database.py
```


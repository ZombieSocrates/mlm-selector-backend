# mlm-selector-backend
Backend API to choose and track ChIDEO MLM hosts

# dependencies
- python 3.6.10
- postgreSQL
- Heroku CLI

# set up
_N.B._ Throughout this section, anything formatted <LIKE-THIS> means you have to fill it in with user-specific values

- Make a Python 3.6.10 virtual environment and install the requirements at the root of this repo. I use [pyenv and  pyenv-virtualenvwrapper](https://gist.github.com/eliangcs/43a51f5c95dd9b848ddc), so for me this looks like:

```
pyenv virtualenv 3.6.10 <NAME-OF-YOUR-VIRTUALENV>
pyenv activate <NAME-OF-YOUR-VIRTUALENV>
pip install -r requirements.txt
```

- Create a `.env` file that looks something like the following:

```
ENV_NAME="DEVELOPMENT"
APP_CONFIG = "config.DevelopmentConfig"
FLASK_SECRET_KEY="<A-GNARLY-STRING>"

DEV_DB_URI="postgresql://<BASH-USERNAME>@localhost:5432/<NAME-OF-LOCAL-DB-FOR-PUSHING-TO-HEROKU>"
TEST_DB_URI="postgresql://rweijer@localhost:5432/<NAME-OF-LOCAL-DB-FOR-TESTING-BACKUP-PURPOSES>"
```

- Then, create the actual postgres database on your machine and populate it like so:
```
createdb <NAME(S)-OF-LOCAL-DB>
python load_database.py
```

- At this point, you should be able serve a local version of the API at `localhost/5000` as follows:

```
export FLASK_APP=app.py
flask run
```

# doing deploys
Assuming that you have been added to [the project on Heroku](https://dashboard.heroku.com/apps/ml-eminem), and that you have added the `heroku` remote branch to your local repo: `git remote add heroku <PUT URL FROM HEROKU DASHBOARD HERE>`. With that, you should be able to deploy the application by simply pushing to that remote branch.

```
heroku login
git push heroku master
```

**CAVEAT 1**: If anything you've done requires an update to the database, however, you'll need to run the following commands before pushing: 
```
heroku pg:reset DATABASE_URL
heroku pg:push postgresql://<BASH-USERNAME>@localhost:5432/<NAME-OF-LOCAL-DB> DATABASE_URL --app ml-eminem`
```

**CAVEAT 2**: If anything needs to be added to the requirements, do `pip freeze > requirements.txt` and commit before pushing.

# sketchy to-do list
- Build a route that accepts POST requests if a host is chosen
- Uh, better database hygiene
- If you really want to try-hard, separate DBs for testing, dev, and production
# API

## Requirements
`python3` \
`pip` : preferred installer program. Include by default with Python 3.4 \
`venv` : standard tool for creating virtual environments


## Environment variable

Project need an `.env` file at root directory (for pattern, cf. `.env.example`)

> **Enable Flask debug console. Doesn't use it for production environment**\
`FLASK_ENV=development`
`FLASK_DEBUG=True`

> **Generate two 16 bits random string. You can use this [tool](https://passwordsgenerator.net/)** \
`SECRET_KEY=***`
`SECURITY_PWD_SALT=True`

> **Database URI** \
`SQLALCHEMY_DATABASE_URI=postgresql://**`
`SQLALCHEMY_DATABASE_URI_LOCAL=postgresql://localhost:5432/**` \
>
> Specify at least one url and use the right run script (`run_local.sh` or `run_cloud.sh`) depending on your choice

> **SMTP Configuration** \
> `SMTP_EMAIL_SERVER=smtp.gmail.com` \
> `SMTP_EMAIL_PORT=465` \
> `SMTP_EMAIL_USER=<your_gmail_email>` \
> `SMTP_EMAIL_PASSWORD=<your_gmail_application_pwd>` \
>
> API is configured to work with the Google SMTP server only \
> You need to create an "app password" in your Google account. \
> For more details, please refer to Google [FAQ](https://support.google.com/accounts/answer/185833?hl=fr)

## Installation
```shell
# Clone Git repo
➜  $ git clone https://github.com/emmanuel-sarpedon/etna-pli-bachelor_flask_api.git
Cloning into 'etna-pli-bachelor_flask_api'...
[...]
Receiving objects: 100% (123/123), 26.94 KiB | 215.00 KiB/s, done.
Resolving deltas: 100% (44/44), done.

# Move on cloned folder
➜  $ cd etna-pli-bachelor_flask_api/

# Create an virtual environment
➜  $ python3 -m venv venv

# Activate the virtual environment
➜  $ source venv/bin/activate

# Install all necessary packages on virtual env
(venv) ➜ $ pip install -r requirements.txt
Collecting flask~=2.1.2
  Using cached Flask-2.1.2-py3-none-any.whl (95 kB)
[..]
Successfully installed Jinja2-3.1.2 Mako-1.2.0 MarkupSafe-2.1.1 SQLAlchemy-1.4.37 [...]

# Increase script privileges 
(venv) ➜ $ chmod u+x run_cloud_db.sh run_local_db.sh

# Lauch the API
### (with local database)
(venv) ➜ $ ./run_local_db.sh

### (or remote - cloud database)
(venv) ➜ $ ./run_cloud_db.sh

 * Serving Flask app 'app' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 122-083-220
```

## Database migration

For the first launch of the application, you must create all the tables of your database. We use here, `flask-migrate`
which detects the differences between your database and the models and updates your database if necessary :
```shell
> $ flask db upgrade # upgrade your database
```

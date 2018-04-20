# Bitcoin CLI GraphQL API

This is a simple server for any Bitcoin Node that has bitcoin-cli installed and the RPC server activated.

### Setup

[Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) must be working properly on your system before continuing.

* clone the repository
* copy config.ini.sample to config.ini and apapt the values to your requirements
* add a new virtual environment: _mkvirtualenv btc-graphql_
* _pip install -r requirements.txt_
* deactivate virtual environment to prevent some errors _deactivate_
* use the environment: _workon btc-graphql_
* _./manage.py makemigrations_
* _./manage.py migrate_
* _./manage.py runserver_

Open http://localhost:8000/graphql to explore the available queries via GraphiQL.

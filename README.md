Flask quickstarts
======


Development
------

To setup your virtualenv:

    $ mkvirtualenv sampleapp
    $ setvirtualenvproject sampleapp path_to_project

    # Optionally, create a new project with
    $ mkproject sampleapp
    $ git clone git@github.com:jsvgoncalves/flask-quickstart .

Then, everytime you work on the project, run:

    $ workon sampleapp

To install the dependecies run:

    $ pip install -r requirements.txt

### Virtualenvwrapper cheatsheet

    # To stop working
    $ deactivate
    # To show all environments
    $ workon
    # To show installed packages
    $ lssitepackages

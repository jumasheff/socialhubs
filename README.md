# socialhubs
An educational project for It-Attractor coding club members

## Installation
 * install Pillow dependencies:
    `sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk`
 * clone the project (we like to use ~/projects dir. The final path would look like ~/projects/socialhubs)
 * create virtualenv named venv: `virtualenv -p /usr/bin/python2.7 venv`
 * activate virtualenv: `source venv/bin/activate`
 * install project dependencies: `pip install -r requirements.txt`
 * run migrations: `manage.py migrate`
 * load fixtures: `manage.py loaddata apps/fixtures.json`
 
## Run tests
 * cd to the project root
 * bash run_tests.sh
 
## Default settings
 * the project uses SQLite (for now)
 * superuser -- username: admin pass: 123
 
## Credits
 * Alexey Karahanidi
 * Kairat Omurbek uulu

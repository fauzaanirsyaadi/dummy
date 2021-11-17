## Final project Movie-Director API with Flask

# task :
1. Mampu melakukan membuat API dengan Flask.
2. Mampu melakukan operasi CRUD ke dalam database dengan SQLAlchemy dan Flask.
3. Mampu melakukan deployment ke Heroku.

# persyaratan

virtual env
pip
python
code editor
flask
database


# instalasi virtualenv dan setup

pip install virtualenv
virtualenv --version
mkdir nama_project
cd nama_project
virtualenv env

# beberapa cara activkan env (windows)

env\Scripts\activate.bat
sortcut installation syntac (in env): pip install -r requirements.txt

untuk auto membuat requitments.txt pip3 freeze

-- install flask dan setup --
1. pip install flask
2. flask --version
3. pip install flask-dotenv
4. buat folder bernama app

-- RDBMS --
1. buat databse
2. configurasi .env
3. flask db init
4. buat models init,..
5. flask db migrate -m "comment"
6. flask db upgrade

## Resource :

github : https://github.com/fauzaanirsyaadi/dummy
heroku : https://h8ocbc-milestone1-025.herokuapp.com/api/ui/

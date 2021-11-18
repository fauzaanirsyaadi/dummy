'''
ini adalah file config yang berisi data konfigurasi
'''
import os

import connexion
from flask import jsonify, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'final_proj.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jtevnnhswxubhi:1ed2ca23e061086d6d0b70a26f376110a1449b69eab54871a56f606667f73d2c@ec2-34-198-189-252.compute-1.amazonaws.com:5432/dcvvrc09alvf9p'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

CORS(app, resources={r"/*": {"origins": "*", "methods": "GET,HEAD,PUT,PATCH,POST,DELETE"}})

connect_str = 'sqlite:///' + os.path.join(basedir, 'final_proj.db')
engine = create_engine(connect_str, echo=False)
from models import Movie
from models import Director


# get all movies
@app.route('/movies/', methods=['GET'])
def get_all_movie():
    response = jsonify([
        {
            "id": i.id,
            "title": i.title,
            "original_title": i.original_title,
            "budget": i.budget,
            "popularity": i.popularity,
            "release_date": i.release_date,
            "revenue": i.revenue,
            "vote_average": i.vote_average,
            "vote_count": i.vote_count,
            "overview": i.overview,
            "tagline": i.tagline,
        } for i in Movie.query.all()
    ])
    return response


# get movie by offsiet limit
@app.route('/movies/<int:offset>/<int:limit>', methods=['GET'])
def get_movie_by_offset_limit(offset, limit):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies LIMIT ? OFFSET ?', (limit, offset))
        row = rs.fetchall()
        if row:
            return jsonify([dict(i) for i in row])
        else:
            return jsonify({'error': 'Not found'})


# search director
@app.route('/movies/search/<string:director>', methods=['GET'])
def get_movie_by_director(director):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE director ILIKE ' % {} % ' ORDER BY director'.format(director))
        row = rs.fetchall()
        if row:
            return jsonify([dict(i) for i in row])
        else:
            return jsonify({'error': 'Not found'})


# get movie by title
@app.route('/movies/title/<string:title>', methods=['GET'])
def get_movie_by_title(title):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE title = ?', (title,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get movie by original title
@app.route('/movies/original_title/<string:original_title>', methods=['GET'])
def get_movie_by_original_title(original_title):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE original_title = ?', (original_title,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get movie by budget
@app.route('/movies/budget/<int:budget>', methods=['GET'])
def get_movie_by_budget(budget):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE budget = ?', (budget,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get movie by popularity
@app.route('/movies/popularity/<int:popularity>', methods=['GET'])
def get_movie_by_popularity(popularity):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE popularity = ?', (popularity,))
        # row fetch all
        row = rs.fetchall()
        if row:
            return jsonify([dict(i) for i in row])
        else:
            return jsonify({'error': 'Not found'})

        # row = rs.fetchone()
        # if row:
        #     return jsonify(dict(row))
        # else:
        #     return jsonify({'error': 'Not found'})


# get movie by release date
@app.route('/movies/release_date/<string:release_date>', methods=['GET'])
def get_movie_by_release_date(release_date):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE release_date = ?', (release_date,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get movie by revenue
@app.route('/movies/revenue/<int:revenue>', methods=['GET'])
def get_movie_by_revenue(revenue):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE revenue = ?', (revenue,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get movie by runtime
@app.route('/movies/runtime/<int:runtime>', methods=['GET'])
def get_movie_by_runtime(runtime):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE runtime = ?', (runtime,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get movie by vote average
@app.route('/movies/vote_average/<int:vote_average>', methods=['GET'])
def get_movie_by_vote_average(vote_average):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE vote_average = ?', (vote_average,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get movie by vote count
@app.route('/movies/vote_count/<int:vote_count>', methods=['GET'])
def get_movie_by_vote_count(vote_count):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE vote_count = ?', (vote_count,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get all directors
@app.route('/directors', methods=['GET'])
def get_all_directors():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM directors')
        return jsonify([dict(row) for row in rs.fetchall()])


# get director by id
@app.route('/directors/<int:id>', methods=['GET'])
def get_director_by_id(id):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM directors WHERE id = ?', (id,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get director by name
@app.route('/directors/name/<string:name>', methods=['GET'])
def get_director_by_name(name):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM directors WHERE name = ?', (name,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get director by movie
@app.route('/directors/movie/<int:movie_id>', methods=['GET'])
def get_director_by_movie(movie_id):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM directors WHERE id IN (SELECT director_id FROM movies WHERE id = ?)',
                         (movie_id,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})


# get most popular movies
@app.route('/movies/popular', methods=['GET'])
def get_most_popular_movies():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies ORDER BY popularity DESC')
        return jsonify([dict(row) for row in rs.fetchall()])


# get 5 most revenue
@app.route('/movies/revenue', methods=['GET'])
def get_most_revenue_movies():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies ORDER BY revenue DESC LIMIT 5')
        return jsonify([dict(row) for row in rs.fetchall()])


# get 5 most less revenue
@app.route('/movies/less_revenue', methods=['GET'])
def get_most_less_revenue_movies():
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies ORDER BY revenue ASC LIMIT 5')
        return jsonify([dict(row) for row in rs.fetchall()])


# check if a movie is in the database
@app.route('/movies/<int:id>', methods=['GET'])
def check_movie_in_db(id):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies WHERE id = ?', (id,))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            # return error message not found with id
            return jsonify({'error': 'maaf movie yang anda cari tidak ada'})


# show movie with pagination
@app.route('/movies/page/<int:page>', methods=['GET'])
def show_movie_with_pagination(page):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM movies LIMIT 5 OFFSET ?', (page,))
        return jsonify([dict(row) for row in rs.fetchall()])

# get director name and uid with pagination
@app.route('/directors/page/<int:page>', methods=['GET'])
def show_director_with_pagination(page):
    with engine.connect() as con:
        rs = con.execute('SELECT name, uid FROM directors LIMIT 5 OFFSET ?', (page,))
        return jsonify([dict(row) for row in rs.fetchall()])


# get director name and uid
@app.route('/directors/name/<string:name>/uid/<string:uid>', methods=['GET'])
def get_director_by_name_and_uid(name, uid):
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM directors WHERE name = ? AND uid = ?', (name, uid))
        row = rs.fetchone()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({'error': 'Not found'})



from app import connex_app
import unittest


class FlaskTest(unittest.TestCase):
    data_director = {
        "department": "test",
        "gender": 1,
        "name": "test",
        "uid": 0
    }
    data_movie = {
        "budget": 0,
        "original_title": "test",
        "overview": "test",
        "popularity": 0,
        "release_date": "2015/02/19",
        "revenue": 0,
        "tagline": "test",
        "title": "test",
        "uid": 0,
        "vote_average": 0,
        "vote_count": 0
    }
    def test_get_all_director(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/director/0/10')
        self.assertEqual(response.status_code, 200)
        print('')
        print('----------------------------------------------------------------------')
        print('Test Get_All_Director Completed')
        print('----------------------------------------------------------------------')
    
    def test_post_director(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.post('/api/director', json = self.data_director)
        self.assertEqual(response.status_code, 201)
        print('')
        print('----------------------------------------------------------------------')
        print('Test Post_Director Completed')
        print('----------------------------------------------------------------------')

    def test_get_all_movie(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/movie/0/10')
        self.assertEqual(response.status_code, 200)
        print('')
        print('----------------------------------------------------------------------')
        print('Test Get_All_Movie Completed')
        print('----------------------------------------------------------------------')

    def test_post_movie(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.post('/api/director/7100/movie', json = self.data_movie)
        self.assertEqual(response.status_code, 201)
        print('')
        print('----------------------------------------------------------------------')
        print('Test Post_Movie Completed')
        print('----------------------------------------------------------------------')
        


if __name__ == "__name__":
    unittest.main()
from django.test import TestCase, Client
from student_management_app.models import Courses, Staffs


class ViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Courses.objects.create(course_name='Ruby')

    def test_view_url_courses_by_id(self):
        c = Client()
        resp = c.get('/courses/10/')
        print("RESP::::::::::",resp)
        self.assertEqual(resp.status_code, 404)

    def test_view_signup_admin(self):
        resp = self.client.get('/signup_admin')
        self.assertEqual(resp.status_code, 200)

    def test_view_doLogin(self):
        resp = self.client.post('/doLogin')
        self.assertEqual(resp.status_code, 302)

    def test_post_req(self):
        c = Client()
        resp = c.post('/courses/', {"id": 7, "course_name": "Fly", "created_at": "2020-12-19T10:16:35.970959Z",
                                    "updated_at": "2020-12-19T10:16:35.971029Z"})
        resp.status_code
        # print(resp.__dict__.get('data').get('course_name'))
        self.assertEqual(resp.status_code, 201)
        self.assertIsInstance(resp.content,bytes)
        self.assertEqual(resp.__dict__.get('data').get('course_name'),'Fly')


    def test_get_reques(self):
        c = Client()
        resp1 = c.get('/courses/')
        # print('RESP CONTENT:::::::',resp1.content[2])
        # print(type(resp1.__dict__.get('data')))
        # self.assertIsInstance(resp1.__dict__.get('data'), ('rest_framework.utils.serializer_helpers.ReturnList'))
        self.assertEqual(resp1.__dict__.get('request'),{'PATH_INFO': '/courses/', 'REQUEST_METHOD': 'GET', 'SERVER_PORT': '80', 'wsgi.url_scheme': 'http', 'QUERY_STRING': ''})
        self.assertIn('data',str(resp1.__dict__))



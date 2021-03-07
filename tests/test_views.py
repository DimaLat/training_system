from django.test import TestCase
from student_management_app.models import Courses


class ViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Courses.objects.create(course_name='Ruby')

    def test_view_url_courses_by_id(self):
        resp = self.client.get('/courses/2')
        self.assertEqual(resp.status_code, 301)

    def test_view_signup_admin(self):
        resp = self.client.get('/signup_admin')
        self.assertEqual(resp.status_code, 200)

    def test_view_doLogin(self):
        resp = self.client.post('/doLogin')
        self.assertEqual(resp.status_code, 302)


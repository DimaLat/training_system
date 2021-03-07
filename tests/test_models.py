from django.test import TestCase
from student_management_app.models import Courses


class CoursesModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Courses.objects.create(course_name='Ruby')

    def test_course_name_label(self):
        course=Courses.objects.get(id=1)
        field_label = course._meta.get_field('course_name').verbose_name
        self.assertEquals(field_label,'course name')

    def test_create_at_label(self):
        course=Courses.objects.get(id=1)
        field_label = course._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label,"created at")

    def test_course_name_max_length(self):
        course=Courses.objects.get(id=1)
        max_length = course._meta.get_field('course_name').max_length
        self.assertEquals(max_length,255)






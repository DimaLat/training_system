from django.test import TestCase

from student_management_app.forms import EditStudentForm


class StudentFormTest(TestCase):

    def test_students_form_field_label(self):
        form = EditStudentForm()
        self.assertTrue(form.fields['email'].label is not None)

    def test_course_name_max_length(self):
        form = EditStudentForm()
        max_length = form.fields['first_name'].max_length
        self.assertEquals(max_length, 50)

    def test_student_sex_field_label(self):
        form = EditStudentForm()
        self.assertTrue(form.fields['sex'].label is not None)

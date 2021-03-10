from django.test import TestCase

from student_management_app.forms import EditStudentForm


class StudentFormTest(TestCase):

    def test_students_form_field_label(self):
        form = EditStudentForm()
        pic_required = form.fields['profile_pic'].required
        max_length = form.fields['first_name'].max_length

        self.assertFalse(pic_required)
        self.assertTrue(form.fields['email'].label is not None)
        self.assertEquals(max_length, 50)
        self.assertTrue(form.fields['sex'].label is not None)

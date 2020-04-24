from wtforms import validators,ValidationError
from flask_wtf import Form
from wtforms.compat import string_types


class test_again(object):
    #field_flags = ('required', )

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        print(not field.data)
        print(field.data)
        print(isinstance(field.data, string_types))
        print(field.data.strip())
        if not field.data or isinstance(field.data, string_types) and not field.data.strip():
            if self.message is None:
                message = field.gettext('This field is required.')
            else:
                message = self.message

            field.errors[:] = []
            raise validators.StopValidation(message)


class my_test(object):
    #field_flags = ('required', )

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        print(not field.data)
        print(field.data)
        print(isinstance(field.data, string_types))
        print(field.data.strip())
        if not field.data or isinstance(field.data, string_types) and not field.data.strip():
            if self.message is None:
                message = field.gettext('This field is required.')
            else:
                message = self.message

            field.errors[:] = []
            raise validators.StopValidation(message)
from __future__ import unicode_literals

from django import forms


class DatePickerInput(forms.widgets.DateInput):
    attrs = {'class': "datepicker",
             'data-date-format': 'yyyy-mm-dd'}

    def __init__(self):
        super(DatePickerInput, self).__init__(self.attrs, format='%Y-%m-%d')

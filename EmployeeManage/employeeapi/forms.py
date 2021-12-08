from django import forms
from .models import Employee


# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

'''class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','Email','Password','Address')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code',
            'mobile':'Mobile Number',
            'Email':'Email',
            'Password':'Password',
            'Address':'Address'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        #self.fields['Department'].empty_label = "Select"
        self.fields['emp_code'].required = False
'''
class NumWordForm(forms.Form):
    Number = forms.IntegerField()






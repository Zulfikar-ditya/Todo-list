from django import forms


class AddTodoForm(forms.Form):
    value = forms.CharField(max_length=200)
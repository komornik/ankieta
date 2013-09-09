# -*- coding: UTF-8 -*-
from django import forms

from models import Poll

class PollForm(forms.ModelForm):
    votes = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)

        choices = self.instance.choice_set.all().values_list('id', 'choice')
        
        votes_field = self.fields['votes']
        votes_field.widget = forms.RadioSelect()
        #votes_field.choices = [('', '-- wybierz odpowiedź --',),] + list(choices)
        votes_field.choices = choices
        votes_field.label = self.instance.question

    class Meta:
        model = Poll
        fields = ('votes',)


class PollForms(forms.ModelForm):
    pass
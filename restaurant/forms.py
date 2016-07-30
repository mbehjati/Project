from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class SearchForm(forms.Form):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    one_to_ten =( ('1', '1') , ('2' , '2') , ('3' , '3') , ('4' , '4') , ('5' ,'5'))

    name = forms.CharField(max_length=50)
    type = forms.ChoiceField(label='type' , widget=forms.Select ,choices=CHOICES)
    score_from = forms.ChoiceField(widget=forms.Select , choices=one_to_ten)
    score_to =  forms.ChoiceField(widget=forms.Select , choices=one_to_ten)
    taste = forms.ChoiceField(label='taste' , widget=forms.Select ,choices=CHOICES)
    price_from = forms.ChoiceField( widget=forms.Select ,choices=one_to_ten)
    price_to = forms.ChoiceField( widget=forms.Select ,choices=one_to_ten)


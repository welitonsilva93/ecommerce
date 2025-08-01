from django import forms

class AdicionarCarrinhoForm(forms.Form):
    quantidade = forms.IntegerField(min_value=1, label='quantidade')
    
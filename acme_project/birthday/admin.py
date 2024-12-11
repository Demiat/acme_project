from django import forms


class ContestForm(forms.Form):
    title = forms.CharField(
        label='Название',
        max_length=20
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={'rows': 10, 'cols': 30}
        )
    )
    price = forms.IntegerField(
        label='Цена',
        help_text='Рекомендованная розничная цена',
        max_value=100,
        min_value=10,
        widget=forms.NumberInput()
    )
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(
            attrs={'rows': 10, 'cols': 20}
        ),
        required=False
    )

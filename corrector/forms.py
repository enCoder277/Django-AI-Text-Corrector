from django import forms


class TextCorrectionForm(forms.Form):
    original_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 6,
            'cols': 80,
            'placeholder': 'Введите текст для исправления...',
        }),
        label='Ваш текст',
        required=True
    )
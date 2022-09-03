from django import forms


class formdata(forms.Form):
    name = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input'}))
    psrd = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={'class': 'input'}), label='Password')
    rpsrd = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'input'}),
                            label='Re-Type Password')

    def clean(self):
        cleaned_data = super().clean()

        p = self.cleaned_data['psrd']
        rp = self.cleaned_data['rpsrd']

        if p != rp:
            raise forms.ValidationError('Password not matched')

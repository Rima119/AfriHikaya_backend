from django import forms

class CustomUserCreationForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=160)
    last_name = forms.CharField(max_length=160)
    username = forms.CharField(max_length=160, required=False)
    country = forms.CharField(max_length=160)
    native_language = forms.CharField(max_length=160)
    hobbies = forms.CharField(max_length=255, required=False)
    roles = forms.CharField(max_length=160, required=False)
    profile_pic = forms.FileField(required=False)
    profile_pic_url = forms.CharField(max_length=255, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('passwords do not match')
        return cleaned_data
from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    'placeholder': 'Your full name',
                    'class': 'form-control'
                    }
                    )   
        )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                    'placeholder': 'Your email',
                    'class': 'form-control'
                    }
                    )   
        )

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    'placeholder': 'Your message',
                    'class': 'form-control'
                    }
                    )   
        )
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("Email has to be gmail.com")
    #     return email

    # def clean_content(self):
    #     raise forms.ValidationError("Content is wrong.")
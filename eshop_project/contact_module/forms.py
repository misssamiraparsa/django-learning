from django import forms

from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی', max_length=50,
                                error_messages={
                                    'required': 'please enter your fullname',
                                },
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'نام و نام خانوادگی'
                                })
                                )
    email = forms.EmailField(label='ایمیل',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'ایمیل'
                             })
                             )
    title = forms.CharField(label='موضوع', required=False,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'موضوع'
                            })
                            )
    message = forms.CharField(label='متن',
                              widget=forms.Textarea(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'متن پیام',
                                  'rows': '5',
                                  'id': 'massage',
                              }))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'rows': 5,
                                             'id': 'message'
                                             }),
        }

        labels = {
            'full_name': 'first and last name'
        }

        error_messages = {
            'full_name': {
                'required' : 'نام و نام خانوادگی اجباری است'
            }
        }

        # fields = '__all__'
        # exclude = ['response']

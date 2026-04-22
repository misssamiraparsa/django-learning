from django import forms


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
    subject = forms.CharField(label='موضوع', required=False,
                              widget=forms.EmailInput(attrs={
                                  'class': 'form-control',
                                  'placeholder': 'موضوع'
                              })
                              )
    text = forms.CharField(label='متن',
                           widget=forms.Textarea(attrs={
                               'class': 'form-control',
                               'placeholder': 'متن پیام',
                               'rows': '5',
                               'id': 'massage'
                           }))

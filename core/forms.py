from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    number = forms.IntegerField(label='Number')
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    # For get the data
    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        number = self.cleaned_data['number']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name}\nEmail: {email}\nNumber: {number}\nSubject: {subject}\nMessage: {message}'

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='andrecrgoveia@gmail.com',
            to=['andrecrgoveia@gmail.com',],
            headers={'Reply-To': email}
        )
        mail.send()


from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):
    # title = forms.CharField(
    #     max_length=120,
    #     label='Some field',
    #     help_text='some help text',
    #     error_messages={
    #         'required': 'The title field is required'
    #     }
    # )

    class Meta:  # is describing anything that's not a field
        model = Post
        fields = ['user', 'title', 'slug', 'image']
        # exclude = ['height_field', 'width_field']
        labels = {
            'title': 'this is  title label',
            'slug': 'this is slug'
        }
        help_texts = {
            'title': 'this is  title label',
            'slug': 'this is slug'
        }
        error_messages = {
            'title': {
                'max_length': 'This title is too long',
                'required': 'The title field is required'
            },
            'slug': {
                'max_length': 'This title is too long',
                'required': 'The slug field is required'
                # 'unique': 'The slug field is must be unique'

            }
        }

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].error_messages = {
            'max_length': 'This title is too long',
            'required': 'The title field is required'
        }
        self.fields['slug'].error_messages = {
            'max_length': 'This title is too long',
            'required': 'The slug field is required'
        }

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     print(title)
    #     # raise forms.ValidationError('What the is heck is that aSDQWDDQ!')
    #     return title

    # def save(self, commit=True):  # overriding save method
    #     obj = super(PostModelForm, self).save(commit=False)
    #     obj.publish = '2016-10-01'
    #     obj.content = 'THIS CONTENT CONTAINS SOME CONTENTS'
    #     if commit:
    #         obj.save()
    #     return obj


SOME_CHOICES = [
    ('db-value', 'display value'),
    ('db-value2', 'display value2'),
    ('db-value3', 'display value3'),
    ('db-value4', 'display value4'),
]
INT_CHOICES = [
    tuple([x, x]) for x in range(0, 100)
]
YEARS = [x for x in range(1960, 2035)]


class TestForm(forms.Form):
    date_field = forms.DateField(initial='2014-11-20', widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label='Great feature', widget=forms.Textarea(attrs={'rows': 4, 'cols': 10}))
    choices = forms.CharField(label='Select', widget=forms.Select(choices=SOME_CHOICES))
    # choices2 = forms.CharField(label='RadioSelect', widget=forms.RadioSelect(choices=SOME_CHOICES))
    # choices3 = forms.CharField(label='CheckboxSelectMultiple',
    # widget=forms.CheckboxSelectMultiple(choices=SOME_CHOICES))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10)
    email = forms.EmailField(min_length=10)

    def __init__(self, user=None, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        # self.fields['email'].initial = 'some@newmail.com'
        if user:
            self.fields['some_text'].initial = user.username

    def clean_integer(self, *args, **kwargs):  # Basic form validation
        integer = self.cleaned_data.get('integer')
        if integer < 10:
            raise forms.ValidationError('The integer must be greater than 10')
        return integer

    def clean_some_text(self, *args, **kwargs):  # Basic form validation
        some_text = self.cleaned_data.get('some_text')
        if len(some_text) < 10:
            raise forms.ValidationError('Ensure the text is greater than 10 character')
        return some_text

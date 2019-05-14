from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render
from .forms import TestForm, PostModelForm


# Create your views here.
def formset_view(request):
    TestFormSet = formset_factory(TestForm)
    formset = TestFormSet()
    context = {
        'formset': formset
    }
    return render(request, 'formset_view.html', context)


def home(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)  # get the same data from the form but don't put in db yet for a second
        obj.title = 'Some random title'
        obj.publish = '2010-10-10'
        obj.save()  # As default, commit=True

    if form.has_error:
        # print(form.errors.as_json())
        # print(form.errors.as_text())
        data = form.errors.items()
        for key, value in data:
            print('key --> ', key, ' value --> ', value)
            err_str = "{field}: {error}".format(field=key, error=value)
            print(err_str)

    # initial_dict = {  # view(initial dictionary in view) overrides forms initial values
    #     'some_text': 'merhaba gibi',
    #     "integer": 4,
    #     'boolean': True
    # }
    # form = TestForm(request.POST or None, initial=initial_dict)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     print(form.cleaned_data.get('some_text'))
    #     print(form.cleaned_data.get('email'))
    #     print(form.cleaned_data.get('email2'))
    # ilk burayı aç / comment in
    # if request.method == 'POST':
    #     form = TestForm(data=request.POST)
    #     print(request.POST)
    #     print(request.POST.get("username"))  # None
    #     # print(request.POST.get["username2"])  # RaiseError
    # elif request.method == 'GET':
    #     form = TestForm(user=request.user)
    #     print(request.GET)
    return render(request, 'forms.html', {"form": form})

from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from test_app.handlers import ProgressBarUploadHandler
from test_app.models import TestModel


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class FileUploadView(View):
    model = TestModel
    template_name = 'test_app/upload.html'

    def setup(self, request, *args, **kwargs):
        request.upload_handlers.insert(0, ProgressBarUploadHandler)
        super(FileUploadView, self).setup(request, *args, **kwargs)

    def get(self, request):
        form = FileUploadForm()
        return render(request, self.template_name, context={'form': form})

    @method_decorator(csrf_protect)
    def post(self, request):
        print(request.upload_handlers)
        return HttpResponse(status=200)
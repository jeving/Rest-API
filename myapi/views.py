import csv, io, os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HospitalSerializer
from .models import Hospital

from django.views.generic.list import ListView
# Create your views here.


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all().order_by('Hospital')
    serializer_class = HospitalSerializer


@permission_required('admin.can_add_log_entry')
def data_upload(request):
    template = "abc1.html"
    prompt = {
        'order' : 'name , alias'
    }
    if request.method == "GET":
        return render(request,template,prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,"this is not a csv file")
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string , quotechar = '|'):
        _, created  = Hospital.objects.update_or_create(
            Hospital = column[0],
            County = column[1],
            City = column[2],
        )
    context = {}
    return render(request, template, context)

path = '../downloads.csv'
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
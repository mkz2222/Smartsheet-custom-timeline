from django.shortcuts import render

from .models import Projects, Status

from django.db.models import Max

from django.utils.dateparse import parse_datetime


def smartsheet_timeline(request):


	projects = Projects.objects.all().order_by('-Last_update')

	comments = Status.objects.all()

	# #Total number of records
	qmax1 = Projects.objects.all().aggregate(Max('Index'))

	qmax = int(qmax1['Index__max']) 

	qmax = '{:,}'.format(qmax)

	#Use a fixed time in this example
	datetime_object = parse_datetime('2025-5-02T02:33:00')

	context = {

	'qmax' : qmax,

	'projects' : projects,

	'comments' : comments,

	'date' : datetime_object,
	}

	return render(request, 'smartsheet_web_template.html', context)




# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def test(request):
	#student_ids = models.Student.objects.all()
	#teacher_ids = models.Teacher.objects.all()

	return render(request, "template.html")
	# return HttpResponse("Hello, world. You're at the index file.")
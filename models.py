# -*- coding: utf-8 -*-		
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):

	name = models.CharField(max_length=150)
	salary = models.IntegerField(default=1)
	salary1 = models.FloatField(default=0)
	email = models.EmailField()

	def __str__(self):
		return self.name



class Teacher(models.Model):

	name = models.CharField(max_length=150)
	student_id = models.ForeignKey('Student')

	def __str__(self):
		return "%s (%d)"%(self.name,self.student_id.name, self.student_id.salary)

class Courses(models.Model):

	courses = models.CharField(max_length=100)

	student_id = models.ForeignKey('Student')

	def __str__(self):
		return "%s %s"%(self.student_id.name,self.courses)



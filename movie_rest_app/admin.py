# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin
from models import Genre, MovieDetail

admin.site.register(Genre)
admin.site.register(MovieDetail)
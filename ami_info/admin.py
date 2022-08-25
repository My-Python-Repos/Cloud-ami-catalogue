# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ami_info.models import Ami, Update
# Register your models here.
admin.site.register(Ami)
admin.site.register(Update)

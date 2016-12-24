# -*- encoding: UTF-8 -*-
"""
@author: Federico Cáceres <fede.caceres@gmail.com>
"""
from django.contrib import admin
from chat.models import *

admin.site.register(Room)
admin.site.register(Message)
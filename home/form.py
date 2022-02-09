from .models import *

from django.forms import ModelForm
from .models import *



class CUs_form(ModelForm):

    class Meta:

        model = Order
        fields = '__all__'
       # exclude = ('job_link',)

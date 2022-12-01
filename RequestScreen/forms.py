from django.forms import ModelForm
from .models import VisitRequestDetails


class VisitRequestDetailsForm(ModelForm):
    class Meta:
        model = VisitRequestDetails
        fields = '__all__'

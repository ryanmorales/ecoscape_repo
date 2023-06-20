from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm, forms
from .models import Visa

class VisaProcessingForm(BSModalModelForm):
    class Meta:
        model = Visa
        exclude = ['created_by','updated_by','date_created','date_updated']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }


class VisaFilterForm(BSModalForm):
    client_surname = forms.CharField(max_length=250, required=False)
    or_number = forms.CharField(max_length=50, required=False)

    class Meta:
        fields = ['client_surname','or_number']

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm, forms
from .models import Passport

class PassportProcessForm(BSModalModelForm):
    class Meta:
        model = Passport
        exclude = ['created_by','updated_by','date_created','date_updated']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'epp_passport_date_issued': forms.DateInput(attrs={'type': 'date'}),
        }


class PassportFilterForm(BSModalForm):
    client_surname = forms.CharField(max_length=250, required=False)
    or_number = forms.CharField(max_length=50, required=False)

    class Meta:
        fields = ['client_surname','or_number']

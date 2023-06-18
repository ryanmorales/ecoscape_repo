from bootstrap_modal_forms.forms import BSModalModelForm
from .models import Visa

class VisaProcessingForm(BSModalModelForm):
    class Meta:
        model = Visa
        exclude = ['created_by','updated_by','date_created','date_updated'] 

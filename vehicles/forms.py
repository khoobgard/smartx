from vehicles.models import Vehicle , Master

class FormModelName(forms.ModelForm):
    class Meta():

        model = Vehicle
        fields = '__all__'

class FormModelMaster(forms.ModelForm):
    class Meta():

        model = Master
        fields = '__all__'

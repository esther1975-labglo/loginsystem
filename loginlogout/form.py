from django import forms  
from loginlogout.models import registration  

   
class reg_Form(forms.ModelForm):  
    class Meta:  
        model = registration
         
        fields = "__all__"  #meta use and "__all__" 

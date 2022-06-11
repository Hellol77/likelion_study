from .models import User
from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
   class Meta(UserCreationForm.Meta):
       model = User
       fields = ['user_id','password']
# Venom
A CRM developed while learning with SteinOveHelset

for creating superuser-
from django. contrib.auth.models import User 
from userprofile.models import Userprofile
superuser = User.objects.get(username='admin')
UserProfile.objects.create(user=superuser)

admin-
test4@gmail.com
pass: zxcvbnm,
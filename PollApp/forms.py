from django import forms

class RegisterForm(forms.Form):
	Name=forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Age=forms.IntegerField(required=True,widget=forms.NumberInput(attrs={'class':'form-control'}))
	Place=forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Mobile=forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
	Password=forms.CharField(required=True,max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))
	ConfirmPassword=forms.CharField(required=True,max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class LoginForm(forms.Form):
	Email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
	Password=forms.CharField(required=True,max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class PollForm(forms.Form):
	Question=forms.CharField(max_length=200,required=True,widget=forms.Textarea(attrs={'cols':'80','rows':'1','class':'form-control'}))
	Option1=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Option2=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Option3=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
	Option4=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

	




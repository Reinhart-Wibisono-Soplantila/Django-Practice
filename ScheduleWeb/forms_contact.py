from django import forms

class ContactForms(forms.Form):
    Nama_Lengkap=forms.CharField(label='Nama Lengkap', max_length=20)
    Gender = (
        ('P', 'Pria'),
        ('W', 'Wanita')
    )
    
    Jenis_Kelamin = forms.ChoiceField(
        # widget=forms.RadioSelect,
        choices=Gender)
    Email = forms.EmailField(label='Alamat Email')
    Alamat = forms.CharField(label='Alamat')
    Kode_Pos = forms.IntegerField(label='Kode Pos')
    Kota = forms.CharField(label='Kota')
    Provinsi = forms.CharField(label='Provinsi', required=False)
    Agree = forms.BooleanField(label='Agree')
    
from django import forms

class ContactForms(forms.Form):
    Nama_Lengkap=forms.CharField(label='Nama Lengkap', max_length=20)
    Gender = (
        ('P', 'Pria'),
        ('W', 'Wanita')
    )
    
    Jenis_Kelamin = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Gender
        )
    Tahun = range(1990, 2030, 1)
    tanggal_lahir = forms.DateField(
        # memakai years untuk mengedit tahun
        widget=forms.SelectDateWidget(years = Tahun),
    )
    Email = forms.EmailField(label='Alamat Email')
    Alamat = forms.CharField(
        max_length=100,
        label='Alamat',
        widget=forms.Textarea,
        )
    Kode_Pos = forms.IntegerField(label='Kode Pos')
    Kota = forms.CharField(label='Kota')
    Provinsi = forms.CharField(label='Provinsi', required=False)
    Agree = forms.BooleanField(label='Agree')
    
from django import forms

class ContactForms(forms.Form):
    NamaLengkap=forms.CharField(
        label='Nama Lengkap', 
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Masukkan Nama Lengkap'
            }
            )
        )
    def clean_NamaLengkap(self):
        NamaLengkap_input = self.cleaned_data.get('NamaLengkap')
        if NamaLengkap_input == 'Hello World':
            raise forms.ValidationError("Hellow World Not Allowed")
        # print(NamaLengkap_input)
        return NamaLengkap_input
    
    
    Jenis_Kelamin = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class' : "form-check-label",
                }
            ),
        choices=(
            ('P', 'Pria'),
            ('W', 'Wanita')
        ),
        )
    
    tanggal_lahir = forms.DateField(
        # memakai years untuk mengedit tahun
        widget=forms.SelectDateWidget(
            attrs={
                'class' : 'form-select',
                },
            years = range(1990, 2030, 1)
            ),
    )
    
    Email = forms.EmailField(
        label='Alamat Email',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Masukkan Email',
            }
        )
    )
    
    Alamat = forms.CharField(
        max_length=100,
        label='Alamat',
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Masukkan Email',
            }
        ),
    )
    
    Agree = forms.BooleanField(
        label='Agree',
        widget=forms.CheckboxInput(
            attrs={
                'class' : 'form-check-input'
            }
        )
    )
    
    # Kode_Pos = forms.IntegerField(label='Kode Pos')
    # Kota = forms.CharField(label='Kota')
    # Provinsi = forms.CharField(label='Provinsi', required=False)
   
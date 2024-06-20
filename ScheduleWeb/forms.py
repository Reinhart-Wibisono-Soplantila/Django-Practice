from django import forms
class ContactForm(forms.Form):
    
    # Data Type
    nama = forms.CharField()
    alamat = forms.CharField(max_length=10)
    integer = forms.IntegerField(required=False)
    decimal = forms.DecimalField(required=False)
    float = forms.FloatField(required=False)
    boolean = forms.BooleanField(required=False)
    
    # String Input
    email = forms.EmailField()
    
    # belum tau cara pakai regex
    # regex = forms.RegexField()
    
    slug = forms.SlugField()
    url = forms.URLField()
    ip = forms.GenericIPAddressField()
    
    # Select Input
    Pilihan=(
        ('nilai1', 'pilihan1'),
        ('nilai2', 'pilihan2'),
        ('nilai3', 'pilihan3'),
        ('nilai4', 'pilihan4'),
    )
    choice = forms.ChoiceField(choices=Pilihan)
    multi = forms.MultipleChoiceField(choices=Pilihan)
    typemulti = forms.TypedMultipleChoiceField(choices=Pilihan)
    null_boolean = forms.NullBooleanField()
    
    # Date time
    date_field = forms.DateField()
    datetime_field = forms.DateTimeField()
    duration_field = forms.DurationField()
    time_field = forms.TimeField()
    splitdatetime_field = forms.SplitDateTimeField() 
    
    # File Field
    file_field = forms.FileField()
    image_field = forms.ImageField()
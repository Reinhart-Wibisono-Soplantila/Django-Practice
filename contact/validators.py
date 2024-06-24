from django.core.exceptions import ValidationError

def validate_NamaLengkap(value):
    NamaLengkap_input = value
    if NamaLengkap_input == 'Einstein':
        message = "maaf," + NamaLengkap_input + "Tidak bisa di posting"
        raise ValidationError(message)
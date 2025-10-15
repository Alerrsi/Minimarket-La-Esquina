import re
from django.core.exceptions import ValidationError

class StrongPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r"[A-Z]", password):
            raise ValidationError("Debe contener al menos una letra mayúscula.")
        if not re.search(r"[a-z]", password):
            raise ValidationError("Debe contener al menos una letra minúscula.")
        if not re.search(r"\d", password):
            raise ValidationError("Debe contener al menos un número.")
        if not re.search(r"[@$!%*?&]", password):
            raise ValidationError("Debe contener al menos un carácter especial (@, $, !, %, *, ?, &).")

    def get_help_text(self):
        return "Debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un símbolo."

from django.forms import ValidationError


error_messages = {
    'invalid': "CPF Inválido.",
    'digits_only': "Este campo só aceita números.",
    'max_digits': "Este campo aceita apenas 11 digitos.",
}


def validate_cpf(cpf):
    try:
        int(cpf)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])

    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    if len(numbers) != 11:
        raise ValidationError(error_messages['max_digits'])

    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        raise ValidationError(error_messages['invalid'])

    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        raise ValidationError(error_messages['invalid'])

    return numbers

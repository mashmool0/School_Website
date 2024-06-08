from django import template

register = template.Library()


@register.filter(name="money")
def convert_to_persian(number):
    # Mapping of English digits to Persian digits
    persian_digits = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹'
    }

    # Convert the number to a string to iterate over each character
    number = "{:,}".format(int(number))
    persian_number = ''

    # Replace each English digit with the corresponding Persian digit
    for digit in number:
        if digit in persian_digits:
            persian_number += persian_digits.get(digit, digit)  # Use get to handle non-digit characters
        else:
            persian_number += digit
    # now convert it to better format and integer

    return persian_number

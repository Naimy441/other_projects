import re, pyperclip

def find_phone_numbers(text):
    phone_number_pattern = re.compile(r'''(
        (\d{3}|\(\d{3}\))
        (\s|\.|-)
        (\d{3})
        (\s|\.|-)
        (\d{4})
        )''', re.VERBOSE)
    return phone_number_pattern.findall(text)

tuples_of_phone_number_groups = find_phone_numbers(pyperclip.paste())

list_of_phone_numbers = []
print("Copied to Clipboard:")
for tuple_of_phone_number_groups in tuples_of_phone_number_groups:
    print(tuple_of_phone_number_groups[0])
    list_of_phone_numbers.append(tuple_of_phone_number_groups[0])

pyperclip.copy("\n".join(list_of_phone_numbers))

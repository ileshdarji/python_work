# 2 August 2020 — this programme is all about strings

person_name = "ilesh"

person = {
    "first_name": "ilesh",
    "last_name": "darji",
}

print(person)

person_full_name = f"{person['first_name']} {person['last_name']}"

print(person_full_name.title())


message = f"Hello {person_full_name.title()}, would you like to learn some Python today? \n {person_full_name.lower()} \n {person_full_name.upper()}"
print(message)


famous_quote = {
    "author": " Albert Einstein ",
    "quote": " A person who never made a mistake never tried anyting new. ",
}

quote_message = f'{famous_quote["author"].rstrip()} once said: "{famous_quote["quote"].strip()}" \n\t "{famous_quote["quote"].lstrip()}" \n\t "{famous_quote["quote"].rstrip()}"'
print(quote_message)

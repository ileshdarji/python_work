mydict = {'pk': '#STRASC::2020-01-26::6562::7602680', 'strasc': '0.1918',
          'component_terms': [['calculated_strasc', '0'], ['inter_branch_transfer_units', '22'],
                              ['pk', '#STRASC::2020-01-26::6562::7602680']]}

expected_calculated_strasc = '0'
item = ['calculated_strasc', expected_calculated_strasc]
# print(item)

component_terms = mydict['component_terms']
# print(component_terms[0])
# print(component_terms.index('inter_branch_transfer_units'))
# print(type(component_terms))

assert item in component_terms, f"BOOOOOO"

# for i in component_terms:
#     if i == item:
#         print(f"yeeeeeeey")
#         break
#     else:
#         raise Exception(f"boooo | {i}")



# for i, v in enumerate(component_terms):
#     if v == item:
#         print(f"i == {i}")
#         print(f"v == {v}")
#         print(f"component_terms == {component_terms}")

#
# order(item, component_terms)

# print(type(component_terms))
#
#
# print(component_terms[0])
# print(component_terms[0][0])


# for k in mydict.items():
#     list(k)
#     calculated_strasc = list(k[1])
#     print(calculated_strasc)
#
#
# def nested_get(mydict, nested_key):
#     internal_dict_value = mydict
#     for k in nested_key:
#         internal_dict_value = internal_dict_value.get(k, None)
#         if internal_dict_value is None:
#             return None
#     return internal_dict_value
#
# nested_get(mydict, )

from dnd_ldap import lookup

query = raw_input("Enter a name or nickname:")
print lookup(query, ['mail','uid'])
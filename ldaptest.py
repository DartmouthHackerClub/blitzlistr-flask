from dnd_ldap import lookup
# dndAssignedNetid
query = raw_input("Enter a name or nickname:")
print "you entered: \"" + query + "\""
lookup(query)
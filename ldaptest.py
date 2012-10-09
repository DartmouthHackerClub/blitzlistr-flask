from dnd_ldap import *

word = raw_input("Enter a netid:")
print "you entered: \"" + word + "\""
lookup("dndAssignedNetid",word,"mail")
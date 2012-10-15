from dnd_ldap import *
# dndAssignedNetid
word = raw_input("Enter a netid:")
print "you entered: \"" + word + "\""
lookup("uid",word,"mail")
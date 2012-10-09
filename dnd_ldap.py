def main(netid):
	import ldap

	keyword = netid
	try:
		l = ldap.open("ldap.dartmouth.edu")
		l.simple_bind_s("", "")
		print "Successfully bound to server.\n"
	except ldap.LDAPError, error_message:
		print "Couldn't Connect. %s " % error_message

	baseDN = "dc=dartmouth, dc=edu"
	searchScope = ldap.SCOPE_SUBTREE

	retrieveAttributes = ["mail"]
	searchFilter = ("dndAssignedNetid="+ keyword)

	try:
		ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
		result_set = []
		while 1:
			result_type, result_data = l.result(ldap_result_id, 0)
			if (result_data == []):
				break
			else:
				if result_type == ldap.RES_SEARCH_ENTRY:
					print result_data
	#	print result_data
	except ldap.LDAPError, e:
		print e

	# try:
	# 	ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
	# 	result_set = []
	# 	while 1:
	# 		result_type, result_data = l.result(ldap_result_id, 0)
	# 		if (result_data == []):
	# 			break
	# 		else:
	# 			## here you don't have to append to a list
	# 			## you could do whatever you want with the individual entry
	# 			## The appending to list is just for illustration. 
	# 			if result_type == ldap.RES_SEARCH_ENTRY:
	# 				result_set.append(result_data)
	# 	print result_set
	# except ldap.LDAPError, e:
	# 	print e
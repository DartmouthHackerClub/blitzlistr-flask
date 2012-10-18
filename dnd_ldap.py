def lookup(query):
	import ldap

	try:
		l = ldap.initialize('ldap://ldap.dartmouth.edu')
		l.start_tls_s()
		l.simple_bind_s("", "")
		print "Successfully bound to server."
	except ldap.LDAPError, error_message:
		print "Couldn't Connect. %s " % error_message

	baseDN = "dc=dartmouth, dc=edu"
	searchScope = ldap.SCOPE_SUBTREE
	retrieveAttributes = ['mail']
	# retrieveAttributes= what LDAP retrieves in response to query. None for everything, expects list of strings
	paddedQuery = "*"
	query_list = query.split(' ')
	for s in query_list:
		paddedQuery = paddedQuery+ "".join(s +"*")

	# searchFilter is the LDAP Search Filter: Use 'dndAssignedNetid' for netid
	searchFilter = "(|(cn="+ paddedQuery + ")(nickname=" + paddedQuery+"))"
	print "Searching using search filter \"" + searchFilter + "\"."
	try:
		ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
		result_set = []
		while 1:
			result_type, result_data = l.result(ldap_result_id, 0)
			if (result_data == []):
				l.unbind()
				break
			else:
				if result_type == ldap.RES_SEARCH_ENTRY:
					d = [tup[1] for tup in result_data]
					print result_data
					print d
	except ldap.LDAPError, e:
		print e
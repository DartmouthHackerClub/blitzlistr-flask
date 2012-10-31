# Performs a DND Lookup
# query is a string, while attribs is the attributes you want returned for each matching object

def lookup(query,attribs=None):
    import ldap, re
    response = []
    try:
        l = ldap.initialize('ldap://ldap.dartmouth.edu')
#       l.start_tls_s()
        l.simple_bind_s("", "")
        print "Successfully bound to server."
    except ldap.LDAPError, error_message:
        print "Couldn't Connect. %s " % error_message

    baseDN = "dc=dartmouth, dc=edu"
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = attribs
    query = (re.sub("^|\s+|$", "*", query))
    searchFilter = "(|(cn="+ query + ")(nickname=" + query +")(mail="+ query + "))"

    print "Requested \"" + str(attribs) + "\" using search filter \"" + searchFilter + "\"."

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
                        response.append(result_data)
    except ldap.LDAPError, e:
        print e

    return response
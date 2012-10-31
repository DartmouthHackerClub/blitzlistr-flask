import ldap, re

default_attributes = ['cn', 'mail', 'dndDeptclass', 'eduPersonAffiliation', 'dndAssignedNetid'] 

l = None

def lookup(query,attribs=default_attributes):
    global l
    response = []

    if l is None:
        try:
            l = ldap.ldapobject.ReconnectLDAPObject('ldap://ldap.dartmouth.edu')
            l.simple_bind_s("", "")
        except ldap.LDAPError, error_message:
            l = None
            return None

    baseDN = "dc=dartmouth, dc=edu"
    searchScope = ldap.SCOPE_SUBTREE
    retrieveAttributes = attribs
    query = (re.sub("^|\s+|$", "*", query))
    searchFilter = "(|(cn="+ query + ")(nickname=" + query +")(mail="+ query + "))"

    try:
        results = l.search_st(baseDN, searchScope, searchFilter, retrieveAttributes, timeout=1)
        for r in results:
            response.append(r[1])
    except ldap.LDAPError, e:
        print e
        return None

    return response

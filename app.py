from flask import Flask, request, session, render_template, redirect
from dnd_ldap import lookup
import re

app = Flask(__name__)

@app.route("/")
def index():
    err_msg = ""
    qlist_txt = request.args.get('qlist_txt')

    if qlist_txt:
        qlist_txt = qlist_txt.strip(',;\n\r ')
        qlist = re.split(',|;|\n', qlist_txt)
    else:
        qlist = []

    conflicts = []
    not_founds = []
    blitzlist = []
    for query in qlist:
        results = lookup(query)
        print results
        if results is None:
            blitzlist = []
            err_msg = "LDAP query failed"
        
        elif len(results) == 1:
            result = results[0]
            blitzlist.append(result['Email'])
        elif len(results) == 0:
            not_founds.append(query)
        elif len(results) > 1:
            conflicts.append(query)

    to_string = "; ".join(blitzlist)
    conflict_string = ", ".join(conflicts)
    not_founds_string = ", ".join(not_founds)

    return render_template('listr.html', to_string=to_string, \
                            not_founds_string=not_founds_string, \
                            conflict_string=conflict_string)

if __name__ == "__main__":
    app.run(debug=False)

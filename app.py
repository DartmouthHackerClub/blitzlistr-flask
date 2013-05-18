from flask import Flask, request, session, render_template, redirect
from dnd_ldap import lookup
import re

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    qlist_txt = request.form.get('qlist_txt') or request.args.get('qlist_txt') or ''
    separator = request.form.get('separator') or request.args.get('separator') or ';'

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

    to_string = ("%s " % separator).join(blitzlist)
    conflict_string = ", ".join(conflicts)
    not_founds_string = ", ".join(not_founds)

    return render_template('listr.html', **locals())

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)

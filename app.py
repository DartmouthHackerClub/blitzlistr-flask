from flask import Flask, request, session, render_template, redirect
from dnd_ldap import lookup
import re

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/blitzlistr')

@app.route("/blitzlistr")
def make_list():
    err_msg = ""
    qlist_txt = request.args.get('qlist_txt')

    if qlist_txt:
        qlist = re.split(',|;|\n', qlist_txt)
    else:
        qlist = []

    conflicts = []
    not_founds = []
    results = []
    for query in qlist:
        r = lookup(query, ['mail'])
        print r
        if r is None:
            err_msg = "LDAP query failed"
            break
        elif len(r) == 1:
            results.append(r[0]['mail'][0])
        elif len(r) == 0:
            not_founds.append(query)
        elif len(r) > 1:
            mails = map(lambda x: x['mail'][0], r)
            conflicts.append((query, mails))

    to_string = "; ".join(results)
    conflict_string = ", ".join(map(lambda c:c[0] , conflicts))
    not_founds_string = ", ".join(not_founds)

    return render_template('listr.html', to_string=to_string, \
                            not_founds_string=not_founds_string, \
                            conflict_string=conflict_string)

if __name__ == "__main__":
    app.run(debug=True)

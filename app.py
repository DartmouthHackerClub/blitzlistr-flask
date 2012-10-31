from flask import Flask, request, session, render_template
from dnd_ldap import lookup

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('search.html', results=[])

@app.route("/search")
def search():
    err_msg = ""
    results = []

    query = request.args.get('query')

    if not query:
        err_msg = "Please specifiy a query"
    else:
        results = lookup(query)

    if results == None:
        results = []
        err_msg = "LDAP query failed"

    return render_template('search.html', results=results, err_msg=err_msg)

if __name__ == "__main__":
    app.run(debug=True)

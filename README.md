dnd-ldap
===================

Uses python-ldap

Introduction:
--------------------

This project uses Dartmouth's ldap directory to look up a Dartmouth email address when passed a netid.  To use, follow the setup instructions and then run the test script:

	$ python ldaptest.py

Setup
-----

Assuming you already have Python and pip installed, go ahead and install
`virtualenv` if you haven't already:

    $ sudo pip install virtualenv

Now, create a new virtualenv (this provides an isolated environment for
the app to run in):

    $ virtualenv dnd-ldap
    $ cd dnd-ldap
    $ source bin/activate

The virtualenv is now set up. You can clone this repository inside the
virtualenv:

    $ git clone https://github.com/DartmouthHackerClub/dnd-ldap.git

I've included a `requirements.txt` file, which, coupled with pip and
virtualenv, provides an automatic method for installing all necessary
dependencies:

    $ cd dnd-ldap
    $ pip install -r requirements.txt


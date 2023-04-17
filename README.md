# Documentation
  https://docs.google.com/document/d/1G2zMKBnXpjMHraJP-ez9fOsn0mnW7BnOIzChiFxFTU0/edit

# How to save python requirements.

* Source the python venv

```
source ./bluetoothenv/Scripts/activate
```

* Freeze the requirements into a requirements.txt

```
py -m pip freeze > requirements.txt
```

For our particular project, this will create the following requirements.txt:

```
bcrypt==4.0.1
click==8.1.3
colorama==0.4.6
Flask==2.2.3
Flask-Login==0.6.2
Flask-SQLAlchemy==3.0.3
Flask-WTF==1.1.1
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.2
SQLAlchemy==2.0.9
typing_extensions==4.5.0
Werkzeug==2.2.3
WTForms==3.0.1
```

# How to load python requirements

```
py -m pip install -r requirements.txt
```

In our case, this should result in the following console output:

```
$ py -m pip install -r requirements.txt
Collecting bcrypt==4.0.1
  Using cached bcrypt-4.0.1-cp36-abi3-win_amd64.whl (152 kB)
Collecting click==8.1.3
  Using cached click-8.1.3-py3-none-any.whl (96 kB)
Collecting colorama==0.4.6
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting Flask==2.2.3
  Using cached Flask-2.2.3-py3-none-any.whl (101 kB)
Collecting Flask-Login==0.6.2
  Using cached Flask_Login-0.6.2-py3-none-any.whl (17 kB)
Collecting Flask-SQLAlchemy==3.0.3
  Using cached Flask_SQLAlchemy-3.0.3-py3-none-any.whl (24 kB)
Collecting Flask-WTF==1.1.1
  Using cached Flask_WTF-1.1.1-py3-none-any.whl (12 kB)
Collecting greenlet==2.0.2
  Using cached greenlet-2.0.2-cp310-cp310-win_amd64.whl (192 kB)
Collecting itsdangerous==2.1.2
  Using cached itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting Jinja2==3.1.2
  Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)
Collecting MarkupSafe==2.1.2
  Using cached MarkupSafe-2.1.2-cp310-cp310-win_amd64.whl (16 kB)
Collecting SQLAlchemy==2.0.9
  Using cached SQLAlchemy-2.0.9-cp310-cp310-win_amd64.whl (2.0 MB)
Collecting typing_extensions==4.5.0
  Using cached typing_extensions-4.5.0-py3-none-any.whl (27 kB)
Collecting Werkzeug==2.2.3
  Using cached Werkzeug-2.2.3-py3-none-any.whl (233 kB)
Collecting WTForms==3.0.1
  Using cached WTForms-3.0.1-py3-none-any.whl (136 kB)
Installing collected packages: typing_extensions, MarkupSafe, itsdangerous, greenlet, colorama, bcrypt, WTForms, Werkzeug, SQLAlchemy, Jinja2, click, Flask, Flask-WTF, Flask-SQLAlchemy, Flask-Login
Successfully installed Flask-2.2.3 Flask-Login-0.6.2 Flask-SQLAlchemy-3.0.3 Flask-WTF-1.1.1 Jinja2-3.1.2 MarkupSafe-2.1.2 SQLAlchemy-2.0.9 WTForms-3.0.1 Werkzeug-2.2.3 bcrypt-4.0.1 click-8.1.3 colorama-0.4.6 greenlet-2.0.2 itsdangerous-2.1.2 typing_extensions-4.5.0

[notice] A new release of pip available: 22.3.1 -> 23.1
[notice] To update, run: python.exe -m pip install --upgrade pip
```


# How to create a venv:

Go look it up.

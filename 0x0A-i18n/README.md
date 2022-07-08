# 0x0A. i18n
## Details
      By Emmanuel Turlay, Staff Software Engineer at Cruise          Weight: 1                Ongoing project - started Jul 7, 2022 , must end by Jul 8, 2022           - you're done with 0% of tasks.              Checker was released at Jul 7, 2022 12:00 PMManual QA review must be done          (request it when you are done with the project)              An auto review will be launched at the deadline       ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/1/91e1c50322b2428428f9.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220707%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220707T192845Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ef79bf6816958af7cb19c37583b4ab05a7fdb636d1414e78fa4f96db7e7d221c) 

## Resources
Read or watch:
* [Flask-Babel](https://intranet.hbtn.io/rltoken/Q71CxQOjqpOJrqHd_F4lXQ) 

* [Flask i18n tutorial](https://intranet.hbtn.io/rltoken/NdAnX-Td57RRaA25LX0A1Q) 

* [pytz](https://intranet.hbtn.io/rltoken/yk8MxfbrtfmHusK6pmX7XQ) 

## Learning Objectives
* Learn how to parametrize Flask templates to display different languages
* Learn how to infer the correct locale based on URL parameters, user settings or request headers
* Learn how to localize timestamps
## Requirements
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* The first line of all your files should be exactly  ` #!/usr/bin/env python3 ` 
* All your  ` *.py `  files should be executable
* All your modules should have a documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your classes should have a documentation ( ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` )
* All your functions and methods should have a documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` )
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.
## Tasks
### 0. Basic Flask app
          mandatory         Progress vs Score  Task Body First you will setup a basic Flask app in   ` 0-app.py `  . Create a single   ` / `   route and an   ` index.html `   template that simply outputs “Welcome to Holberton” as page title (  ` <title> `  ) and “Hello world” as header (  ` <h1> `  ).
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x0A-i18n ` 
* File:  ` 0-app.py, templates/0-index.html ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Basic Babel setup
          mandatory         Progress vs Score  Task Body Install the Babel Flask extension:
 ` $ pip3 install flask_babel
 ` Then instantiate the   ` Babel `   object in your app. Store it in a module-level variable named   ` babel `  .
In order to configure available languages in our app, you will create a   ` Config `   class that has a   ` LANGUAGES `   class attribute equal to   ` ["en", "fr"] `  .
Use   ` Config `   to set Babel’s default locale (  ` "en" `  ) and timezone (  ` "UTC" `  ).
Use that class as config for your Flask app.
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x0A-i18n ` 
* File:  ` 1-app.py, templates/1-index.html ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Get locale from request
          mandatory         Progress vs Score  Task Body Create a   ` get_locale `   function with the   ` babel.localeselector `   decorator. Use   ` request.accept_languages `   to determine the best match with our supported languages.
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x0A-i18n ` 
* File:  ` 2-app.py, templates/2-index.html ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Parametrize templates
          mandatory         Progress vs Score  Task Body Use the   ` _ `   or   ` gettext `   function to parametrize your templates. Use the message IDs   ` home_title `   and   ` home_header `  .
Create a   ` babel.cfg `   file containing
 ` [python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
 ` Then initialize your translations with
 ` $ pybabel extract -F babel.cfg -o messages.pot .
 ` and your two dictionaries with 
```bash
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr

```
Then edit files   ` translations/[en|fr]/LC_MESSAGES/messages.po `   to provide the correct value for each message ID for each language. Use the following translations:
msgidEnglishFrench ` home_title `  ` "Welcome to Holberton" `  ` "Bienvenue chez Holberton" `  ` home_header `  ` "Hello world!" `  ` "Bonjour monde!" ` Then compile your dictionaries with
 ` $ pybabel compile -d translations
 ` Reload the home page of your app and make sure that the correct messages show up.
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x0A-i18n ` 
* File: ```bash
3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo
```

 Self-paced manual review  Panel footer - Controls 
### 4. Force locale with URL parameter
          mandatory         Progress vs Score  Task Body In this task, you will implement a way to force a particular locale by passing the   ` locale=fr `   parameter to your app’s URLs.
In your   ` get_locale `   function, detect if the incoming request contains   ` locale `   argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.
Now you should be able to test different translations by visiting   ` http://127.0.0.1:5000?locale=[fr|en] `  .
Visiting  ` http://127.0.0.1:5000/?locale=fr `  should display this level 1 heading:  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/f958f4a1529b535027ce.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220707%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220707T192845Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bcc6721cab16ee0bbbd648f6ea49734fc150db7a9e878760a6c0b1cc36ac3265) 

 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x0A-i18n ` 
* File:  ` 4-app.py, templates/4-index.html ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Mock logging in
          mandatory         Progress vs Score  Task Body Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in   ` 5-app.py `  .
```bash
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

```
This will mock a database user table. Logging in will be mocked by passing   ` login_as `   URL parameter containing the user ID to log in as.
Define a   ` get_user `    function that returns a user dictionary or   ` None `   if the ID cannot be found or if   ` login_as `   was not passed.
Define a   ` before_request `   function and use the   ` app.before_request `   decorator to make it be executed before all other functions.   ` before_request `   should use   ` get_user `   to find a user if any, and set it as a global on   ` flask.g.user `  .
In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.
msgidEnglishFrench ` logged_in_as `  ` "You are logged in as %(username)s." `  ` "Vous êtes connecté en tant que %(username)s." `  ` not_logged_in `  ` "You are not logged in." `  ` "Vous n'êtes pas connecté." ` Visiting  ` http://127.0.0.1:5000/ `  in your browser should display this:
 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/2c5b2c8190f88c6b4668.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220707%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220707T192845Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=eaa4ea10035b4aebce797e3bbdce85eae828ef332aa9f5ac537c55f19703d51a) 

Visiting  ` http://127.0.0.1:5000/?login_as=2 `  in your browser should display this:  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/277f24308c856a09908c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220707%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220707T192845Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=70b6dafe4a43eb09c240d05931decd2e529fc6a430ba4fb5b8d9da7e34684fb9) 

 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x0A-i18n ` 
* File:  ` 5-app.py, templates/5-index.html ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Use user locale
          mandatory         Progress vs Score  Task Body Change your   ` get_locale `   function to use a user’s preferred local if it is supported.
The order of priority should be
Locale from URL parametersLocale from user settingsLocale from request headerDefault localeTest by logging in as different users
 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/3/9941b480b0b9d87dc5de.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220707%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220707T192845Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=17f4ec4d7f4093fb1b22da52e89d7b5a063c4246a63afa95209344c8fc7a3c2e) 

 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x0A-i18n ` 
* File:  ` 6-app.py, templates/6-index.html ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Infer appropriate time zone
          mandatory         Progress vs Score  Task Body Define a   ` get_timezone `   function and use the   ` babel.timezoneselector `   decorator.
The logic should be the same as   ` get_locale `  :
Find  ` timezone `  parameter in URL parametersFind time zone from user settingsDefault to UTCBefore returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use   ` pytz.timezone `   and catch the   ` pytz.exceptions.UnknownTimeZoneError `   exception.
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-web_back_end ` 
* Directory:  ` 0x0A-i18n ` 
* File:  ` 7-app.py, templates/7-index.html ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 1 advanced task now!](https://intranet.hbtn.io/projects/631/unlock_optionals) 

Ready for a  manual review
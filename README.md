# MOOC Aggregator Restful API

This project is a restful api over various MOOC APIs. This restful api can be
used to create one's own online course aggregator app

| Build Status |
| ------------ |
| [![Build Status](https://travis-ci.org/ueg1990/mooc_aggregator_restful_api.svg?branch=master)](https://travis-ci.org/ueg1990/mooc_aggregator_restful_api)|

# Dependencies
To install, run:
   
     $ pip install -r requirements.txt

# Usage
To run app locally in debug mode,

    $ python main.py
     * Running on http://127.0.0.1:5000/
 	 * Restarting with reloader

Now head over to http://127.0.0.1:5000/, and you should see your hello world greeting

If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. To make app visible from a remote server, example Digital Ocean, change the call of the run() method in main.py to look like this:

    app.run(host='0.0.0.0')
    
This tells your operating system to listen on all public IPs. Doing this is useful for developing and testing remotely. 

Once server is running, you can open a new console window/tab and use curl to make API requests:

    curl -i http://127.0.0.1:5000/  
    
You should see the following output:

    HTTP/1.0 200 OK
	Content-Type: text/html; charset=utf-8
	Content-Length: 15
	Server: Werkzeug/0.9.6 Python/2.7.3
	Date: Thu, 23 Oct 2014 21:06:38 GMT

	Hello World!!!

# Tests

To run individual tests, under the pypoker parent folder,

    $ python -m unittest tests.<module name>

To run all the tests, under the pypoker parent folder, just do:

    $ python -m unittest discover tests -v

To run all tests using nose,

    $ nosetests -v tests

To run all tests using nose and coverage,

    $ nosetests -v --with-coverage --cover-package=mooc_aggregator_restful_api --cover-inclusive --cover-erase tests

# PEP 8 Test

Whole project:

    $ pep8 --exclude=LICENSE*,*.txt,*.md,*.pyc,.svn,CVS,.bzr,.hg,.git,__pycache__ --ignore=E501 * 

A specific file:

    $ pep8 --exclude=LICENSE*,*.txt,*.md,*.pyc,.svn,CVS,.bzr,.hg,.git,__pycache__ --ignore=E501 <path_to_file> 

# Author

Usman Ehtesham Gul - <uehtesham90@gmail.com>

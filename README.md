# Custom upload handler
Aim of project is to demonstrate problem of immutablelist in request.upload_handlers object when request method is POST

## Setup
```bash
git clone git@github.com:Smoooky/custom_upload_handler.git
python -m venv venv
source venv/bin/activate
pip install requirments.txt
python manage.py runserver
```
Go to http://localhost:8000/upload/
Fill the form and click Upload button
If you use a debugger and check if upload_handler is inserting during POST request you will see that 
request.upload_handler type is ImmutableList and will get 'You cannot alter upload handlers after the upload has 
been processed.' 
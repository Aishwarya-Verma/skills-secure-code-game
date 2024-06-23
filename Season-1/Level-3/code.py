# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Normalize the input path to prevent directory traversal
        normalized_path = os.path.normpath(os.path.join(base_dir, path))
        resolved_prof_picture_path = os.path.realpath(normalized_path)
        
        if not resolved_prof_picture_path.startswith(base_dir):
            return None
        
        try:
            with open(resolved_prof_picture_path, 'rb') as pic:
                picture = bytearray(pic.read())
        except FileNotFoundError:
            return None
        
        return resolved_prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        if not path:
            raise Exception("Error: Tax form is required for all users")
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        normalized_path = os.path.normpath(os.path.join(base_dir, path))
        resolved_tax_form_path = os.path.realpath(normalized_path)
        
        # Change here: Return None instead of raising FileNotFoundError
        if not resolved_tax_form_path.startswith(base_dir):
            return None
        
        try:
            with open(resolved_tax_form_path, 'rb') as form:
                tax_data = bytearray(form.read())
        except FileNotFoundError:
            return None
        
        return resolved_tax_form_path
#!fenv/bin/python
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    vendor = TextField('Vendor:', validators=[validators.required()])
    

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    
    print(form.errors)
    if request.method == 'POST':
        vendor=request.form['vendor']
        site=request.form['site']
        print(vendor)
        print(site)
 
        data = {
          "vendor": vendor,
          "site": site
        }
#         if form.validate():
#             # Save the comment here.
# #             flash('Hello ' + vendor)
#         else:
#             flash('All the form fields are required. ')
 
    return render_template('base.html', data=data, form=form)

# https://pythonspot.com/en/flask-web-forms/
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
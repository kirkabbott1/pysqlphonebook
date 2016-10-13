from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='phonebook')
app = Flask('MyApp')

@app.route('/')
def home():
    return render_template(
        'layout.html',
        title='BOOK O'' PHONE',
    )
@app.route('/list_o_entries')
def list_entries():
    query = db.query('select * from phonebook')
    return render_template(
        'list_o_entries.html',
        title='BOOK O'' PHONE',
        phonebook_list=query.namedresult()
    )

@app.route('/new_entry')
def new_phonebook_form():
    return render_template(
        'new_phonebook.html',
        title='Add Entry')

@app.route('/submit_new_entry', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    db.insert(
        'phonebook',
        name=name,
        phone_number=phone_number,
        email=email)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

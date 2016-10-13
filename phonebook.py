from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='phonebook')
app = Flask('MyApp')

@app.route('/')
def home():
    return render_template(
        'layout.html',
        title="BOOK O' PHONE",
    )
@app.route('/list_o_entries')
def list_entries():
    query = db.query('select * from phonebook')
    return render_template(
        'list_o_entries.html',
        title="BOOK O\' PHONE",
        phonebook_list=query.namedresult()
    )

@app.route('/new_entry')
def new_phonebook_form():
    return render_template(
        'new_phonebook.html',
        title='Add Entry')

@app.route('/update_entry')
def update_entry():
    id = int(request.args.get('id'))
    query = db.query('''
    select * from phonebook
    where id = %d''' % id)
    entry = query.namedresult()[0]
    return render_template(
        'update_entry.html',
        entry=entry
    )

@app.route('/submit_update_entry', methods=['POST'])
def submit_update_entry():
    id = int(request.form.get('id'))
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')
    email = request.form.get('email')
    action = request.form.get('action')
    if action == 'update':
        db.update('phonebook', {
            'id': id,
            'name': name,
            'phone_number': phone_number,
            'email': email
        })
    elif action == 'delete':
        db.delete('phonebook', { 'id': id })
    else:
        raise Exception("I don know how to %s" % action)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

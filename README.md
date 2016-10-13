#Pysql Phonebook app
You may refer to the examples in flask-examples.zip.

List Entries

Write a web application that renders all the phone book entries in your phone book database as an unordered list (ul) at the root URL: /.

Add an Entry - 1

Add a form page which takes input from the user to create a new entry in the phone book. It should have at least the fields:

name
phone number
email
The form's action attribute should point to /submit_new_entry - you will write the handler for it in the next step. This page should be displayed at the URL: /new_entry.

Add an Entry - 2

Write a form submission handler for the URL /submit_new_entry. The handler should only accept the POST method. The handler should:

Take in user input from each form field.
Use these values to insert a row into the database table.
redirect back to the root URL /.
Add an Entry - 3

Add a link from the / page that goes to /new_entry so that users at the top level page can navigate to the "Add an Entry" page.

Styling

Add some styling to the site. Change the overall font, background color, and choose a layout - either centered with top navigation bar or a two-column layout. The navigation bar should contain just 2 items: a link to the listing for all entries and a link to add a new entry. You may use bootstrap if you wish. You will want to use a layout template and template extension to reuse the layout structure across all pages.

Edit an Entry - 1

Add a form page for editing an existing entry in the database at the URL /update_entry. A id query parameter will passed to it when it is called, i.e. /update_entry?id=4 to specify which entry to update. It should pre-populate the form with the entry's existing values. It's action attribute will point to the /submit_update_entry URL - you will write the handler for it in the next step. You will need to pass the id to the /submit_update_entry handler for it to know which database entry to update, to do that use a hidden input field.

Edit an Entry - 2

Write a form submission handler for the URL /submit_update_entry. It should

Get user input from the form.
Update the entry in the database.
Redirect back to the root URL /.
Edit an Entry - 3

In the List Entries page on /, for each entry, add an "edit" link that goes to the /update_entry URL with the corresponding id query parameter, such as /update_entry?id=4.

Delete an Entry

In the /update_entry page, you will add a "Delete entry" button into the same form to give the option of deleting the entry. To do this, you will give both submit buttons a name attribute of "action" and give them different values for their "value" attribute. The /submit_update_entry handler will differentiate between whether to update or delete based on the value of the action form parameter. If the action is delete, delete the entry from the database.

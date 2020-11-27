# Import Flask and render-template.
from flask import Flask, render_template, request, redirect
app=Flask(__name__)

# Store all dictionary items
list_of_dicts = []

# Add function for Route 'Sign-Up'

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form
        print(req)

        return redirect('/')

    return render_template('signup.html', title = 'Sign-Up')

# Add function for Home

@app.route("/data", methods=['GET', 'POST'])
def data():
    req = request.form
    name = req.get("name")
    dept = req.get("dept")
    email = req.get("email")
    password = req.get("password")

    my_dict = {'name': name,
               'dept': dept,
               'email': email,
               'password': password}

    list_of_dicts.append(my_dict)

    print(req)
    return render_template('data.html', title = 'Dictionary Data', my_data=list_of_dicts)


app.run(debug=True)
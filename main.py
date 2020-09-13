#
#
# Alex Diker
#
#
#
#
# Tutorial for Interns, and other Python learners.
#
#

from flask import Flask, request
from sdwan_webui.processing import do_calculation, ssh_connection

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        ip1 = None
        number1 = None
        number2 = None
        try:
            number1 = (request.form["number1"])
            ip1 = (request.form['ip1'])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = (request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None and ip1 is not None:
            result = do_calculation(number1, number2)
            ssh_connection(ip1, username=number1, password=number2)
            return '''
                <html>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to run script again</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
        <title>SDWAN Dashboard</title>
        <!-- CSS only -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
            <body><center>
                {errors}
                <p>Enter your IP Number:</p>
                <form method="post" action=".">
                    <p><input name="ip1" /></p>
                <p>Enter username and password:</p>
                    <p><input name="number1" /></p>
                    <p><input type="password" name="number2" /></p>
                    <p><input type="submit" value="Run Script" /></p>
                    <br>
                </form>
                </center>
            </body>
        </html>
    '''.format(errors=errors)


if __name__ == '__main__':
    app.run(debug=True)

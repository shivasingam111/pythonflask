#raj project
from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__,template_folder='templates')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskpj'

mysql = MySQL(app)


#app is object reference using decorator we are passin to route.
@app.route('/',methods=['GET','POST'])

#note when ever u face the jinga template issue ref: https://www.codegrepper.com/code-examples/whatever/jinja2.exceptions.templatenotfound%3A+templates%2Findex.html
#create the Templates the folder and move the entire data to that folder
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        con = mysql.connection.cursor()
        con.execute("INSERT INTO users (name,email) VALUES (%s,%s)", (username, email))
        mysql.connection.commit()
        con.close()
        return "suceess"
    return render_template('index.html')

@app.route('/users')
def my_users():
    con = mysql.connection.cursor()
    users = con.execute("SELECT * FROM users")
    if users > 0:
        userdetails = con.fetchall()
        print(userdetails)
        return render_template('users.html',userdetails=userdetails)     
if __name__ == '__main__':
       app.run(debug=True)
#debug=True we can use for auto save will reflect on browser
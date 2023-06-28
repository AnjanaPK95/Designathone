from flask import Flask,render_template,request
import mysql.connector
#user_dict={'admin':'1234','user':'5678'}
conn = mysql.connector.connect(host='localhost',user='root',password='',database='ABCEDU')
mycursor=conn.cursor()
#create a flask application
app = Flask(__name__)

#Define the route 

@app.route('/')
def home1():
    return render_template('home1.html')

@app.route('/home1')
def backhome():
    return render_template('home1.html')

@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    query="SELECT * FROM STUDENT WHERE EMAIL = %s AND PASSWORD = %s"
    values=username,password
    mycursor.execute(query,values)
    account=mycursor.fetchall()
    if account:
        msg ='Logged in successfully!'
        return render_template('userhome.html',msg = msg)
    else:
        msg = 'Incorrect Username or Password!'

    return render_template('login.html',msg=msg)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register',methods=['POST'])
def register():
    stname=request.form['stdname']
    address=request.form['stdaddress']
    gender=request.form['gender']
    phone=request.form['phone']
    email=request.form['email']
    password=request.form['password']
    query ="INSERT INTO STUDENT(ST_NAME,ADDRESS,GENDER,PHONE,EMAIL,PASSWORD) VALUES(%s,%s,%s,%s,%s,%s)"
    data=(stname,address,gender,phone,email,password)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('/signup.html',addmsg='Success!!Login to explore..')

@app.route('/courses')
def courses():
    query="SELECT * FROM COURSE"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('courses.html',sqldata=data)
#Run the flask app
if __name__=='__main__':
    app.run(debug = True)
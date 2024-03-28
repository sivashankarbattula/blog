 from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "Homepage of Blog"
@app.route("/reg",methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        mobile=request.form['mobile']
        address=request.form['address']
        email=request.form['email']
        password=request.form['password']
        print(username)
    return render_tempiate('registaer.html')  
app.run()    
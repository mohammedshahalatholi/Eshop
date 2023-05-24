from flask import *
import pymysql

app = Flask(__name__)
app.secret_key="qqqq"
con = pymysql.connect(host="localhost", user="root", password="", port=3306, db="product")
cmd = con.cursor()
# ----------------------Login process started---------------------------------
@app.route("/")
def login():
    return render_template('login.html')
# ----------------------Login process ended---------------------------------
# ---------------------Product processing area started------------------------------------
@app.route("/productview")
def productview():
    sid=request.args.get('sid')
    print(sid)
    session['sid']=sid
    cmd.execute("SELECT * FROM product WHERE sid='"+str(session['sid'])+"'")
    s=cmd.fetchall()
    # print(s)
    return render_template('home.html',VAL=s)
    

@app.route("/add")
def add():
    return render_template('addproduct.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')
# ----------------------Product processing area ended---------------------------------
# ----------------------Shop adding process started---------------------------------
@app.route("/shops")
def shops():
    cmd.execute("SELECT * FROM shops")
    s=cmd.fetchall()
    return render_template('shops.html',VAL=s)

@app.route("/shopformview")
def shopformview():
    return render_template('shopformview.html')



@app.route("/adminpage")
def adminpage():
    cmd.execute("SELECT * FROM shops")
    s=cmd.fetchall()
    return render_template('adminpage.html',val=s)

@app.route('/addshop',methods=['get','post'])
def addshop():
    sname = request.form['sname']
    splace = request.form['splace']
    simage = request.form['simage']
    cmd.execute("insert into shops values(sid,'"+sname+"','"+splace+"','"+simage+"')")
    con.commit()
    return '''<script>alert("Shop registration successfull");window.location="/"</script>'''

@app.route("/shopview")
def shopview():
    cmd.execute("SELECT * FROM shops")
    s=cmd.fetchall()
    # print(s)
    return render_template('shops.html',VAL=s)

@app.route('/updateshop',methods=['get','post'])
def updateshop():
    sid=request.args.get('sid')
    print("sid is"+sid)
    sname = request.form['sname']
    splace = request.form['splace']
    simage = request.form['simage']
    cmd.execute("update shops set sname='"+sname+"',splace='"+splace+"',simage='"+simage+"' where sid='"+str(sid)+"'")
    con.commit()
    return '''<script>alert("updated successfully");window.location="/shops"</script>'''

@app.route('/deleteshop',methods=['get','post'])
def deleteshop():
    sid=request.args.get('sid')
    print(sid)
    cmd.execute("delete from shop where id='"+str(sid)+"'")
    con.commit()
    return '''<script>alert("deleted successfully");window.location="/"</script>'''

# ----------------------Shop adding  processing area ended---------------------------------
# ----------------------Admin page started---------------------------------
@app.route("/editproduct")
def editproduct():
     cmd.execute("SELECT * FROM product")
     s=cmd.fetchall()
     return render_template('editshopitem.html',val=s)

    # return "<p>Hello, World!</p>"

@app.route('/addproduct',methods=['get','post'])
def addproduct():
    Fname = request.form['fname']
    price = request.form['price']
    image = request.form['image']
    cmd.execute("insert into product values(id,'"+Fname+"','"+price+"','"+image+"','"+str(session['sid'])+"')")
    con.commit()
    return '''<script>alert("registration successfull");window.location="/"</script>'''

@app.route('/updateproduct',methods=['get','post'])
def updateproduct():
    id=request.args.get('id')
    print("id is"+id)
    name = request.form['name']
    price = request.form['price']
    image = request.form['image']
    cmd.execute("update product set name='"+name+"',price='"+price+"',image='"+image+"' where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("updated successfully");window.location="/productview"</script>'''

@app.route('/deleteproduct',methods=['get','post'])
def deleteproduct():
    id=request.args.get('id')
    print(id)
    cmd.execute("delete from product where id='"+str(id)+"'")
    con.commit()
    return '''<script>alert("deleted successfully");window.location="/"</script>'''
# ----------------------Admin page ended---------------------------------
if __name__ == '__main__':
     app.run()

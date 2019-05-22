from flask import Flask, render_template, request, json, redirect, url_for, flash
import pymysql
import secrets
app = Flask(__name__)


app.config['SECRET_KEY'] = 'y5JX0bC0Vp3-HpB_RsjYJg'
db=pymysql.connect("localhost","Deniro","Deniro09","harrypotter")
cursor = db.cursor()


@app.route('/Home')
def Home():
    db = pymysql.connect("localhost", "Deniro", "Deniro09", "harrypotter")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM wizards")
    records = cursor.fetchall()
    cursor.close()
    return render_template("Home.html",title="aa",records=records)


@app.route('/')
@app.route('/HomePage',methods=['GET','SET'])
def HomePage():
   return render_template("HomePage.html")





@app.route('/Create', methods=['POST'])
def Create():
    db = pymysql.connect("localhost", "Deniro", "Deniro09", "harrypotter")
    cursor = db.cursor()
    if request.method == 'POST':
      Name = request.form['Name']
      Surname = request.form['Surname']
      Wizard_House = request.form['Wizard_House']
      Wand_Type = request.form['Wand_Type']
      Wizard_Club = request.form['Wizard_Club']
      cursor.execute("INSERT INTO wizards(Name,Surname,Wizard_House,Wand_Type,Wizard_Club) VALUES('%s','%s','%s','%s','%s')"
      %(Name, Surname, Wizard_House, Wand_Type, Wizard_Club))
      db.commit()
      cursor.close()
      flash("Wizard Inserted Successfully")
    return redirect(url_for("Home"))






@app.route('/Delete/<string:id_data>/',methods=['GET'])
def Delete(id_data):
    flash("Wizard Has Been Deleted Successfully")
    db = pymysql.connect("localhost", "Deniro", "Deniro09", "harrypotter")
    cursor = db.cursor()
    cursor.execute("DELETE FROM wizards WHERE ID=%s", (id_data,))
    db.commit()

    return redirect(url_for("Home"))

@app.route('/Update',methods=['POST','GET'])
def Update():
    db = pymysql.connect("localhost", "Deniro", "Deniro09", "harrypotter")
    cursor = db.cursor()

    if request.method == 'POST':
     id_data = request.form['id']
     Name = request.form['Name']
     Surname = request.form['Surname']
     Wizard_House = request.form['Wizard_House']
     Wand_Type = request.form['Wand_Type']
     Wizard_Club = request.form['Wizard_Club']
     cursor.execute(""" UPDATE wizards SET Name=%s, Surname=%s, Wizard_House=%s, Wand_Type=%s, Wizard_Club=%s WHERE ID=%s""",
     (Name, Surname, Wizard_House, Wand_Type, Wizard_Club,id_data))
     db.commit()
     flash("Wizard Updated Successfully")
    return redirect(url_for("Home"))


@app.route('/Search',methods=['POST','GET'])
def Search():
     db = pymysql.connect("localhost", "Deniro", "Deniro09", "harrypotter")
     cursor = db.cursor()
     Search = request.form['Search']
     cursor.execute("SELECT * FROM wizards WHERE (Name=%s) OR (Surname=%s) OR (Wizard_House=%s) OR (Wand_Type=%s) OR  (Wizard_Club=%s)  ",
     (Search,Search,Search,Search,Search))
     records = cursor.fetchall()
     if records ==  None:
      flash("No Wizarding Information Found ")

      cursor.close()
     return render_template("Home.html", title="aa", records=records)


@app.route('/Wands',methods=['GET','SET'])
def Wands():
    return render_template("Wands.html")

@app.route('/Houses',methods=['GET','SET'])
def Houses():
    return render_template("House.html")


db.close()

if __name__ == '__main__':
      app.run(debug=True)


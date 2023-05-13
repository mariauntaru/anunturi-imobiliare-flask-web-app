from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQLdb
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

import mysql.connector
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from flask_login import current_user

login_manager = LoginManager()
conn = mysql.connector.connect(host = "localhost", port = "3306", user = "root", password = "untaru", database = "anunturi")
cursor = conn.cursor()
app = Flask(__name__)
app.config["SECRET_KEY"]="M"

@app.route("/index/admin")
def administrator():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    elif session["userid"] != 1:
        return redirect(url_for('index'))
    return render_template("admin.html")

@app.route("/index")
def index():
    if session['loggedin'] == False:
        return redirect(url_for('login'))
    return render_template("index.html", value = session['userid'])

@app.route("/recente")
def recente():
    cursor.execute("SELECT P.Zona,P.Tip_loc,P.Nr_camere,P.Descriere, A.Pret, PA.Data FROM anunturi A INNER JOIN proprietatianunturi PA ON PA.ID_anunt = A.ID_anunt INNER JOIN proprietate P ON P.ID_proprietate = PA.ID_proprietate WHERE PA.ID_proprietate NOT IN(SELECT ID_proprietate FROM contracte) ORDER BY PA.Data DESC LIMIT 3")
    value = cursor.fetchall();
    return render_template("recente.html", data = value, name = "Cele mai recente anunturi")

@app.route("/anunturi")
def anunturi():
    cursor.execute("SELECT P.Zona, P.Tip_loc, P.Nr_camere, P.Descriere, PA.Data, AN.Pret, AN.Detalii, AG.Nume, AG.Prenume, AG.Nr_telefon FROM proprietatianunturi PA INNER JOIN proprietate P ON P.ID_proprietate = PA.ID_proprietate INNER JOIN anunturi AN ON AN.ID_anunt = PA.ID_anunt INNER JOIN agenti AG ON AG.ID_agent = PA.ID_agent WHERE PA.ID_proprietate NOT IN(SELECT ID_proprietate FROM contracte)")
    value = cursor.fetchall();
    return render_template("anunturi.html", data = value, name = "Anunturi")

@app.route("/cumparat")
def cumparat():
    cursor.execute("SELECT P.Zona, P.Tip_loc, P.Nr_camere, P.Descriere, PA.Data, AN.Pret, AN.Detalii, AG.Nume, AG.Prenume, AG.Nr_telefon FROM proprietatianunturi PA INNER JOIN proprietate P ON P.ID_proprietate = PA.ID_proprietate INNER JOIN anunturi AN ON AN.ID_anunt = PA.ID_anunt INNER JOIN agenti AG ON AG.ID_agent = PA.ID_agent INNER JOIN contracte C ON C.ID_proprietate <> PA.ID_proprietate WHERE Detalii LIKE 'de cumparat'")
    value = cursor.fetchall();
    return render_template("cumparat.html", data = value, name = "Proprietati de cumparat")

@app.route("/inchiriat")
def inchiriat():
    cursor.execute("SELECT P.Zona, P.Tip_loc, P.Nr_camere, P.Descriere, PA.Data, AN.Pret, AN.Detalii, AG.Nume, AG.Prenume, AG.Nr_telefon FROM proprietatianunturi PA INNER JOIN proprietate P ON P.ID_proprietate = PA.ID_proprietate INNER JOIN anunturi AN ON AN.ID_anunt = PA.ID_anunt INNER JOIN agenti AG ON AG.ID_agent = PA.ID_agent INNER JOIN contracte C ON C.ID_proprietate <> PA.ID_proprietate WHERE Detalii LIKE 'de inchiriat'")
    value = cursor.fetchall();
    return render_template("inchiriat.html", data = value, name = "Proprietati de inchiriat")

@app.route("/vandute")
def vandute():
    cursor.execute("SELECT CL.Nume, CL.Prenume, P.Zona, P.Descriere FROM contracte CO INNER JOIN clienti CL ON CL.ID_client = CO.ID_client INNER JOIN proprietate P ON CO.ID_proprietate = P.ID_proprietate")
    value = cursor.fetchall();
    return render_template("vandute.html", data = value, name = "Proprietati vandute si clienti multumiti")

@app.route("/clienti")

def clienti():
        cursor.execute("SELECT CL.Nume, CL.Prenume, CO.Data_incheiere FROM contracte CO INNER JOIN clienti CL ON CL.ID_client = CO.ID_client")
        value = cursor.fetchall();
        return render_template("clienti.html", data=value, name = "Clienti")
 
@app.route("/proprietari")
def proprietari():
        cursor.execute("SELECT * ,(SELECT COUNT(*) FROM proprietate WHERE proprietate.ID_proprietar = proprietari.ID_proprietar) as NumarProprietati FROM proprietari")
        value = cursor.fetchall();
        return render_template("proprietari.html", data=value, name = "Proprietari")

@app.route("/proprietate")
def proprietate():
    cursor.execute("SELECT p.Zona, p.Tip_loc, p.Nr_camere, p.Descriere, pr.Nume, pr.Prenume FROM proprietate p INNER JOIN proprietari pr on pr.ID_proprietar = p.ID_proprietar")
    value = cursor.fetchall();
    return render_template("proprietate.html", data=value, name = "Proprietati")

@app.route("/agenti")
def agenti():
    cursor.execute("SELECT AG.Nume, AG.Prenume, COUNT(P.ID_proprietate) as NrProprietati FROM proprietatianunturi PA INNER JOIN agenti AG ON PA.ID_agent = AG.ID_agent INNER JOIN proprietate P ON P.ID_proprietate = PA.ID_proprietate GROUP BY AG.ID_agent")
    value = cursor.fetchall();
    return render_template("agenti.html", data=value, name = "Agenti")
 
@app.route("/contracte")
def contracte():
    cursor.execute("SELECT C.Data_incheiere, C.Pret, P.Zona, P.Tip_loc, CL.Nume, CL.Prenume FROM Contracte C INNER JOIN proprietate P ON P.ID_proprietate = C.ID_proprietate INNER JOIN clienti CL ON CL.ID_client = C.ID_client")
    value = cursor.fetchall();
    return render_template("contracte.html", data = value,name = "Contracte")

@app.route("/aparitii")
def aparitii():
    cursor.execute("SELECT P.Zona, P.Tip_loc, (SELECT COUNT(*) FROM proprietatianunturi PA WHERE PA.ID_proprietate = P.ID_proprietate) AS Nr_Aparitii FROM proprietate P")
    value = cursor.fetchall();
    return render_template("aparitii.html", data = value, name = "Aparitii")

@app.route("/buni")
def buni():
    cursor.execute("SELECT DISTINCT AG.Nume, AG.Prenume FROM agenti AG INNER JOIN proprietatianunturi PA ON PA.ID_agent = AG.ID_agent WHERE PA.ID_proprietate IN(SELECT PA.ID_proprietate FROM proprietatianunturi PA INNER JOIN contracte C ON C.ID_proprietate = PA.ID_proprietate)")
    value = cursor.fetchall();
    return render_template("buni.html", data = value, name = "Agentii cei mai recomandati")

@app.route("/insert", methods = ['GET', 'POST'])
def insert():
    return render_template("insert.html", name = "Insert")

@app.route("/insert/agent")
def insertA():
    return render_template("insertag.html")

@app.route("/insert/agent/", methods = ['GET', 'POST'])
def insertAgent():
    ID_agent = request.form["ID"]
    Nume = request.form["Nume"]
    Prenume = request.form["Prenume"]
    NrTel = request.form["Nr_telefon"]
    cursor.execute("INSERT INTO agenti VALUES (%s, %s, %s, %s)", (int(ID_agent), Nume, Prenume,NrTel))
    conn.commit()
    return redirect(url_for("index"))

@app.route("/insert/proprietate")
def insertP():
    return render_template("insertpr.html")

@app.route("/insert/proprietate/", methods = ['GET', 'POST'])
def insertProprietate():
    ID_proprietate = request.form["ID_proprietate"]
    ID_proprietar = request.form["ID_proprietar"]
    Zona = request.form["Zona"]
    Tip_loc = request.form["Tip_loc"]
    Nr_camere = request.form["Nr_camere"]
    Descriere = request.form["Descriere"]
    cursor.execute("INSERT INTO proprietate VALUES (%s, %s, %s, %s, %s, %s)", (int(ID_proprietate),int(ID_proprietar), Zona, Tip_loc, Nr_camere, Descriere))
    conn.commit()
    return redirect(url_for("index"))

@app.route("/update")
def update():
    return render_template("update.html", name = "Update")

@app.route("/update/proprietate")
def updatepr():
    return render_template("updatepr.html")

@app.route("/update/proprietate/", methods = ['GET', 'POST'])
def updateproprietate():
    ID_proprietate_vechi = request.form.get("ID_proprietate_vechi")
    Camp = request.form.get('Camp')
    Camp_update = request.form.get("Camp_update")
    if Camp == "ID_proprietate":
        try:
            q1 = "UPDATE proprietate SET ID_proprietate = (%s) " % (int(Camp_update))
            q2 = "WHERE ID_proprietate = (%s)" % (int(ID_proprietate_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()
        except:
            Camp = Camp
    elif Camp == "ID_proprietar":
        try:
            q1 = "UPDATE proprietate SET ID_proprietate = (%s) " % (int(Camp_update))
            q2 = "WHERE ID_proprietar = (%s)" % (int(ID_proprietate_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()
        except:
            Camp = Camp
    elif Camp =="Nr_camere":
        try:
            q1 = "UPDATE proprietate SET Nr_camere = (%s) " % (int(Camp_update))
            q2 = "WHERE ID_proprietate = (%s)" % (int(ID_proprietate_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()
        except:
            Camp = Camp
    elif Camp == "Zona":
            q1 = "UPDATE proprietate SET Zona = ('%s') " % (Camp_update)
            q2 = "WHERE ID_proprietate = (%s)" % (int(ID_proprietate_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()
    elif Camp == "Tip_loc":
            q1 = "UPDATE proprietate SET Tip_loc = ('%s') " % (Camp_update)
            q2 = "WHERE ID_proprietate = (%s)" % (int(ID_proprietate_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()
    elif Camp == "Descriere":
            q1 = "UPDATE proprietate SET Descriere = ('%s') " % (Camp_update)
            q2 = "WHERE ID_proprietate = (%s)" % (int(ID_proprietate_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()

    return redirect(url_for("index"))

@app.route("/update/agent/", methods = ['GET', 'POST'])
def updateagent():
    ID_agent_vechi = request.form.get("ID_agent_vechi")
    Camp = request.form.get('Camp')
    Camp_update = request.form.get("Camp_update")
    if Camp == "ID_agent":
        try:
            q1 = "UPDATE agenti SET ID_agent = (%s) " % (int(Camp_update))
            q2 = "WHERE ID_agent = (%s)" % (int(ID_agent_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()
        except:
            Camp = Camp
    elif Camp == "Nume":
            q1 = "UPDATE agenti SET Nume = ('%s') " % (Camp_update)
            q2 = "WHERE ID_agent = (%s)" % (int(ID_agent_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()
    elif Camp == "Prenume":
            q1 = "UPDATE agenti SET Prenume = ('%s') " % (Camp_update)
            q2 = "WHERE ID_agent = (%s)" % (int(ID_agent_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()
    elif Camp == "Nr_telefon":
            q1 = "UPDATE agenti SET Nr_telefon = ('%s') " % (Camp_update)
            q2 = "WHERE ID_agent = (%s)" % (int(ID_agent_vechi))
            q = q1 + q2
            cursor.execute(q)
            conn.commit()

    return redirect(url_for("index"))

@app.route("/update/agent")
def updateag():
    return render_template("updateag.html")

@app.route("/delete")
def delete():
    return render_template("delete.html", name = "Delete")

@app.route("/delete/proprietate")
def deletepr():
    return render_template("deletepr.html", name = "Delete Proprietate")

@app.route("/delete/proprietate/", methods = ['GET', 'POST'])
def deleteproprietate():
    ID_proprietate = request.form["ID_proprietate"]
    cursor.execute(f"DELETE FROM proprietate WHERE ID_proprietate = {int(ID_proprietate)}")
    conn.commit()
    return redirect(url_for('index'))

@app.route("/delete/agent")
def deleteag():
    return render_template("deleteag.html", name = "Delete Agent")

@app.route("/delete/agent/", methods = ['GET', 'POST'])
def deleteagent():
    ID_agent = request.form["ID_agent"]
    cursor.execute(f"DELETE FROM agenti WHERE ID_agent = {int(ID_agent)}")
    conn.commit()
    return redirect(url_for('index'))

@app.route("/")
@app.route("/login", methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
       # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM clienti WHERE Email=%s AND Parola=%s', (email, password))
        clienti = cursor.fetchone()
        if clienti:
            session['loggedin'] = True
            session['userid'] = clienti[0]
            session['email'] = clienti[3]
            mesage = 'Logged in successfully !'
            return redirect('index')
        else:
            mesage = 'Email sau parola incorecte !'
    return render_template('login.html', mesage = mesage)
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host="127.0.0.9", port=8080, debug=True)

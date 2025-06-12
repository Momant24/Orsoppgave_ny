from flask import Flask, render_template, request
from databaseting import db_config, get_db_connection

app = Flask(__name__)

#Gir meg en melding om databasen er koblet til

print("Database koblet til!") if get_db_connection() else print("Ingen tilkobling!")

#Ruten til første side
@app.route('/')
def index():

    return render_template('index.html')

# Ruten til faq siden    
@app.route('/faq')
def faq():
    return render_template('faq.html') 

#Ruten til navn siden og kobling til databasen for å lagre og vise antall navn
@app.route('/navn', methods=['GET', 'POST'])
def navnside():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    navn_liste = []

    if request.method == 'POST':
        navninn = request.form.get("navninn")
        if navninn:
            cursor.execute("INSERT INTO navn (navn) VALUES (%s)", (navninn,))
            conn.commit()
    print("Hei1")       
    cursor.execute("SELECT DISTINCT navn FROM navn;")
    navn_resultat = cursor.fetchall()
    print(navn_resultat)
    for rad in navn_resultat:
        navnvalg = rad['navn']
        cursor.execute("SELECT COUNT(navn) FROM navn WHERE navn = ?;", (navnvalg, ))
        resultat = cursor.fetchall()
        print(resultat)
        navn_liste.append([navnvalg, resultat])
        

    return render_template('navn.html', navn_liste=navn_liste)

@app.route('/kontaktoss', methods=['GET', 'POST'])
def kontak():
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        epostinn = request.form.get("epost")
        klageinn = request.form.get("klage")
        if epostinn:
            cursor.execute("INSERT INTO meldingtiloss (epost, klage) VALUES (%s, %s)", (epostinn, klageinn))
            conn.commit()
    
    return render_template('kontaktoss.html')
    


if __name__ == '__main__':
    app.run(debug=True)
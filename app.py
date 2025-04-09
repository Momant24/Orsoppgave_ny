from flask import Flask, render_template, request
from databaseting import db_config, get_db_connection

app = Flask(__name__)

print("✅ Database koblet til!") if get_db_connection() else print("❌ Ingen tilkobling!")

@app.route('/', methods=['GET', 'POST'])
def index():
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
        

    
    #navn_resultat = cursor.fetchall()
    #cursor.close()
    #conn.close()

    #defult_liste = [rad['navn'] for rad in navn_resultat]


    

    return render_template('index.html', navn_liste=navn_liste)

    
    

        
    
if __name__ == '__main__':
    app.run(debug=True)
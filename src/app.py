from flask import Flask, request, render_template
import psycopg2
import re

app = Flask(__name__)

# change to fit your own database
db = "dbname='XXX' user='XXX' host='localhost' password='XXX'"
conn = psycopg2.connect(db)
cursor = conn.cursor()

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search')
def search():
    query = request.args.get('query')
    if query:
        if not re.match(r'^[a-zA-Z0-9\s]+$', query):
            raise Exception("Invalid query") # can test with 𡨸
        cur = conn.cursor()
        cur.execute('SELECT title, rating FROM Titles_Ratings WHERE title LIKE %s', ('%' + query + '%',))
        titles = cur.fetchall()
        return render_template('index.html', titles=titles)
    else:
        return render_template('search.html')

@app.route('/rate', methods=['POST'])
def rate():
    title = request.form.get('title')
    rating = request.form.get('rating')
    cur = conn.cursor()
    cur.execute('UPDATE Titles_Ratings SET rating = %s WHERE title = %s', (rating, title))
    conn.commit()
    return "Rating updated succesfully"
    
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'
    # mars = mongo.db.mars.find_one()
    # return render_template('index.html', surfing=surfing)

@app.route('/scrape')
def scrape():
    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    
    # Define database and collection
    db = client.mars
    collection = db.items
    key = {'key':'value'}
    
    # Scrape data
    data = scrape_mars.scrape()
    collection.update(key, data, upsert=True)
    
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
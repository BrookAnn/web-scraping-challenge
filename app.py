from flask import Flask, render_template, redirect
from pymongo import MongoClient
import MarsMission

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = MongoClient("mongodb://localhost:27017/scraped")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    scraped_data = mongo.db.scraped_data.find_one()

    # Return template and data
    return render_template("index.html", scraped=scraped_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    data_scraped = MarsMission.data_scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.scraped_data.update({}, data_scraped, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

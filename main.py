import random
from flask import Flask, render_template
import os
app = Flask(__name__)
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. - James Cameron"
]
@app.route('/')
def quote_of_the_day():
  quote = random.choice(quotes)
  return render_template('index.html', quote=quote)
  
if __name__ == "__main__":
  port = int(os.environ.get('PORT', 3030))
  app.run(debug=True, host='0.0.0.0', port=port)
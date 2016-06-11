from flask import Flask, render_template, redirect, request
app = Flask(__name__)

email_addresses = []

@app.route('/')
def home():
  author = "My"
  name = "You"
  return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
  email = request.form['email']
  gender = request.form['gender']
  email_addresses.append((email, gender))
  print(email_addresses) 
  return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == '__main__':
  app.run()

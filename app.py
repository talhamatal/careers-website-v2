from flask import Flask, render_template

app = Flask(__name__)

JOBS = [ 
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Lahore Pakistan',
    'salary': 'Rs 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'New York USA',
    'salary': '$150,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote USA'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Remote USA',
    'salary': '$140,000'
  }
]

@app.route("/")
def hello_talha():
  return render_template('home.html', jobs=JOBS, company_name='Talman')

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

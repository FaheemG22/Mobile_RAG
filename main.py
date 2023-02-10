from flask import *  # imports all the proper functions from the flask library
import pandas as pd

app = Flask(__name__)

users = {}  # Creates a dictionary to find unique user inputs


@app.route('/')  # / is home page
def index():
    client_ip = request.remote_addr
    if client_ip not in users.keys():
        users[client_ip] = [0, 0, 0]

    return render_template('index.html')


@app.route("/", methods=["POST"])
def colours():
    client_ip = request.remote_addr
    users[client_ip] = [0, 0, 0]
    if request.form.get('Red'):
        print(users)
        users[client_ip][0] += 1
    if request.form.get('Amber'):
        users[client_ip][1] += 1
    if request.form.get('Green'):
        users[client_ip][2] += 1
    print(users[client_ip])
    with open('RAG.csv','a') as f:
        f.write(f'\n{client_ip},{users[client_ip][0]},{users[client_ip][1]},{users[client_ip][2]}')

    return render_template('index.html')



@app.route('/tutor')
def tutor():
    f = pd.read_csv('RAG.csv')

    return  f'<h2>users : {sum(f["R"])+sum(f["A"])+sum(f["G"])}</h2>' + \
           f"Red : {sum(f['R'])}" \
           f"<br> Amber:{sum(f['A'])}" \
           f"<br> Green:{sum(f['G'])}"
"""
f'<table>' \
f'<th> IP' \
f'</th>' \
f'<th> Red' \
f'</th>' \
f'<th> Amber' \
f'</th>' \
f'<th> Green' \
f'</th>' \
f'<tr>' \
f'<td>{f["user_ip"][0]} </td> <td>{sum(f["R"])} </td> <td>{sum(f["A"])} </td> <td>{sum(f["G"])} </td>' \
f'</tr>' \
f'</table>'

"""



if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/api/classement/add", methods=['POST'])
def add():
    new_team = request.get_json(force=True)
    if "Equipe" in new_team:
        equipe = new_team["Equipe"]
    if "Points" in new_team:
        points = new_team["Points"]
    return ("OK", {"Content-Type": "application/plaintext"})


@app.route('/api/classement/')
def classement():
    dico_L1 = {
        'titre': 'Classement Ligue 1',
        'classement' : {'PSG':58, 'OM':49, 'Rennes':41, 'LOSC':40}
    }
    return jsonify(dico_L1)


@app.route('/api/classement/allinterventions')
def interventions():
    lst = [{'id':5, 'client':'dupont', 'panne':'frigo 345'}, {'id':3, 'client':'gilles', 'panne':'télé'}]
    return jsonify(lst)


if __name__ == '__main__':
    app.run()

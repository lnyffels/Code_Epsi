from flask import Flask, request, Response, jsonify
import json

from EasySAV.EasySAV.Use_cases.Intervention_list_use_case import *
from EasySAV.EasySAV.Use_cases.Intervention_save_use_case import *
from EasySAV.UserInterfaces.data import *
from EasySAV.EasySAV.Repository.Dbrepo import *
from EasySAV.EasySAV.Repository.Memrepo import *
from EasySAV.EasySAV.Serializers.intervention_json_serializer import InterventionJsonEncoder


app = Flask(__name__)

@app.route('/interventions', methods=['GET'])
def interventions():
    #repo = MemRepo([intervention1, intervention2, intervention3])
    repo = Dbrepo(r"c:\temp\interventions.db")
    use_case = InterventionUseCase(repo)
    liste_interventions = use_case.execute()
    if type(repo) is MemRepo:
        return Response(json.dumps(liste_interventions, cls=InterventionJsonEncoder), mimetype='application/json',
                    status=200)
    else:
        return jsonify(liste_interventions)

@app.route("/add", methods=['POST'])
def add_intervention():
    try:
        interv = request.get_json(force=True)
        repo = Dbrepo(r"c:\temp\interventions.db")
        use_case = InterventionSaveUseCase(repo)
        response = use_case.execute(interv)
        return ("{}".format(str(response)), {"Content-Type": "application/plaintext"})
    except Exception as exc:
        return (str(exc), 400, {})




if __name__ == '__main__':
    app.run()

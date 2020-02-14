from flask import Flask, render_template, request
from Tarificateur.model.simulateur import Simulateur
from Tarificateur.model.request import Request
from Tarificateur.model.response import Response
from Tarificateur.model.enum_formule import Formule
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/resultat_dentaire')
def resultat_dentaire():
    return render_template('404.html'), 404

@app.route('/resultat_optique')
def resultat_optique():
    return render_template('404.html'), 404


@app.route('/')
def question():
    return render_template("questionnaire_hopital.html")


@app.route('/resultat_hopital',methods = ['POST'])
def resultat_hopital():
  try:
      result = request.form
      req = Request()
      req.formule = result['formule']
      req.prestation = result['prestation']
      req.depenses = float(result['depense'])
      req.regime_alsace_moselle = result['alsace']
      req.dptam = result['dptam']
      sim = Simulateur(req)
      res = sim.calculer_remboursements()
      return render_template("resultat_hopital.html",
                             prestation=Formule.titre_prestation(req.prestation),
                             depense= req.depenses,
                             rac_avant=res.rac_avant_axa,
                             formule=Formule.titre_formule(req.formule),
                             secu=res.base_secu, axa_secu=res.axa_plus_secu, rac=res.rac_prospect)
  except Exception as exc:
      return render_template("erreur.html", message=exc)

if __name__ == '__main__':
    app.config.from_object('config')
    app.run(host='localhost', debug=True)
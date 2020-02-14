# Created by S611372 at 29/11/2019
Feature: Lister_mes_comptes
  # Enter feature description here
  EN TANT QUE client de la banque
  JE VEUX connaitre la liste de mes comptes
  AFIN DE pouvoir effectuer des virements

  Scenario: Renvoyer_liste_comptes
    # Enter steps here
    Given je suis connecté à mon application de getion de compte
    When je demande la liste de mes comptes
    Then j'obtiens la liste suivante
    | num_compte  | nom_compte        | type_compte | interets  |
    | 123         | compte courant    | courant     | 0         |
    | 456         | CEL               | epargne     | 0.5       |

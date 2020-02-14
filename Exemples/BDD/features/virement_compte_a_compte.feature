# Created by S611372 at 04/12/2019
Feature: Virement_compte_a_compte
  # Enter feature description here
  En tant que Client de la banque ALM
  Je veux virer une somme d'un de mes comptes vers un autre de mes comptes
  afin de crediter un compte epargne

  Scenario: Virer_compte_A_vers_B
    # Enter steps here
    Given J'ai un compte_A avec un solde de 1000 euros
    Given J'ai un compte_B avec un solde de 0 euros
    When Je vire 150.00 euros du compte_A vers le compte_B
    Then le solde de mon compte_A est de 850.00 euros
    And  le solde de mon compte_B est de 150.00 euros
    And le virement est confirmé
# Created by Laurent at 15/11/2019
Feature: virer_compte_simple

  EN TANT QUE client de la banque
  JE PEUX effectuer un virement depuis mon compte courant
  AFIN DE d'alimenter un compte épargne


  Scenario: virement_simple
    # Enter steps here
    Given mon compte courant_123 a un solde de 280.50 euros
    Given mon compte epargne_CEL a un solde de 1200.00 euros
    When je vire 100 euros de mon compte courant_123 vers mon compte epargne_CEL
    Then alors mon compte courant_123 a un solde de 180.50
    And  mon compte epargne_CEL a un solde de 1300.00 euros

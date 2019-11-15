# Created by Laurent at 15/11/2019
Feature: Crediter_compte
  """
  EN TANT QUE client de la banque
  JE PEUX créditer mon compte courant
  AFIN DE l'alimenter
  """

  Scenario: credit_simple
    # Enter steps here
    Given mon compte courant_123 a un solde de 0 euros
    When je credite mon compte courant_123 de 150 euros
    Then le solde de mon compte courant_123 est de 150 euros

# Created by Laurent at 15/11/2019
@banque
Feature: Crediter_compte

  EN TANT QUE client de la banque
  JE PEUX créditer mon compte courant
  AFIN DE l'alimenter

  REGLE : credit_simple :
    solde = somme(montant des operations)

  Scenario Outline: credit_simple

    Given mon compte courant_123 a un solde de <montant_init> euros
    When je credite mon compte courant_123 de <operation_init> euros
    Then le solde de mon compte courant_123 est de <solde_init> euros

    Examples: 2_operations_credit
    | montant_init  | operation_init  | solde_init     |
    | 55.00         | 150.00          | 215.00         |
    | -150.00       | 10.00           | -140.00        |
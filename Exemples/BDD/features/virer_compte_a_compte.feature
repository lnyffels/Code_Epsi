# Created by Laurent at 15/11/2019
Feature: virer_compte_simple

  EN TANT QUE client de la banque
  JE PEUX effectuer un virement depuis mon compte courant
  AFIN DE d'alimenter un compte épargne



  Scenario Outline: virement_simple
    # Enter steps here
    Given mon compte courant_123 a un solde de <init_montant_courant> euros
    Given mon compte epargne_CEL a un solde de <init_montant_epargne> euros
    When je vire <montant> euros de mon compte courant_123 vers mon compte epargne_CEL
    Then alors mon compte courant_123 a un solde de <solde_courant> euros
    And mon compte epargne_CEL a un solde de <solde_epargne> euros

    Examples: 2_transfers
    | init_montant_courant  | init_montant_epargne  | montant     | solde_courant | solde_epargne |
    | 300.00                | 1200.00               | 100.00      | 200.00        | 1300.00       |


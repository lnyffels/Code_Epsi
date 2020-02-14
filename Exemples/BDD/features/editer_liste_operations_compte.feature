# Created by S611372 at 28/11/2019
Feature: US1 - Lister_operations
  # Enter feature description here
  EN TANT QUE Client de la banque titulaire d'un compte courant
  JE VEUX obtenir la liste de mes opérations sur les 30 derniers jours
  AFIN DE vérifier mes comptes

  Scenario: lister_operations_trier_date_décroissante
    # Enter steps here
    Given je dispose du compte courant_123
    When je souhaite obtenir la liste de mes opérations des trente derniers jours
    Then le systeme me donne la liste des dernieres operations triées par date
      | date_operation | description      | type_operation | montant  |
      | 25/11/2019     | achat livre      | Débit          | 25.63    |
      | 24/11/2019     | réglement EDF    | Débit          | 152.50   |


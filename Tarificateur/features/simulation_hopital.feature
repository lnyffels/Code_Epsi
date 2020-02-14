# Created by S611372 at 09/12/2019
Feature: Simulation_frais_hopital
  # Enter feature description here
  En tant que Prospect
  Je veux simuler le remboursement de mes frais d'hospitalisation
  afin de connaitre le niveau de remboursement des formules d'AXA


  Scenario Outline: calculer_remboursements_hospi_selon_formules_AXA
    Given je ne releve pas du régime Alsace Moselle
    Given mon médécin Le médecin a adhéré à un Dispositif de Pratique TArifaire Maitrisée
    Given ma prestation choisi <prestation>
    Given Le montant simulé pour mes dépense est <depenses> euros
    Given la formule AXA choisit est <formule>
    When Je calcule mes remboursements
    Then la base de remboursement Sécurité sociale est de <base_secu> euros
    And  le reste à charge avant la formule AXA est de <rac_avant_axa> euros
    And le remboursement AXA plus Sécu est de <axa_plus_secu> euros
    And le reste à charge est de <rac_prospect> euros

    Examples: appendicite_chirurgien_ma_sante_hospi_tradi
    | prestation       | depenses | formule     | base_secu  | rac_avant_axa | axa_plus_secu | rac_prospect |
    | APPENDICITE_CHIR | 450      | MA_HOSPI_NR | 187.89     | 262.11        | 450.00        | 0.0          |
    | APPENDICITE_CHIR | 890.60   | MA_HOSPI_NR | 187.89     | 702.71        | 751.56        | 139.04       |
    #| APPENDICITE_CHIR | 450      | MA_100_NR   | 187.89     | 262.11        | 187.89        | 262.11       |

    Examples: appendicite_anesthesiste_ma_sante_hospi_tradi
    | prestation       | depenses | formule     | base_secu  | rac_avant_axa | axa_plus_secu | rac_prospect |
    | APPENDICITE_ANES | 367      | MA_HOSPI_NR | 103.64     | 263.36        | 367.00        | 0.0          |
    | APPENDICITE_ANES | 901.69   | MA_HOSPI_NR | 103.64     | 798.05        | 414.56        | 487.13       |


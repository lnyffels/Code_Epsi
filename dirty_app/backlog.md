# US#1 : Debit compte
En tant que Client

Je souhaite réaliser un débit sur mon compte

Afin de récupérer de l'argent

### Règle 1.1 : débit simple
Solde de 2000 euros, débit 100 euros => 1900 euros
### Règle 1.2 : controle valeur négative
Solde de 1400 euros, débit -100 euros => 1400 euros
### Règle 1.3 : débit plafonné à 10 000 
Solde de 450.55 euros, débit 10001 euros => 450.55 euros
Message dans fichier fraude.txt => alerte mouvement douteux : 10001 


# US#2 : Crédit Compte
En tant que Client

Je souhaite créditer mon compte

Afin d'épargner

### Règle 2.1 : credit simple
Solde de 1500 euros, crédit 250 euros => 1750.0 euros
### Règle 2.2 : controle du "0"
Solde de 0 euros, dépot 0 euros => 00 euros
### Règle 2.3 : crédit plafonné à 10 000 
Solde de 1500 euros, débit 12000 euros => 1500 euros



# US#3: Opérations entre 2 dates 
En tant que titulaire d'un compte

Je souhaite pouvoir afficher les opérations sur ce compte avec la possibilité de filtrer entre 2 dates

Afin de vérifier les mouvements sur mon compte



**Exo 1 : Tax et Tip**

Le programme que vous devez créer pour cet exercice commence par la lecture dans la console du coût d'un repas commandé au restaurant pour un utilisateur. Ensuite, votre programme calculera la taxe et le pourboire du repas. Utilisez une TVA à 10% pour calculer le montant de la taxe. Calculez le pourboire comme étant égal 18% du montant du repas (sans la taxe). Le résultat de votre programme devrait inclure le montant de la taxe, le montant du pourboire et le cout total du repas, taxe et pourboire compris. Formatez la sortie de sorte que toutes les valeurs soient affichées en utilisant deux décimales.

print(f"Pour un repas de {repas:.2f}")

**Exo 2 : Chute libre** 

Créer un programme qui détermine la vitesse à laquelle un objet se déplace lorsqu'il touche le sol. L'utilisateur entrera la hauteur à partir de laquelle l'objet est lâché en mètres (m). Lorsque l'objet est lâché, sa vitesse initiale est de 0 m/s. Supposons que l'accélération due à la gravité est de 9,8 m / s2. Vous utilisez la formule vf = racine carré (vi2 + 2ad) pour calculer la vitesse final, vf, lorsque la vitesse initiale vi, l'accélération a et la distance d sont connues.

**Exo3 : Nommer ce triangle**

Un triangle peut être classé en fonction de la longueur de ses côtés : équilatéral, isocèle ou scalène. Les 3 côtés d'un triangle équilatéral ont la même longueur. Un triangle isocèle a 2 cotés de même longueur et un de longueur différente.  Si tous les cotés ont des longueurs différentes, le triangle est scalène.
Ecrivez un programme console qui demande à l’utilisateur la longueur des 3 côtés du triangle et qui affiche alors un message indiquant le type du triangle.

**Exo 4 : Admission au parc**

Un parc d’attraction détermine les prix d'entrée en fonction de l'âge des visiteurs. Les visiteurs de 2 ans et moins sont admis sans frais. Les enfants entre 3 et 12 ans doivent payer 14 euros. Les personnes âgées de 65 ans et plus payent 18 euros. L'entrée pour tous les autres coutent 23 euros.
Créez un programme console qui commence par lire l'âge de tous les invités d'un groupe, avec un âge entré sur chaque ligne. L'utilisateur entrera une ligne vierge pour indiquer qu'il n'y a plus d'invités dans le groupe. Ensuite, votre programme doit afficher le coût d’admission du groupe avec un message approprié. Le coût total doit être affiché avec deux décimales.



**Exo 5 : Formater un texte en Anglais**

Beaucoup de personnes ne formatte pas correctement leur texte, notamment lorsqu’il rédige un message sur leur smartphone.
L’objectif de cet exercice est d’écrire une fonction « capitalize(<str>) » qui formatte du texte écrit en Anglais. Les règles sont les suivantes :
-	Le « i » devra être transformé en « I » s’il est précédé ou suivi d’un espace
-	Le premier caractère d’une phrase doit mis en majuscule de même que le premier « non espace » après un « ? », un « . » ou un « ! ».
Exemple : what time do i have to be there ? what is your address ?    What time do I have to be there ? What is your address ?
Ecrire un programme console qui lit une chaine et la formatte via la méthode « capitalize ». Afficher le résultat 


**Exo 6 : Fonction inverse**

La fonction inverse renvoi le résultat de 1/x pour un entier x non nul.
Ecriver une fonction qui lève une exception si x est égal à 0. 


**Exo 7 : Eviter les duplications**

Créer un programme qui lit des mots rentrés par l’utilisateur à la console jusqu’à ce que l’utilisateur rentre une ligne blanche. Le programme devra afficher uniquement les mots non redondants dans le même ordre que la saisie.
Exemple :
Moi

Premier

Avant

Moi

Toi

Avant

Donne :
Moi
Premier
Avant
Toi

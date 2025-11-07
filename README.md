
/!\ Nous n'avons été prévenu du concours que le 10 mars /!\
 ↓ si vous voulez une version actualisée (pas forcément finie) différente de celle donnée le 28 mars ↓ 
https://drive.google.com/drive/folders/1--jKM9A903z1SB7FzyKWeHwBZ9DoaEg-?usp=sharing

------------
|NOX VILLAE|
------------


SOMMAIRE : 
1. Description du projet
2. Comment jouer ?
3. Histoire du jeu
4. Fonctionnement derrière l'écran

--1-- DESCRIPTION DU PROJET

	Ce projet python est un jeu Loup-garou solo dans lequel interagir avec les PNJ a de l'importance si on veut gagner avec notre camp.
Pour être sûr de bien jouer avec les PNJ nous devons entretenir un lien de confiance entre chacun pour être sûr de ne pas se faire voter.
Pour augmenter cette confiance nous pouvons récupérer des fruits dans les arbres grâce à l'entraide

--2-- COMMENT JOUER ?

-> Executer le fichier "Start.py" (dans le dossier "Jeu") pour lancer le jeu

	|Dans l'ordre d'une partie habituelle|
	> Menus

	Vous commencez sur le menu principal du jeu, vous pouvez accéder avec les boutons:
- aux menus de paramètres (configuration des paramètres en jeu/configuration des touches)
- au menu de sauvegardes
- au menu de données de parties

Dans le MENU DE SAUVEGARDE vous pouvez:
- Créer une sauvegarde (max 3)
- Supprimer une sauvegarde (si il n'en reste qu'une ça l'a réinitialisera seulement)
- Sélectionner une autre sauvegarde

Dans le MENU DE PARAMETRES vous pouvez:
- Changer dans le menu des paramètres généraux:
	o La durée d'une journée (temps donné pour interagir avec les autres PNJ pendant la journée)
	o Le nombre de créatures de départ (les créatures qui pourront se reproduire chaque nuit pour se multiplier)
	o Le nombre maximum d'entité (limite le nombre de création d'entités pour éviter de prendre trop de ressources)
	o La reproduction hétéronormée (ACTIF : Les créatures ne peuvent procréer qu'entre male et femelle / INACTIF : Le choix des reproductions ne dépends pas du genre)
	o La part définie de méchants (ACTIF : Le nombre de loups est défini équitablement avec le nombre de créatures / INACTIF : Les loups ne sont que les créatures qui ont un niveau de mal inferieur à un seuil)
	o L'affichage du temps écoulé (ACITF : le temps restant à la journée est affichée / INACTIF : plus réaliste, vous ne pouvez pas voir combien de temps il vous reste pour interagir pendant la journée)

- Changer dans le menu de configurations des touches:
	o Les touches directionnelles (Pour se déplacer pendant la journée sans utiliser la souris)
	o "Ecourter la journée" (Pour accélérer le temps jusqu'à la nuit)
	o "Mode spectateur" (Passe en mode automatique et laisse le joueur regarder la partie se dérouler sans qu'il n'interagisse)
	o "Center la caméra" (Passe le mode de vue de large à resserré et inversement |Large : Caméra statique et plan complet de toute la caméra / Resserré : La caméra suit le joueur et le plan est resserré)
	o "Ouvrir les menus" (Touche pour passer du jeu aux menus)

Dans le MENU DE DONNEES DE PARTIES (dans votre tente) vous pouvez:
- Observer tous vos paramètres (que vous avez le droit de voir) enregistrés dans votre sauvegarde :
	o Votre confiance envers chaque PNJ (et qui sont vos proches)
	o Votre rôle et sa description

- Jouer l'action de votre rôle (si il fait nuit et si vous pouvez jouer)


	> Jeu

Au premier lancement vous arrivez dans L'ESPACE LIBRE DE JOUR vous pouvez:
- Vous déplacer (en cliquant avec la souris ou en utilisant les touches directionnelles)
- Récupérer des fruits parterre => [donne 1 de nourriture] (vous le récupérez si vous êtes le premier à le toucher)
- Récupérer des fruits dans les arbres (en le secouant avec d'autres créatures qui peuvent accepter ou refuser selon leur confiance envers vous)
	o Si personne ne trahis => [donne 2 de nourriture par personne]
	o Si une seule personne trahis => [donne 1 de nourriture aux personnes trahis] [donne 2+nbDeCreatures de nourriture au traitre]
	o Si plus d'une personne trahis => [donne 3 de nourriture aux personnes trahis] [donne 0 de nourriture aux traitres] 
- Ouvrir le menu volant (avec un clique droit n'importe où)
	
Dans le MENU VOLANT vous pouvez :
- Accepter la demande d'aide de PNJ pour secouer un arbre (Accepter / Trahir (le nombre de nourriture en plus) / Refuser)
- Partager la confiance envers une créature à une personne (Une seule personne par partie (changeable): 
	o La personne aura une moyenne entre votre confiance et sa confiance envers cette créature selon le niveau de confiance qu'elle a envers vous
- Accuser une créature à quelqu'un (le PNJ choisira avec une probabilité selon la confiance) :
	o Si la personne refuse => rien ne change
	o Si la personne accepte => la personne votera pour la créature:
		Si la créature n'est pas tuée pendant le vote => rien ne change
		Si la créature est tuée pendant le vote et son rôle est du côté des villageois => +10% confiance
		Si la créature est tuée pendant le vote et son rôle est contre les villageois => -10% confiance
- Tuer une créature devant tout le monde :
	o Si la créature n'est pas dans le camp des villageois => +10% de confiance de tout le monde envers vous
	o Si la créature est dans le camp des villageois => -50% de confiance de tout le monde envers vous

A la fin du timer la nuit tombe et vous arrivez dans VOTRE TENTE DE NUIT où vous pouvez:
- Interagir avec le menu de données de partie
- Lancer l'action de rôle possible pendant la nuit :
	o Les villageois ne peuvent rien faire pendant la nuit
	o Cupidon peut coupler deux personne la premier nuit qui seront lié dans la mort
	o Les Loups-garous votent en groupe une personne à tuer anonymement


--3-- HISTOIRE DU JEU

	D'un temps lointain, le village de Thiercelieux, après avoir éradiqué la menace de Loups-garous de son village a décidé d'appeler tous les villages aux alentours à envoyer des groupes d'explorateurs chercher dans la forêt de Jouy pour chercher les derniers Loups-garous qui se sont enfuis. Les explorateurs se sont donc retrouvés pour former un camp mais après évaluation de la situation le groupe a remarqué que des Loups-garous étaient présents dans le groupe et il était trop tard pour faire demi-tour, ils devaient éliminer les Loups-garous avant qu'ils ne meurent.


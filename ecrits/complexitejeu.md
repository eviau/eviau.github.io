# Systématiser la création de jeux

### *journal de création, décembre 2019*

Existe-t-il un système permettant de créer des jeux multijoueurs de façon automatique ? Peut-on décrire mathématiquement le *plaisir* vécu par un joueur lorsqu'iel joue à des jeux vidéos ou à des jeux de société ? Ce sont là quelques-unes des questions qui me sont venues à l'esprit alors que je travaillais sur un jeu de société basé sur la crise des fondements des mathématiques du début du XXième siècle, alors que je réalisais que créer une mécanique de jeu intéressante allait être plus difficile que je ne le croyais... 

C'est lors d'une des rencontres mensuelles de [FLOP](https://flopmtl.ca) que j'allais être amenée à formuler cette première hypothèse: selon moi, il existe une certaine catégorie de jeux amusants, faisant appel à la créativité, qui sont dérivés de problèmes considérés ou prouvés comme étant [NP-complet](https://fr.wikipedia.org/wiki/Problème_NP-complet). N'étant pas experte dans le domaine de la complexité du calcul, je laisse à d'autres le soin d'expliquer ce concept.

Une recherche rapide sur Internet m'indique que je ne suis pas la seule: [Jeremy Kun](https://jeremykun.com/2014/03/17/want-to-make-a-great-puzzle-game-get-inspired-by-theoretical-computer-science/) a déjà élaboré en ce sens, et plusieurs jeux bien connus ont été démontrés comme l'étant (du moins, une généralisation de ces jeux l'est): Tetris, Mario, Zelda ... si l'on en croit cet [article](https://erikdemaine.org/papers/Nintendo_FUN2014/paper.pdf). 

S'il est possible de prouver qu'un jeu pré-existant est NP-difficile, est-il possible de **créer systématiquement des jeux** qui sont considérés comme amusants à partir de problèmes NP-difficiles, qui eux ne sont pas a priori des jeux ? C'est la question que j'explore depuis l'été 2019.

## Théorie des jeux

La [théorie des jeux](https://fr.wikipedia.org/wiki/Théorie_des_jeux) est un domaine des mathématiques et de l'économie s'intéressant à l'étude des jeux et des échanges qui en découlent. Parmi les concepts en faisant partie, nous aimerions souligner celui de [jeu résolu](https://fr.wikipedia.org/wiki/Jeu_résolu).

Selon Wikipedia, un jeu est dit **résolu**  si "le résultat (gagner, perdre ou match nul) peut être correctement prédit à partir de n'importe quelle position, en supposant que les deux joueurs jouent à la perfection." Par exemple, le jeu de Tic Tac Toe est un jeu résolu: si les deux joueurs jouent toujours leur meilleur coup possible, on a systématiquement un match nul.

On peut considérer un jeu résolu comme étant mathématiquement non-amusant: rien n'étant laissé à la stochasticité des choix humains, c'est l'effondrement du libre-arbitre et de la créativité. Bien entendu, ceci n'empêche pas qu'il soit amusant de découvrir cette stratégie optimale, ou que ce soit possible de trouver le jeu amusant pour d'autres raisons.

Bien que la théorie des jeux soit extrêmement intéressante, elle ne s'intéresse habituellement pas au concept très subjectif de plaisir dans le jeu, et nous la laissons de côté pour le moment.

## Un premier jeu: Travelling Erdős

À l'été 2018 je m'intéresse à la question suivante: supposons qu'une personne soit nouvelle dans un groupe d'ami.e.s, quelle serait pour elle la façon optimale de rencontrer tout le monde ? Cette question me mène à formaliser le jeu [Travelling Erdős](https://github.com/eviau/TravelingErdos), disponible en Python et en JavaScript. 

Ce premier jeu me semble intéressant mais peut-être simpliste... des lectures en théorie des graphes  - sur des thèmes comme la *bootstrap percolation* ou la *contagion de graphes* - me laissant croire que la solution analytique ou algorithmique étant possible, je cesse d'y travailler.

## Interlude: jeu de société

Entre temps, je développe un fort intérêt pour la crise des fondements des mathématiques du début du XXième siècle - intérêt qui me pousse à en faire un premier jeu de société visant à expliciter les grandes lignes de cette crise tout en simulant le fait d'être mathématicien ou mathématicienne. Ce premier jeu de société m'introduit à la mécanique des jeux de société et à leur économie - et me pousse à affiner mon raisonnement sur ce qui rend un jeu intéressant. Je pars à la recherche d'une définition formelle, mais pas nécessairement mathématique, de la notion d'amusement - bien que tout jeu puisse être considéré amusant, y a-t-il une formulation permettant de conclure qu'une catégorie de jeux soit considérée comme amusante par un nombre suffisamment grand de personnes pour que ce jeu soit amusant de façon, disons, "rationnelle" ?

C'est là la naissance de l'hypothèse de jeu basé sur un problème connu comme étant NP-difficile. Armée de cette hypothèse et d'une liste de problèmes NP-difficile, je cherche à concevoir un premier jeu: l'idée me viendra dans un cours d'introduction à l'algorithmique.

## Un deuxième jeu: Stable d'un graphe

Le [stable d'un graphe](https://fr.wikipedia.org/wiki/Stable_(théorie_des_graphes)) est défini comme un ensemble de sommets tels que chaque paire de sommets possible ne contienne deux sommets adjacents. Le problème qui nous intéresse est de déterminer un stable de taille maximale, pour un graphe donné.

Quel est le jeu qui en découle ?

Pour un nombre fini mais potentiellement grand de joueurs, commençons par générer un graphe. Ceci peut être fait de façon aléatoire à l'aide d'un ordinateur, mais peut aussi être généré par l'un des joueurs ou encore par l'ensemble des joueurs, à tour de rôle.

Chaque joueur a un crayon d'une couleur différente; tour-à-tour, chaque joueur colorie un noeud du graphe de façon à ce que ce noeud soit non-adjacent à tous les autres noeuds de la même couleur. Il s'agit de créer le plus grand stable possible.

Le jeu continue tant qu'il reste des noeuds possibles à colorier.

Variantes:
- on peut changer la couleur d'un noeud, pourvu que la [règle du ko](https://fr.wikipedia.org/wiki/Règles_du_go#Ko) tienne
- on peut ajouter des noeuds (au hasard, ou un nombre pré-détemriné pour éviter que la partie perdure)
- on peut enlever des noeuds (non-coloriés)
- on peut échanger les crayons de couleur

Une autre variante plus élaborée pourrait être d'en faire un jeu coopératif: sans discuter, les joueurs doivent trouver le stable maximal du graphe, en coloriant à tour de rôle un noeud du graphe.

Ce premier jeu généralement considéré comme "tout de même amusant" me pousse à chercher d'autres problèmes afin de générer des jeux. Je retourne à mes livres.

## Un troisième jeu: la gallerie d'art

Cette fois-ci, c'est en errant sur Wikipédia que je tombe sur le [problème de la gallerie d'art](https://fr.wikipedia.org/wiki/Problème_de_la_galerie_d%27art). Ce problème me semble intéressant car bien que ce soit un problème de la théorie des graphes, on peut en faire une représentation visuelle qui ne soit pas basée sur un graphe.

Son adaptation ([en JavaScript sur mon site](https://eviau.github.io/artgalleryjs/)) me demande un peu plus de recherche (en programmation notamment). Comme avec le problème du stable d'un graphe, on retrouve ce sentiment que le jeu nous échappe toujours un peu; la réponse optimale semble toujours si près, et pourtant on est incapable de vraiment la systématiser...

Si vous jouez au problème de la gallerie d'art, merci de m'envoyer votre solution - j'en ferai un leaderboard :)

## Idées variées

D'autres idées de jeu me traverse l'esprit, comme une machine de Turing compétitive (plus là-dessus dans un autre essai).

## Une heuristique de création de jeux

Qu'apprend-on de mes essais dans la création systématique de jeu ?

En gros mon processus de création s'explicite de la façon suivante:

- trouver un problème NP-difficile ne nécessitant pas de terminologie mathématique pour l'énoncer
- ajouter une composante de jeu: les joueurs doivent trouver simultanément (coopératif) ou à tour de rôle (compétitif) une solution au problème
- la meilleure solution trouvée l'emporte

Si vous avez un problème NP-difficile préféré et que vous souhaitez le transformer en jeu, écrivez-moi !


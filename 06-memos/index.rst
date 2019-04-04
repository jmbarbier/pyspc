Mémos
=====

Syntaxe Python pour la physique-chimie
--------------------------------------

XXX

Mémo Notebook Jupyter
---------------------

Syntaxe Markdown
~~~~~~~~~~~~~~~~

Le Markdown est une manière d’écrire simplement un texte pouvant être
transformé facilement en un autre type de document (pdf, html, word…) en
utilisant quelques conventions pour obtenir une mise en forme ou des
fonctionnalités, tout en restant facilement lisible pour un être humain.

Il est ainsi possible de créer des titres, mettre du texte en gras, en
italique, créer des listes, des liens, insérer des images, des formules
mathématiques, ..

::

   # Un titre
   ## Un sous-titre

   On peut formatter du texte **en gras**, en *italique*.
   On peut mettre `des extraits de code`

   - une liste non numérotée
   - élément 2
   - élément 3

   Une liste numérotée :

   1. liste numérotée
   2. liste numérotée 2
   3. liste numérotée

   Pour changer de paragraphe
   il faut 
   laisser une
   une ligne blanche,
   toute cette phrase ne sera que dans un paragraphe.

   Prochain paragraphe

   Ecrire des maths : $x^2$ ou une formule séparée : $$\frac{x^2}{\sqrt{3}}$$

   ```python
   print("toto")
   ```

Mémo LaTeX pour les formules de physique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Une formule mathématique se trouve entre deux caractères $. Deux modes
d’affichage sont possible : en ligne, et en séparé. Une formule en ligne
est affichée dans le texte : ``$x^{p-2}\$`` se lit :math:`x^{2-p}`,
alors qu’une formule en séparé (début et fin avec deux signes $) est
affichée sur sa propre ligne : ``$$\sqrt{3x-2}$$`` s’affiche

.. math:: \sqrt{3x-2}

Notations utiles
^^^^^^^^^^^^^^^^

-  Exposant : ``$Cl^-$`` : :math:`Cl^-`. Si plusieurs lettres en
   exposant : ``$Mg^{2+}$`` : :math:`Mg^{2+}`
-  Indice : ``$CO_2$`` : :math:`CO_2`. Si plusieurs lettres en indice :
   ``$CO_{2_{(g)}}$`` : :math:`CO_{2_{(g)}}`
-  Exposant et indice ``$CO_3^{2-}$`` : :math:`CO_3^{2-}`
-  Espace et flèche ``$2\ A+3\ B \rightarrow C$`` :
   :math:`2\ A+3\ B \rightarrow C`

-  Fraction : ``$\frac{A}{B}$`` : :math:`\frac{A}{B}`
-  Racine carrée : ``$\sqrt{A}$`` : :math:`\sqrt{A}`
-  Vecteur : ``$\vec{u}$`` : :math:`\vec{u}` ou
   ``$\overrightarrow{AB}$`` : :math:`\overrightarrow{AB}`
-  Somme : ``$\sum_{n=1}^p n^p$`` : :math:`\sum_{n=1}^p n^p`

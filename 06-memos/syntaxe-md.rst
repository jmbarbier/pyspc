Syntaxe Markdown
################

:download:`Télécharger le pdf <https://pyspc.readthedocs.io/fr/latest/06-memos/syntax-md.pdf>`


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

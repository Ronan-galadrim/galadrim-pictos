# Galadrim — pictos pour les devis

Bibliothèque publique d'icônes au trait utilisées dans les decks de devis Galadrim
(slide « Objectifs du projet » et autres slides à pictos). Le dépôt est public parce que
Google Slides doit pouvoir télécharger l'image : il ne contient **que des icônes**,
aucune information client.

- `png/<nom>.png` : 2 416 icônes, PNG 512 × 512, trait noir, fond transparent, cadrées
  et épaissies comme les pictos du template Galadrim (à poser sur les ronds pastel).
- `catalogue.json` : nom de l'icône → mots-clés (anglais), pour choisir la bonne icône.
- URL à passer à Google Slides (`replaceImage` / `createImage`) :
  `https://raw.githubusercontent.com/Ronan-galadrim/galadrim-pictos/main/png/<nom>.png`

Source : [Lucide](https://lucide.dev) v1.79.0, licence ISC (voir `LICENSE-lucide.txt`),
recolorées et recadrées par `build.py`.

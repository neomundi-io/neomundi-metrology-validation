# Politique de divulgation publique — évaluateurs et qualification

**Statut :** proposition à relire, 13 novembre 2026. **Périmètre :** documentation et artefacts de recherche. Ce texte ne vérifie pas la configuration actuelle de production.

## Principe

Rendre publics les objets mesurés, la sémantique des signaux, leurs états et limites, les méthodes générales et les résultats expérimentaux qualifiés, sans divulguer inutilement l'implémentation propriétaire ou des données sensibles.

Un score n'est ni une certification de vérité, de sécurité ou de conformité, ni une preuve de calibration. Distinguer test technique, qualification expérimentale, calibration et réplication indépendante.

| Niveau | Contenu | Règle |
|---|---|---|
| PUBLIC | Définition et unité des signaux, statuts et couverture, limites, résultats datés, méthodologie générale, version et provenance attestées | Publier avec périmètre et limites explicites |
| ACCÈS CONTRÔLÉ | Données pilotes, contenus bruts, configurations complètes, dossiers de réplication sensibles | Autorisations et confidentialité vérifiées avant partage |
| PRIVÉ | Clés, jetons, prompts système internes exacts, routage sensible, adresses internes et données privées | Aucune publication |

Les coefficients et seuils numériques ne sont **pas automatiquement des secrets** : certains sont nécessaires pour expliquer un résultat ou reproduire une expérience figée. Examiner au cas par cas la nécessité scientifique, la propriété intellectuelle et la version applicable. Supprimer une ligne de la branche principale n'efface pas son historique Git.

## Points P0 constatés

- Le SDK public `docs/LIMITES.md` contient des formules, pondérations et limites d'une implémentation historique. Ce document ne prouve pas les calculs déployés aujourd'hui.
- Le manifeste figé `experiments/EXP-001/EXP-001_smoke_test_run_manifest.json` contient une URL complète d'inférence, des noms de variables de configuration, les paramètres du juge et des seuils expérimentaux. Le chemin du service héberge un identifiant ; cela ne constitue pas en soi une clé d'authentification, mais mérite un examen de divulgation.
- Le dictionnaire des métriques documente des seuils et éléments de structure du juge, sans démontrer leur calibration.
- Les empreintes de configuration des évaluateurs ne sont pas nécessairement présentes pour chaque signal : une version de mesure identique ne garantit pas à elle seule une configuration identique.

Les expériences figées, signatures, empreintes et résultats négatifs ne doivent pas être réécrits silencieusement. Toute restriction ou correction historique doit préserver la traçabilité et documenter l'effet sur la reproductibilité.

## Informations minimales par évaluateur

Définition opérationnelle ; entrée et résultat observables ; méthode générale (heuristique, embeddings, LLM-juge) ; valeurs manquantes et modes de défaillance ; provenance effectivement attestée ; version et preuves de qualification ; limites de non-déterminisme et de comparabilité.

N'affirmer qu'un modèle ou une route est actuellement servi qu'à partir d'un inventaire d'exécution récent et autorisé. Les anciennes pages ne suffisent pas.

## Contrôles avant publication

- [ ] Visibilité, branche et version vérifiées
- [ ] Recherche de secrets et de chemins identifiants dans le texte, les pièces jointes et l'historique concernés
- [ ] Limites, erreurs et valeurs nulles conservées
- [ ] Seuils, modèles et résultats rattachés à leur version et protocole
- [ ] Pas d'affirmation de production sans preuve actuelle
- [ ] Cohérence français/anglais, liens et diff contrôlés
- [ ] Aucune modification des évaluateurs, de la production ou des artefacts figés

**Non établi par cet audit :** absence générale de secrets dans tout l'historique, modèles actuellement servis et calibration actuelle des évaluateurs.

[English version](PUBLIC_DISCLOSURE_POLICY.md)

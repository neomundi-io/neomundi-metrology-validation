# EXP-001 — Rapport du smoke test

## 1. Identification

- Run ID :
- Date :
- Version du corpus :
- Version du signal :
- Version de la baseline :
- Commit du repository :

## 2. Objectif

Vérifier le bon fonctionnement technique et méthodologique de la chaîne de validation factuelle.

Ce smoke test ne constitue pas une validation scientifique.

## 3. Corpus

- Nombre total de cas :
- Cas positifs :
- Cas négatifs :
- Cas exclus :
- Cas non interprétables :

## 4. Résultats techniques

- Cas chargés :
- Sorties NeoMundi produites :
- Sorties baseline produites :
- Erreurs de calcul :
- Données manquantes :
- Couverture :

## 5. Matrice de confusion

| Méthode | VP | FP | VN | FN |
|---|---:|---:|---:|---:|
| Baseline |  |  |  |  |
| NeoMundi |  |  |  |  |
| Baseline + NeoMundi |  |  |  |  |

## 6. Performances

| Méthode | Précision | Rappel | Spécificité | F1 |
|---|---:|---:|---:|---:|
| Baseline |  |  |  |  |
| NeoMundi |  |  |  |  |
| Baseline + NeoMundi |  |  |  |  |

## 7. Erreurs observées

### Faux positifs

À compléter.

### Faux négatifs

À compléter.

### Erreurs techniques

À compléter.

## 8. Validation du pipeline

- [ ] Les 20 cas ont été chargés
- [ ] Chaque cas possède une sortie
- [ ] Les labels sont restés masqués au signal
- [ ] La baseline est indépendante
- [ ] Les versions sont enregistrées
- [ ] Les résultats sont recalculables
- [ ] Les erreurs sont tracées

## 9. Conclusion

Statut du smoke test :

- `SUCCESS`
- `PARTIAL_SUCCESS`
- `FAILED`
- `INVALIDATED`

Conclusion méthodologique :

À compléter.

## 10. Limites

- corpus synthétique ;
- cas simples ;
- échantillon très réduit ;
- aucune généralisation autorisée ;
- aucune affirmation de performance autorisée.

## 11. Prochaine décision

- corriger le pipeline ;
- améliorer le protocole ;
- lancer un nouveau smoke test ;
- préparer le corpus de 200 cas ;
- interrompre l’expérience.

## 12. Statut

- Version : v0.1
- Statut : modèle de rapport
- Responsable : Sébastien

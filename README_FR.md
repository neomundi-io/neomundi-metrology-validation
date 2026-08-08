🇫🇷 **Version française :** [README_FR.md](./README_FR.md) · 🇬🇧 **English version:** [README.md](./README.md)

## État actuel

### Première étape de validation terminée — EXP-001

NeoMundi a terminé son premier smoke test métrologique contrôlé.

On peut l’imaginer comme le test d’un thermomètre avec de l’eau dont on connaît déjà la température.

Nous avons préparé 20 cas simples :

- 10 contenant une erreur factuelle connue ;
- 10 ne contenant pas d’erreur factuelle.

Les bonnes réponses ont été cachées à NeoMundi.

NeoMundi a mesuré les 20 cas indépendamment.

Les résultats ont ensuite été comparés avec :

1. la vérité terrain gelée ;
2. une baseline déterministe indépendante ;
3. une revue humaine après exécution.

Sur ce smoke test contrôlé :

- 20 / 20 cas ont produit une mesure ;
- 0 erreur de calcul ;
- 0 signal indisponible ;
- 10 vrais positifs ;
- 10 vrais négatifs ;
- 0 faux positif ;
- 0 faux négatif.

Cela ne signifie **pas** que MET-003 est scientifiquement validé ou que NeoMundi atteint 100 % de performance en général.

Cela signifie quelque chose de plus simple et de plus important à ce stade :

> **la chaîne expérimentale fonctionne, elle est traçable, et elle peut maintenant être testée sur des corpus plus difficiles et plus larges.**

La prochaine étape de validation sera menée dans une nouvelle expérience versionnée, sans modifier rétrospectivement EXP-001.

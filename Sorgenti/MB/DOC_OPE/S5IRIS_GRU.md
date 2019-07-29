L'alternativa di ciclo, possibile se presenti le testate, è una scelta dell'intero ciclo da schedulare, ed è eseguita a monte della schedulazione stessa.

Le ulteriori alternative che sono tra le scelte che opera la schedulazione si definiscono nella tabella dello scenario S5B : 
 * Alternative di fase (si imposta il campo specifico). Attualmente la scelta dell'alternativa di fase va eseguita all'esterno della schedulazione, operando sul ciclo del documento.
 * Alternative di risorsa specifica (se i campi tipo risorsa principale e tipo risorsa specifica sono diversi)

![FIG_015](http://localhost:3000/immagini/MBDOC_OPE-S5IRIS_GRU/FIG_015.png)
 - Solo sequenziazione delle fasi attive sulla risorsa principale
 - Scelta tra le fasi alternative del ciclo
 - Scelta tra le risorse specifiche che appartengono alla risorsa principale delle fasi attive
 - Scelta tra le risorse specifiche appartenenti alla risorsa principale di tutte le fasi in alternativa.

Durante la schedulazione vengono costruiti i 'gruppi di schedulazione' che comprendono tutti gli oggetti da schedulare in competizione tra di loro. Sono le code da cui si sceglie cosa fare per primo e dove farlo.

Vi sono quindi le seguenti possibilità : 
 - Il gruppo è ininfluente (coincide con la risorsa principale)
 - Il gruppo contiene le risorse principali in alternativa tra di loro
 - Il gruppo coincide con la risorsa principale e contiene le sue risorse specifiche
 - Il gruppo contiene le risorse specifiche delle risorse principali in alternativa tra di loro

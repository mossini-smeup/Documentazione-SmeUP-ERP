# CSS - Forme di sintesi
 :  : DEC T(ST) K(CSS)
## OBIETTIVO
La tabella, che si sviluppa in sottosettori diversi, ha lo scopo di definire le decodifiche delle 41 voci di costo presenti nell'archivio dei costi e delle 25 voci di totalizzazione di ciascuna voce di sintesi definita in tabella CSS.
## CARATTERISTICHE
La tabella ha 5 elementi, con codice da 1 a 5, ed ogni elemento di tabella contiene le decodifiche di 5 campi.
__Sottosettore bianco__
Contiene le decodifiche dei singoli campi della struttura del costo. I campi della struttura sono 41 ma i primi 16 si ripetono al livello e ai livelli inferiori. Ai 16 vanno aggiunti i 9 campi di ricarica.
__Sottosettore non bianco__
Contengono le decodifiche dei 25 totalizzatori come definiti nella tabella CSS.
_7_NB  I 25 significati sono raccolti in gruppi di 5 al solo scopo di rendere più veloce l'elaborazione.
_1_Spiegazione dei campi
Quanto segue è valido per tutti i campi __codice__ e __decodifica__
_2_Codice
 È un numero a valore costante che può variare da 1 a 5.
_2_Decodifica campo 1 (e successivi)
Contengono le decodifiche dell'n-esimo (dove n è il codice elemento) gruppo di 5 campi.
__Esempio : __
La terza decodifica della tabella che ha codice elemento = 2, si riferisce al totalizzatore numero 13.
## CONTENUTO DEI CAMPI

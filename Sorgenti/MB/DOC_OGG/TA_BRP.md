# BRP - Tipo parte
 :  : DEC T(ST) K(BRP)
## OBIETTIVO
Definire il comportamento dell'articolo in : 
-    Scansione della distinta base
Un tipo parte '0' è un fantasma, che viene oltrepassato nella scansione di produzione.
-    Calcolo dei costi
I tipi parte 3 e 4 non leggono il ciclo anche se presente.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Codice**
Indica il tipo parte. Il codice è di 3 caratteri ma il primo ha un valore fissato per SME_UP. I valori possibili del primo carattere sono : 

0    =    Fittizio
1    =    Finito
2    =    Semilavorato
3    =    Componente di acquisto
4    =    Materia prima
5    =    Acquisto con costificazione del ciclo


Si considerano quindi fittizi tutti i codici che iniziano con il carattere 0. Ciò permette all'utente di distinguere varie tipologie all'interno dei fittizi.

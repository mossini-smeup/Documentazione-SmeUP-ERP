# MP2 - Parametri previsioni HW
## OBIETTIVO
Imposta i criteri per assegnare ad ogni codice previsto con HW, una classe previsiva e, di comnseguenza, il livello di servizio che si intende assicurare ad ogni classe.
## Parametri consigliati
Nell'impostazione di questa tabella si consiglia di utilizzare i parametri visualizzati di seguito : 
![MPPIAN_048](http://localhost:3000/immagini/MBDOC_OGG-TA_MP2/MPPIAN_048.png)## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$M1,1 **Classe Mape 1**
Agli articoli il cui MAPE è minore o uguale a questo valore, si assegna la classe MAPE 1
 :  : FLD T$M1,2 **Classe Mape 2**
Agli articoli il cui MAPE è minore o uguale a questo valore, si assegna la classe MAPE 2
 :  : FLD T$M1,3 **Classe Mape 3**
Agli articoli il cui MAPE è minore o uguale a questo valore, si assegna la classe MAPE 3
 :  : FLD T$M1,4 **Classe Mape 4**
Agli articoli il cui MAPE è minore o uguale a questo valore, si assegna la classe MAPE 4
 :  : FLD T$M1,5 **Classe Mape 5**
Agli articoli il cui MAPE è minore o uguale a questo valore, si assegna la classe MAPE 5
 :  : FLD T$M2,1 **Classe toccate 1**
Agli articoli con numero toccate maggiore o uguale a questo valore, si assegna la classe toccate 1
Il numero di toccate è pari al numero di elementi non nulli della serie storica.
 :  : FLD T$M2,2 **Classe toccate 2**
Agli articoli con numero toccate maggiore o uguale a questo valore, si assegna la classe toccate 2
 :  : FLD T$M2,3 **Classe toccate 3**
Agli articoli con numero toccate maggiore o uguale a questo valore, si assegna la classe toccate 3
 :  : FLD T$M3,1 **Classe previsiva**
In questa tabella si fissa in orizzontale la classe Mape, ed in verticale la classe toccate, valori definiti in precedenza. Il valore corrispondente al punto di intersezione è la classe previsiva dell'articolo in esame.
Ad esempio, una classe MAPE "4" ed una classe toccate "3" si incontrano nel punto contenente il valore "5", che è la classe previsiva dell'articolo.
 :  : FLD T$M3,2.T$M3,1**Classe previsiva**
 :  : FLD T$M3,3.T$M3,1**Classe previsiva**
 :  : FLD T$M3,4.T$M3,1**Classe previsiva**
 :  : FLD T$M3,5.T$M3,1**Classe previsiva**
 :  : FLD T$M3,6.T$M3,1**Classe previsiva**
 :  : FLD T$MP2A **Limite classe 6**
In questo campo si inserisce il limite per cui un codice appartiene alla classe previsiva "6".
Nello specifico si inserisce il valore massimo della profondità della storia, vale a dire l'elemento, della storia, più lontano dalla frontiera contenente un valore positivo.
Se l'articolo ha una profondità minore o uguale al valore impostato in questo campo, la sua classe previsiva è "6", indipendentemente da ogni altra considerazione sul Mape e numero di toccate.
 :  : FLD T$M4,1 **Livello del servizio**
In questo campo si imposta il livello di servizio (lds) che si vuole assicurare alle varie classi previsionali definite in precedenza.
Il livello di servizio contribuisce a determinare il valore della scorta.
Si noti che per le classi 5 e 6 NON è possibile assegnare un lds, e quindi per esse NON verrà calcolata nessuna scorta.
Si ricorda che il lds può essere definito anche a livello di articolo/plant, e che quest'ultimo valore ha la precedenza su quello definito in questa tabella, a livello di classe.
Si precisa inoltre che il lds è un valore minore di 1.
E' ammesso l'inserimento anche del valore 1 (che in termini matematici produrrebbe un valore di scorta infinito),
che viene trattato come 0.9999.
 :  : FLD T$M4,2.T$M4,1**Livello servizio**
 :  : FLD T$M4,3.T$M4,1**Livello servizio**
 :  : FLD T$M4,4.T$M4,1**Livello servizio**
 :  : FLD T$M4,5.T$M4,1**Livello servizio**
 :  : FLD T$MP2B **Tipo distinta per t.appr.cumulato (SV)**
Se si imposta questo campo, la scorta di sicurezza verrà calcolata in base al tempo di approvvigionamento cumulato (e non del livello), del tipo distinta qui specificato.
 :  : FLD T$MP2C **Abilita storico**
Se si imposta questo campo, il calcolo HW viene memorizzato per piano conservandone lo storico se in presenza di più piani.
La memorizzazione avviene sul tema "£P2". Le impostazioni di questo tema non sono parametrizzabili esse sono derivate dal tema principale "£P1" e se divergenti ricostruite prima del calcolo.
Nello storico rimane attivo solo l'ultimo piano HW calcolato, l'eliminazione dei piani precedenti viene fatta assumendo come radice i primi due caratteri del piano.
Viene fatto presente che questo tema è memorizzato solo per scopi statistici.

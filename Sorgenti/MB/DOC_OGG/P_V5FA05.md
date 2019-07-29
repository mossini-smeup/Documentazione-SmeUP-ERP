## Contabilizzazione fatture
La funzione serve per trasferire i dati delle fatture dal sistema gestionale a quello contabile.
_2_Nota bene, è necessatio che nella tabella di impostazioni generali V51 sia stato definito l'abiente di fatturazione, che nel casi di sistemi diversi da Keep.UP (Applicazione contabile di Sme.UP) è il Sistema Informativo della contabilità, mentre nel caso di Kee.UP deve essere il codice azienda di fatturazione.

## Formato di lancio
![V5FA05_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA05/V5FA05_01.png)
## Funzioni possibili : 
 * Contabilizzazione _2_Fatture/Note di credito
 * Azioni di : 
 ** _2_Controllo
 ** _2_Aggiornamento
 ** _2_Controllo e Aggiornamento, (funzione assunta)
 * Stampa di controllo : 
 ** _2_Completa, produce la stampa dei record di contabilizzazione per ogni fattura
 ** _2_Solo errori, stampa solo gli errori

## Elaborazione
Vengono passati in contabilità le fatture comprese nei limiti di selezione.

Attraverso i parametri di esecuzione (F11) si possono modificare le caratteristiche dell'elaborazione (es. stampante, elaborazione batch/interattiva, ecc..); (cfr. doc. B£GPE2)
- [Parametri di esecuzione](Sorgenti/MB/DOC_OGG/P_B£GPE2)

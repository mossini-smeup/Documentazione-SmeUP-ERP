## Stampa fatture
La funzione permette creare una fattura o più fatture a partire da uno o più documenti selezionati attraverso le parzializzazioni.

## Formato di lancio
![V5FA01_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA01/V5FA01_01.png)
## Funzioni possibili : 
 * Azioni su _2_Fatture/Note di credito
 * Tipo di azione : 
 ** _2_Stampa, il sistema controlla che il documento non sia già stato stampato (numero fattura e data fattura non devono essere compilati, inoltre in testata il Flag 19 deve essere B,  oppure N per le note di credito), dopo la stampa il documento assume numero fattura e data fattura.
 ** _2_Prestampa, il sistema esegue la stampa senza assegnare numero e data fattura.
 ** _2_Ristampa,  il sistema esegue la stampa solo per ducmenti che hanno già numero e data fattura impostati.
 ** _2_Ristampa fatture già contabilizzate,  il sistema esegue la stampa solo se in testata il Flag 19 è E,  oppure Q per le note di credito.
 * Output _2_Formato PDF/Normale
 * Stampa fatture : 
 ** _2_Normali
 ** _2_A data fissa, questa modalità si utilizza quando un cliente od un gruppo di clienti richiedono una fatturazione con data fissa, in questo caso si devono definire dei gruppi di fatturazione (in tabella BR*_CF) ed attribuirli ai clienti (attraverso l'estensione £08), scegliendo fatturazione a data fissa e inserendo il gruppo il programma filtra i documenti fatturabili solo per i clienti appartenenti al gruppo
 * Stampa in _2_Lingua, si imposta la lingua voluta
 * Stampa in valuta : 
 ** _2_Valuta documento
 ** _2_Valuta corrente, definita in tabella B£2, generalmente Euro
 ** _2_Valuta alternativa, definita in tab. B£2
 * Ristampa per numero fattura, forza l'ordine di ristampa dei documenti (per N. Fattura)

## Gestione numeratori
A volte può essere necessario intervenire manualmente per assegnare (prenotare) un numero di fattura, oppure per recuperare un numero di fattura a chiusura di un buco lasciato in precedenza, queste attività possono essere eseguite intervenendo manualmente nella gestione dei numeratori di fattura attivabile atraverso il comando funzione F10 : 
![V5FA01_02](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA01/V5FA01_02.png)
## Azioni
Se il campo "Singolo documento" è compilato, viene stampato solo questo, altrimenti vengono stampati tutti i documenti compresi nelle parzializzazioni, se le parzializzazioni non sono state impostate esce un messaggio di warning che richiede una conferma esplicita per lanciare la stampa di massa.

_1_ATTENZIONE per stampe di più documenti inserire SEMPRE le parzializzazioni.

Attraverso i parametri di esecuzione (F11) si possono modificare le caratteristiche dell'elaborazione (es. stampante, elaborazione batch/interattiva, ecc..); (cfr. doc. B£GPE2)
- [Parametri di esecuzione](Sorgenti/MB/DOC_OGG/P_B£GPE2)

## Generazione documenti di autofattura
La funzione serve per creare dei documenti di autofattura a fronte di righe omaggio presenti in altri documenti.

_2_Nota bene, vengono prese in considerazione solo le righe documento che hanno il Flag 19 = "8".
La tabella V53 deve essere correttamente impostata con elementi che hanno lo stesso valore dei modelli documento (tab. V5A_xx) utilizzati nei documenti di vendita in cui compaiono le righe omaggio.

## Formato di lancio
![V5FA10_01](http://localhost:3000/immagini/MBDOC_OGG-P_V5FA10/V5FA10_01.png)
## Azioni possibili : 
 * _2_Generazione/Rigenerazione documento autofattura
 * Stampa  _2_lista di controllo

## Elaborazione
Le azioni selezionate vengono applicate ai documenti compresi nei limiti di lancio.

Attraverso i parametri di esecuzione (F11) si possono modificare le caratteristiche dell'elaborazione (es. stampante, elaborazione batch/interattiva, ecc..); (cfr. doc. B£GPE2)
- [Parametri di esecuzione](Sorgenti/MB/DOC_OGG/P_B£GPE2)

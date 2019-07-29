## Scheda Report preparati
### Introduzione
Per facilitare le interrogazioni statistiche sono stati preparati dei gruppi di report scelti tra quelli che, a nostro avviso, sono i più utilizzati.

Quando viene scelta questa funzione si presenta la seguente scheda : 

![V5STAT_025](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_02/V5STAT_025.png)
Nella scheda sono presenti varie sottoschede : 
 * _2_Condizioni di esecuzione, con questa sottoscheda si selezionano i parametri per l'emissione del report
 * _2_Dati, mostra i dati del report in base alle condizioni di esecuzione impostate

### Condizioni di esecuzione
![V5STAT_023](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_02/V5STAT_023.png)La sottoscheda presenta delle sezioni di impostazione a sinistra : 

- _1_Report standard (riquadro verde), in cui sono disponibili alcuni report predefiniti. La scelta avviene cliccando su una voce :  il doppio click sulla selezione fatta crea il report e muove la visualizzazione alla sottoscheda Dati

Le sezioni successive mostrano nel dettaglio le impostazioni del report standard selezionato, si possono modificare per ottenere report customizzati più vicini alle proprie esigenze : 
 * _1_Dimensioni (riquadro rosso), sono gli "oggetti" sui quali eseguire l'analisi
 * _1_Valori (riquadro azzurro),  si possono selezionare i numeri da visualizzare per le dimensioni scelte
 * _1_Emissione richiesta (riquadro viola), è il formato in cui proporre il risultato della richiesta.

nelle sezioni di destra abbiamo : 
 * _1_Limiti (riquadro giallo), per impostare i limiti temporali del report
 * _1_Risultato (riquadro nero), mostra il riepilogo dei parametri scelti

### Lancio di un report predefinito
Per lanciare un report predefinito basta selezionarne uno tra i report standard e fissare i limiti di elaborazione, ad esempio se si vuole un report che confronta gli importi di due periodi per cliente, raggruppato per zona e agente selezionare : 

- report _2_Agente/Zona/Cliente, da notare che nel report si vedono anche due indici _2_01 - 01, che significano : 
-- Dimensioni = 01 Agente/Zona/Cliente
-- Valori = 01 Importo (su 2 periodi)

![V5STAT_040](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_02/V5STAT_040.png)
- _2_Limiti**, doppio click su **Parametri/Periodi** per aprire il formato di impostazione dei periodi : 

![V5STAT_036](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_02/V5STAT_036.png)
Da notare i campi liberi "Primo periodo", "Secondo periodo" :  non sono obbligatori, possono essere compilati a piacere dall'utente e saranno riportati sulla testata delle colonne del report ottenuto.
Confermare la scelta con F6, poi per visualizzare il risultato dell'interrogazione è necessario fare un doppio click sul report standard scelto.
Il sistema compone il report ed apre direttamente la sottoscheda "Dati" presentando il fatturato dei clienti divisi per zona associati ai singoli agenti : 

![V5STAT_037](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_02/V5STAT_037.png)
### Report diversi da quelli standard
Per la creazione di report diversi da quelli predefiniti possiamo scegliere direttamente dimensioni e valori nelle sottoschedere relative, ad esempio se volessimo analizzare il confronto del fatturato, in quantità e valore, tra due periodi raggruppato per cliente / articolo si devono scegliere : 
 * Dimensioni = 06 - Cliente/Articolo
 * Valori = 02 - Quantità/Importi (2 periodi)

![V5STAT_038](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_02/V5STAT_038.png)
Dopo aver impostato nella sezione "Limiti" i periodi da confrontare, il tab "Dati" mostra la matrice relativa.

![V5STAT_039](http://localhost:3000/immagini/MBDOC_SCH-V5STAT_02/V5STAT_039.png)
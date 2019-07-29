# Generalità

Il componente input è utilizzabile in ambiente device.

La sintassi di definizione è la medesima prevista per l'utilizzo del componente sul client loocup. Rispetto ad altri componenti utilizzabili sul mobile, per l'input panel le funzionalità rimangono praticamente invariate, ad eccezione di queste due considerazioni : 
* Il layout dell'input panel è fisso :  come nell'immagine riportata a seguire, si presenta sempre come un elenco di campi in verticale
* Le ricerche sono attivabili attraverso la pressione dell'icona riportata in tutte le righe sull'estrema destra. La funzione di default è la ricerca fissa con posizionamento per codice (tenendo conto del contenuto attuale della cella), ma tale funzione può essere sovrascritta attraverso la variabile di SCP_CLO *MOBILECOMBO. Tale funzione di default, viene in ogni caso sovrascritta nell'input panel specifico, nell'xml di setup viene inviato anche l'xml di risoluzione delle combo.

![TEC048](http://localhost:3000/immagini/LOCINP_MO/TEC048.png)

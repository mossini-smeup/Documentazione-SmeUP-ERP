## Fonte fotografata
Se l'origine è FF (fonte fotografata)

La fonte fotografata consente di riprendere le informazioni presenti nei consigli di pianificazione ('fotografate' all'atto dell'esecuzione della pianificazione). In questo ambito, le quantità delle fonti indotte dalla pianificazione stessa (ordini e impegni pianificati) sono ritornate al lordo dei rilasci effettuati, a differenza di quanto accade nelle fonti specifiche (PN e IP). L'intento di questa fonte è di offrire una fotografia 'ferma' al momento della pianificazione, mentre le fonti specifiche sono normalmente incluse in un gruppo fonti, che comprende anche fonti rilasciate. Di conseguenza le fonti pianificate devono contribuire per la quantità ancora da rilasciare.
Per convenzione questa fonte è stata classificata come futura, ma verranno ritornate sia fonti presenti sia fonti future, (a meno che sia stato impostato un filtro tra i parametri, come esposto nel seguito).
Inoltre, è ininfluente quale valore si imposti sull'azione fonte (che è un campo obbligatorio) :  verrà ritornato il valore effettivamente presente sul record dei consigli, relativo alla fonte originaria.
>Parametro 1 : 
-    Pos.1/10  Scenario dei consigli (opzionale) :  se non impostato viene assunto lo
.              scenario ricevuto. Se anch'esso è bianco viene assunto '**'.
Parametro 2 : 
-    Pos.1/1   Tipo fonte (E/F) :  se impostato si tratteranno solo le fonti
.              esistenti o future
-    Pos.2/3   È significativo solo se presente il tipo fonte. È l'origine fonte
.              (V2 M5OFP/M5OFF) che, se impostato, costituirà un filtro sulle fonti
.              da ritornare.
-    Pos.4/6   È significativo solo se presente il tipo fonte. È il codice fonte
.              (TA M5E/M5F) che, se impostato, costituirà un filtro sulle fonti da
.              ritornare.
-    Pos.7/7   Se impostato, verranno applicati i suggerimenti sulle fonti future : 
.              quelle da annullare non verranno ritornate; verranno recepite le
.              variazioni alle quantità e alle date.
-    Pos.8/8   Se impostato, gli impegni pianificati vengono raggruppati per giorno.
.              Se si impostasse il consueto campo 'raggruppamento per data' su
.              questo elemento di tabella, si otterrebbe l'effetto 'eccessivo' di
.              raggruppare tutte le fonti dello stesso giorno (ordini e impegni,
.              pianificati e rilasciati).
.              Va ricordato, inoltre, che gli impegni rilasciati sono già ragguppati
.              all'origine (se impostato nella fonte), e di conseguenza sono scritti
.              già raggruppati nei consigli di pianificazione.
-    Pos.9/9   Se impostato, verrà utilizzata cone descrizione della fonte la
.              descrizione della fonte fotografata al posto della descrizione della
.              fonte origine


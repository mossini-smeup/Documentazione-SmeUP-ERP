## Conservazione sostitutiva solo per fatture con trasmissione elettronica
I programmi di conservazione sostitutiva prevedono che i numeri di fattura conservati siano consecutivi.
Questo pone un problema nel caso si decida di archiviare con conservazione sostitutiva solo le fatture elettroniche.

La soluzione consigliata consiste nel creare un registro dedicato (in modo da ottenere una numerazione sequenziale delle fatture conservate).
Per questo è necessario : 
1- creare un nuovo registro iva nella tabella C5R ed il corrispondente numeratore in CRN (i numeratori sono per anno e azienda :  REG.AN.AZ).
2- creare le corrispondenti C5D e C5V per vendite PA e vendite B2B a partire da quelle delle vendite Italia.
3- creare un modello contabile in C5A per le vendite PA e uno per le vendite B2B a partire da quello delle vendite Italia con impostate le nuove C5D e C5V.
4- impostare in C5A nel modello contabile delle vendite Italia il campo Modello Contab.PA (T$C5AL) con la nuova C5A creata, in modo da determinare la deviazione su una C5A alternativa nel caso di cliente PA.
5- impostare in C5A nel modello contabile delle vendite Italia il campo Modello Cont.F.E.B2B (T$C5AM) con la nuova C5A creata, in modo da determinare la deviazione su una C5A alternativa nel caso di cliente B2B.
6- Nel caso sia valorizzato il campo Causale contabile forzata (T§CAUS) in testata del documento, tale impostazione prevale, escludendo quindi l'eventuale deviazione sui modelli PA e B2B.

Questo comporta obbligatoriamente l'attivazione in V51 della exit standard V5FA01S_2 per il recupero del numeratore impostando il campo T1V51A Num.Fat.Sp. a "2".
Per release che non hanno il campo in V51, e quindi non prevedono il richiamo della exit,  modificare il V5FA01S prevedendo il richiamo del V5FA01S_2 .
La exit V5FA01S_2 devia il numeratore delle fatture su numeratore C5 solamente per i clienti per i quali sia attiva la fatturazione elettronica PA o B2B (con presente l'estensione £51 sul BRESCO).
Qualora nella propria installazione si sia invece attivato il richiamo della exit V5FA01S_1, si otterrà la deviazione su numeratori C5 di TUTTE le fatture (COMPRESE quelle alla PA / B2B).

Questa soluzione viene proposta (rispetto alla creazione di modelli documento specifici)  per non obbligare alla creazione di un programma di conversione per gli ordini aperti.
 :  : NPG
### Oggetti V4 per release precedenti a V3R2
**N.B. Il B£G15M distribuito esegue la conversione dei valori V4 da formato posizionale ad** **attributo riscrivendo gli script in SCP_TAB.**
**Fare quindi una copia degli script in SCP_TAB in un diverso sorgente per sicurezza.**
Si consiglia di far uscire tutti gli utenti prima di mettere in linea il B£G15M, in modo che tutti abbiano in linea la nuova versione.

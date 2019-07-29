# G91 - Gestione post-acquisto
## OBIETTIVO
Definisce i parametri generali relativi al ciclo attivo.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM Elemento
È un elemento fisso.
 :  : FLD T$G91A __Tipo contatto__
È un elemento della tabella BRE. È il tipo ente che viene utilizzato nella contabilizzazione.
 :  : FLD T$G91B __Ambiente contabilizzazione__
È un parametro tipico dell'applicazione contabile interfacciata.
_9_Esempio :  se l'applicazione è sotto modulo base, e in questo campo si inserisce il sistema informativo d'arrivo, viene eseguito, dopo la scrittura degli archivi di transito, anche il passaggio agli archivi finali dei movimenti contabili.
 :  : FLD T$G91C __1=Protocollo autom.__
Inserendo il carattere '1' in questo campo, il protocollo IVA viene attribuito automaticamente. Per attivare questa funzione è necessario che l'applicazione contabile installata lo consenta.
 :  : FLD T$G91G __Attivo analitica__
Inserendo il carattere '1', il pgm di controllo fatture attiva la gestione dell'analitica. Vengono gestiti i campi Cdc/vds etc.
 :  : FLD T$G91D __Pgm contab.analitica__
Nome del programma con cui gestire la creazione batch dei movimenti di analitica (cdc e vds).
 :  : FLD T$G91E __Riservato SMEUP (ex Gest.contab.Smeup)__

 :  : FLD T$G91F __Rif.forn.su mov.MAG.__
Questo campo gestisce la scrittura dei campi relativi alla fattura sui movimenti di magazzino (numero e data fattura), inserendo il carattere '1' in questo campo. Nei campi "numero e data contabile" del movimento di magazzino verranno inseriti numero e data del protocollo contabile, mentre lasciandolo ' ' viengono registrati il numero e la data fattura del fornitore.
 :  : FLD T$G91O __Rif.forn. a video__
Inserendo il valore '1' nella lista delle fatture collegate, viene presentato il protocollo IVA invece della fattura del fornitore.
 :  : FLD T$VCSM __Var. +/- Costo medio__
Questo campo è utilizzato nella stampa delle entrate per gestire gli scostamenti dei prezzi con il costo medio.
 :  : FLD T$G91V __Reg.contab.solo lire__
Impostando il carattere '1', le registrazioni delle fatture in valuta vengono trasformate in lire.
 :  : FLD T$G91H __Note/messaggi__
Deve essere un elemento della tabella NSI. Se inserito attiva la gestione dei messaggi legati ad una bolla di entrata.
Il controllore della fattura li potrà leggere.
 :  : FLD T$G91I __Dettaglio conti__
Indica il dettaglio con cui la £V5F somma i valori relativi ai singoli conti. I valori possibili sono : 
_R_' '  Riepilogo per conto
_R_'1'  Riepilogo per conto/centro di costo
_R_'2'  Riepilogo per conto/commessa
_R_'3'  Riepilogo per conto/centro di costo/commessa
_R_'4'  Riepilogo per conto/centro di costo/Voce di spesa
_R_'5'  Riepilogo per conto/commessa/Voce di spesa
_R_'6'  Riepilogo per conto/centro di costo/commessa/Voce di spesa
_R_'7'  Riepilogo per conto/Voce di spesa
_R_'A'  Riepilogo secondo il modello di analitica inserito
 :  : FLD T$G91L __Calcolo Iva__
Inserendo il carattere '1', il programma di contabilizzazione delle fatture calcola l'IVA utilizzando gli assoggettamenti fiscali delle bolle di entrata (ordini). Lasciandolo bianco utilizza l'assoggettamento indicato in formato guida.
 :  : FLD T$G91M __Gest.Num.INTRA sep.__
Inserendo il carattere '1', il programma di contabilizzazione delle fatture in caso di fattura INTRA gestisce la numerazione separata (acquisti/vendite).
 :  : FLD T$G91N __Numeratore vendite__
Inserendo l'elemento della tabella CRNV5, gestisce il numero delle vendite automaticamente.
 :  : FLD T$G91P __Gestione Spese AGG.__
Inserendo il valore '1' viene attivata la gestione delle spese aggiuntive. Il programma di contabilizzazione, prima di creare la registrazione (Formato CONTABILIZZAZIONE), dà la possibilità di integrare la fatture con le spese/sconti, imputando la relativa aliquota (anche diversa dal formato guida).
Può essere implementata la tabella G9S per memorizzare le spese più frequenti.
 :  : FLD T$G91R __Contab.Interattiva.__
Inserendo il valore '1', si indica al programma di controllo fatture passive che si vuole contabilizzare la fattura in modo IMMEDIATO. Questa funzione è possibile solo dove la contabilità generale installata lo permette. (Programma di riferimento G9CF65_xx dove xx è la contabilità installata).
 :  : FLD T$G91S __Param. Cont.Inter.__
È possibile passere un parametro al programma che esegue la contabilizzazione interattiva.
 :  : FLD T$G91Q __Gest.forn.ult.record.__
Inserendo il valore '1', si indica al programma di contabilizzazione delle fatture passive che, nella registrazione contabile, la riga del fornitore DEVE essere l'ultima. Se lasciato bianco assume che sia la prima (verificare quale soluzione prevede la contabilità installata).
 :  : FLD T$G91T __Agg.Ass.Iva in test.__
Inserendo il valore '1', si indica al programma di contabilizzazione delle fatture passive che durante l'aggiornamento delle testate documenti verrà memorizzato anche l'assoggettamento IVA (T§CASI) della registrazione contabile (se diversa da '  ')

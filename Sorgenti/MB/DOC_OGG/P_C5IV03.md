## Prerequisiti
Aver compilato correttamente i seguenti campi della tabella IVA : 
 * T$IVAM :  Esclusione Elenco Clienti  (assoggettamenti che non vanno trasmessi per i clienti)
 * T$IVAR :  Esclusione Elenco Fornitori (assoggettamenti che non vanno trasmessi per i fornitori)
 * T$IVAF :  Codice Esenzione (per caratterizzare nel modo corretto gli assogettamenti). Quest'ultimo può assumere i seguenti valori : 
 ** "  "= Operazione Imponibile
 ** "NI"= Operazione Non imponibile
 ** "ES"= Operazione Esente
 ** "NE"= Operazione con IVA non esposta

## Dati di input
 * _2_Esercizio :  Determina quale esercizio elaborare
 ** Note Variazione Anno Precendente :  Se indicata verrano compilate anche i dati relativi agli importi di note di variazione degli anni precedenti (informazione opzionale per gli esercizi 2006-07)
 * _2_Codice Fiscale :  Tramite questa opzione posso decidere come trattare il dato del codice fiscale (opzionale per gli esercizi 2006-07)
 * _2_Tipi di Registrazione da escludere :  posso indicare una lista di tipi di registrazione da escludere a priori
 * _2_Partite IVA da escludere :  posso indicare una lista di partite IVA da escludere a priori
 * _2_Parzializzazioni :  Se si vuole filtrare in modo particolare le registrazioni (anche solo per poter fare delle prove su alcune registrazioni senza dover elaborare ogni volta tutto l'esercizio)
 * _2_Trasferimento :  Definizione del trasferimento del file da impostare obbligatoriamente.

## Descrizione dell'elaborazione
Vengono letti tutti i documenti IVA attivi/passivi aventi data documento all'interno dell'esercizio in esame, al fine di produrre le seguenti informazioni : 

### Clienti
 * Operazioni da inserire nell'elenco clienti
 ** Soggetti :  tutti i soggetti per i quali sono state emesse delle fatture/note nell'anno (titolari di partita IVA o consumatori finali)
 ** Dati da indicare : 
 *** Codice fiscale (obbligatorio)
 *** Partita IVA (se ne è titolare)
 *** Operazioni Imponibili
 *** Operazioni Imposta afferente (cioè l'imposta delle operazioni imponibili)
 *** Operazioni Non Imponibili
 *** Operazioni Esenti
 ** Note di variazione :  tutte le note vanno al netto di tutte le note dell'esercizio (che facciano riferimento ad una fattura dell'esercizio precedente o meno)
 * Operazioni escluse dall'elenco clienti
 ** le esportazioni di cui all'articolo 8, comma 1, lettere a) e b) del dPR n. 633 del 1972 (cessione all'esportazione diretta  e cessione all esportazione con trasporto a cura del cessionario non residente)
 ** le cessioni intracomunitarie di beni e servizi (escluse quelli intestate a soggetti titolari di partita IVA italia/codice fiscale)
 * Esoneri per gli anni 2006/07
 ** possono indicare anche solo la partita iva
 ** operazioni relative a fatture di importo a 154,94, registrate cumulativamente
 ** operazioni relative a fatture emesse per le quali non è prevista la registrazione ai fini IVA
 ** operazioni il cui importo comprensivo dell'imposta è stato annotato nel registro dei corrispettivi

### FORNITORI
 * Operazioni da inserire nell'elenco fornitori
 ** Soggetti :  tutti i soggetti per i quali sono state ricevute delle fatture/note nell'anno e che sono titolari di partita IVA
 ** Dati da indicare : 
 *** Codice fiscale (obbligatorio)
 *** Partita IVA (obbligatorio)
 *** Operazioni Imponibili
 *** Imposta afferente (cioè l'imposta delle operazioni imponibili)
 *** Operazioni Non Imponibili
 *** Operazioni Esenti
 *** Operazioni imponibili comprensive dell'imposta afferente (in fattura sono divisi ma per alcune deroghe particolari possono essere registrate con un unico importo)
 ** Note di variazione :  tutte le note vanno al netto di tutte le note dell'esercizio (che facciano riferimento ad una fattura dell'esercizio precedente o meno)
 * Operazioni escluse dall'elenco fornitori
 ** le importazioni di cui all'art. 68 e seg. del dPR n. 633 del 1972
 ** gli acquisti intracomunitari di beni e servizi
 * Esoneri per gli anni 2006/07
 ** possono indicare anche solo la partita iva
 ** operazioni relative a fatture di importo a 154,94, registrate cumulativamente
 ** operazioni relative a fatture emesse per le quali non è prevista la registrazione ai fini IVA

## Stampe di controllo
Il programma produce tre stampe : 
 - IVA_CTR :  Stampa di controllo dei dati che verranno trasmessi
 - IVA_WAR :  Stampa di warning per segnalare quali elementi vengono (correttamente) esclusi dalla trasmissione
 - IVA_ERR :  Errori nei dati mancanti obbligatori per la trasmissione

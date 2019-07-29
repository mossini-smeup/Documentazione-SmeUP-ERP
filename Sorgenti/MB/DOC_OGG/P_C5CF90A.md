# CONTROLLO FATTURE - RICEZIONE E.D.I.

# DEFINIZIONE
La ricezione E.D.I. riceve e controlla le fatture di acquisto provenienti da un sistema esterno con Smeu_up.
Il flusso è diviso in tre passi : 
    _7_. ricezione
    _7_. applicazione
    _7_. controllo

## Ricezione
I dati vengono trasferiti da un file esterno in AS/400.

## Applicazione
I dati ricevuti vengono trasformati in dati contabili Smeup.

## Controllo
I dati contabili sono integrati con i dati del gestionale.

Ad ogni passo è possibile eseguire una stampa di controllo con le informazioni sull'esito dell'elaborazione.

Creando opportune memorizzazioni video è possibile eseguire tutta la procedura o alcuni suoi passi in batch. Eseguire il programma master C5CF90A passando come parametro di chiamata il nome della memorizzazione video.


T01 RICEZIONE
Tutti i files presenti in una specifica cartella PC vengono trasferiti in AS/400 nel file EDRECI0F.
I dati sono inseriti con livello/stato 2/10.

E' necessario definire : 
    _7_. il messaggio
    _7_. il percorso PC
    _7_. il numeratore del messaggio.

## Messaggio
Costruire nella rispettiva tabella EDR codice e descrizione, non sono richieste altre informazioni.
Il messaggio identifica sul file EDRECI0F le diverse tipologie di ricezione E.D.I.
Ad esso sono legate tutte le impostazioni di ricezione : 
     - percorso PC;
     - numeratore EDRECI0F;
     - programma di applicazione;
     - parametri di controllo.

## Percorso PC
Il percorso definisce dove risiedono i files da ricevere.
Devono trovarsi in una cartella IFS AS/400. Vi si accede da risorse di rete con \\XXX.XX.X.XX dove XX.. è l'indirizzo IP AS/400. Una volta elaborati i files vengono cancellati.

## Numeratore
Ad ogni ricezione viene attibuito al file EDRECI0F un numero progressivo. Il valore è scritto nel campo numero lotto.


# APPLICAZIONE
Elabora tutti i dati nel file EDRECI0F in stato 2/10 e costruisce la registrazione contabile di acquisto con le relative bolle. I dati elaborati a buon fine passano a stato 8/60 o 8/80 in funzione dell'esito dei controlli contabili.
 In "visulizzazione dati" è possbilie vedere i dati ricevuti con il relativo stato di avanzamento.

E' necessario definire : 
    _7_. il programma di applicazione messaggio
    _7_. gli alias
    _7_. la fonte E.D.I.
    _7_. il conto di ricezione E.D.I.

## Programma applicazione
Il nome del programma deve necessariamente essere C5CF90_XX, dove XX è un suffisso libero.
E' il programma specifico relativo alla tipologia di messaggio E.D.I. ricevuto. In funzione dei vari tipi di record costruisce la registrazione contabile e le sue bolle. La registraziona contabile viene prima costruita nel C5BATC0F e successivamente applicata, ossia trasformata in registrazione contabile effettiva.
Questo comporta che anomalie contabili fermano la registrazione nell'immissione batch. Oltre alle segnazioni su stampa ciò è visibile dagli stati del file EDRECI0F. La cotruzione del batch porta lo stato di tutti i record a buon fine a 8/60. La trasformazione in registrazione effettiva porta lo stato degli stessi record a 8/80. Il primo passaggio viene eseguito direttamente dal programma specifico. Il secondo è attivabile inserendo un passo di flusso di immissione E4 con progr.C5CF90D.
Le bolle relative alla fatture ricevute sono scritte nei files V5TDOC0F/V5RDOC0F con tipo documento specificato nella fonte.

## Alias
Sono tutte le trascodifiche necessarie al programma specifico per interpretare il significato dei dati esterni ricevuti.
Poichè molti di questi dati assumono significato fisso all'interno della ricezione è possibile creare un programma, C5CF90_XXP, che li ricostruisce automaticamente. Ulteriori alias variabili, come i fornitori.. sono da inserire manualmente. L'esecuzione del programma CANCELLA tutti gli alias creati automaticamente e li ricostruisce sulla base delle informazioni presenti nello stesso programma. Inoltre RIFASA anche le eventuali tabelle in esso definite. manualmente con i dati ente/articolo.

## Fonte
E' la fonte con cui vengono lette in contabilità le bolle di tipo E.D.I. ricevute con la fattura. E' obbligatoria come origine fonte "09".

## Conto contabile
La registrazione contabile assume come unica contropartita il conto contabile specificato nella tabella della fonte.
E' obbligatorio ed è necessario definirne uno apposito in quanto il controllo poi elabora tutte le registrazione che hanno valori su questo conto.


# CONTROLLO
Il sistema elabora tutte le registrazioni che hanno valore di contropartita sul conto di ricezione E.D.I.

Per ogni registrazione contabile vengono caricate tutte le bolle ricevute con la fattura(previste) e tutte le bolle del gestionale in attesa di pagamento(effettive).

Per ogni bolla si totalizza a livello di articolo e di bolla : 
    >- quantità
    >- prezzo
    >- numero di righe
    >- numero di articoli(solo a livello di bolla)

I controlli sono eseguiti su tre livelli : 
   _7_. articolo
   _7_. bolla
   _7_. fattura

I parametri di controllo definiti nella impostazioni(per le anomalie a livello di articolo/bolla) e nella tabella C56(per le anomalie a livello di fattura), definiscono la modalità di ricezione, segnalazione messaggi di anomalie e eventuale blocco pagamento della fattura.

## Controllo articolo
Alla presenza di un'anomalia l'articolo non viene ricevuto e viene bloccato il pagamento della fattura.

## Quadratura
E' il limite entro il quale una differenza di valore dell'articolo fra la bolla prevista e effettiva non genera anomalia di differenza prezzo. Il delta rimane come residuo.

## Mancante
Segnala la mancanza di un articolo nella bolla effettivarispetto alla bolla prevista.

## Numero righe
Segnala la differenza del numero di righe che compongono l'articolo nella bolla prevista e effettiva.

## Differenza quantità
Segnala la differenza di quantità fra l'articolo della bolla  prevista e effettiva.

## Differenza prezzo
Segnala la differenza di prezzo fra l'articolo delle bolla prevista e effettiva.

## Controllo bolla : 
Alla presenza di un'anomalia la bolla non viene ricevuta e viene bloccato il pagamento della fattura.

## Quadratura
E' il limite entro il quale una differenza di valore fra la bolla prevista e effettiva non genera anomalia di differenza prezzo. Il delta rimane come residuo.

## Mancante
Segnala la mancanza di una bolla effettiva rispetto alle previste.

## Numero articoli
Segnala la differenza del numero di articoli che compongono la bolla prevista e effettiva.

## Numero righe
Segnala la differenza del numero di righe che compongono la bolla prevista e effettiva.

## Differenza quantità
Segnala la differenza di quantità fra la bolla prevista e effettiva.

## Differenza prezzo
Segnala la differenza di prezzo fra la bolla prevista e effettiva.

## Controllo fattura
Alla presenza di un'anomalia viene bloccato il pagamento della fattura.

## Quadratura
E' il limite entro il quale un valore residuo sulla fattura  non genera anomalia di differenza prezzo ma viene integrato come quadratura fattura.

## Modalità pagamento
Segnala la differenza fra la modalità di pagamento della fattura una bolla effettiva.

## Non conforme qualità
Segnala la presenza nelle bolle effettive di un lotto non conforme.

## Blocco pagamento
 Segnala la presenza di una bolla che prevede un blocco di pagamento :  per validazione, ...

## Residuo
 Segnala la presenza di un valore residuo sulla fattura.

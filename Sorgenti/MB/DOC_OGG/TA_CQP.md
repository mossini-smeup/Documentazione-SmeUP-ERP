# CQP - Piano controllo qualità
 :  : DEC T(ST) K(CQP)
## OBIETTIVO
Definire la struttura della tabella del piano di campionamento, stabilendone le intestazioni delle colonne e le tipologie dei campi.
Legare il piano di campionamento descritto ad un piano di riferimento.
## TIPO DI CAMPIONAMENTO
I Piani di Campionamento normalmente usati sono indicati in tabelle di derivazione statistica (fanno normalmente origine alle  tabelle  "Military  Standard 105  D"), che permettono di ricavare : 
-    quanti  pezzi estrarre dal lotto, in base alle sue dimensioni, per formare il campione
-    quanti  pezzi "Non Conformi" sono ammessi  nel campione per decidere, in funzione dell'L.Q.A. stabilito, l'accettabilità del lotto.
Generalmente il piano di campionamento può essere suddiviso in : 
- Campionamento Semplice
- Campionamento Doppio
per entrambi i casi è definibile la scelta in : 
- NORMALE
- RINFORZATO
- RIDOTTO.
Esistono pertanto sei possibilità di campionamento.
### Campionamento semplice
In base alla grandezza del lotto si trova, sul Prospetto, la grandezza del  campione. Si esegue il collaudo dei pezzi componenti il campione,  individuando i pezzi "Non Conformi". In base all'L.Q.A. stabilito si trova, nella tabella, il numero di accettazione C.
Se il numero di pezzi "Non Conformi" individuato nel campione è minore od uguale a C, si accetta il lotto.
_9_Esempio : 
Si deve verificare un lotto di 3000 perni, con controllo normale, per i quali è stato stabilito un L.Q.A. pari a 1. In  base alla tabella, deve essere estratto un campione di 150 pezzi che, per L.Q.A. fissato, ammette un numero massimo (C) di pezzi "Non Conformi" uguale a 4.
Fino a 4 pezzi "Non Conformi" si accetta il lotto.
Oltre i 4 pezzi si scarta l'intero lotto e si procede alla selezione al 100%.
### Campionamento doppio
**Primo Campione**
In base alla grandezza del lotto si trova, sul prospetto, la numerosità' del "primo campione".
Si esegue il collaudo del primo campione e si individua il numero dei pezzi "non conformi" presenti.
In base al L.Q.A. fissato si trovano, sul prospetto, i numeri di accettazione "C1" e "C2".
Se il numero di pezzi "non conformi" individuato nel primo campione è minore o uguale a "C1", si accetta il lotto.
Se il numero di pezzi "non conformi" individuato nel primo campione è maggiore di "C1", ma minore di "C2", si deve procedere all'esame di un secondo campione.
Se il numero di "non conformi" individuati nel primo campione è maggiore di "C2", si scarta il lotto.
**Secondo Campione**
A fronte di una condizione di ricontrollo, si verifica un secondo campione la cui grandezza è sempre indicata nella tabella 105.D.
Si  esegue il collaudo del secondo campione e si individua il numero di pezzi "non conformi".
Se il numero di pezzi "non conformi" del primo e del secondo campione, sommati assieme, è inferiore a "C2" si accetta il lotto, in caso contrario il lotto viene scartato.
_9_Esempio : 
Consideriamo sempre il lotto di 3000 perni con L.Q.A. = 1. In base alla tabella deve essere estratto un primo campione di 100 pezzi. I pezzi vengono controllati e se ne trovano 3 "non conformi".
I numeri di accettazione indicati della tabella sono : 
C1 = 2                C2 = 5
Nell'esempio, il numero di pezzi "non  conformi" del primo campione è compreso tra C1 e C2.
Si deve quindi estrarre un secondo campione di 200 pezzi.
Nel secondo campione si individuano altri 2 pezzi "non conformi".
Il numero totale dei pezzi "non conformi" del primo e del secondo campione risulta pertanto di 3+2 =5.
Poiché questo numero è uguale ma non superiore a C2, si accetta il lotto.
Per i pezzi "non conformi" superiori a 5 si scarta il lotto.
### Confronto tra campionamento Semplice e Doppio
I due sistemi di campionamento hanno la stessa validità statistica (che non significa sicurezza matematica dei risultati). La scelta dell'uno o dell'altro metodo è normalmente dettata da una maggiore convenienza pratica o economica.
**CAMPIONAMENTO SEMPLICE - (S)**
Il  numero dei pezzi da controllare è superiore a quello del "primo campione" del campionamento doppio. Diventa inferiore se, per il campionamento doppio, si deve ricorrere al "secondo campione".
Il  metodo è di più semplice applicazione e trova un utilizzo vantaggioso quando il costo del collaudo non è eccessivo.
**CAMPIONAMENTO DOPPIO - (D)**
Il numero dei pezzi da controllare è inferiore, per il primo campione, a quello del campionamento semplice. Tuttavia diventa superiore se si deve ricorrere al secondo campione.
La convenienza del metodo è da valutarsi in base al tipo di produzione ed in funzione del grado di affidabilità dei processi produttivi o del fornitore. Se l'affidabilità è buona il metodo è conveniente; diventa invece aleatorio a fronte di dubbia affidabilità.
## SCELTA DEL PIANO DI CAMPIONAMENTO
La scelta del "piano di campionamento" deve essere fatta in funzione di vari fattori, tra cui : 
- forma e dimensione dei pezzi da controllare;
- facilità o difficoltà di prelevare i pezzi per formare il campione;
- difficoltà e tempo di collaudo;
- dati storici di affidabilità del processo produttivo per il particolare da controllare;
- necessità di elaborare statistiche per verificare l'andamento del prodotto nel tempo.
**PREMESSA**
Le tabelle usate per i piani di campionamento, di qualsiasi derivazione esse siano, indicano un numero di pezzi "non conformi" ammessi nei campioni. Come è verificabile, questo numero è costantemente superiore all'L.Q.A. stabilito, ossia alla percentuale dei pezzi "non conformi" ammessi nel lotto.
Si tratta di una situazione statistica generalmente accettata (margine di sicurezza per l'imprecisione matematica dei risultati), anche se può comportare una certa percentuale di rischio, con una percentuale effettiva di pezzi "non conformi" superiore a quella stabilita, possano essere
accettati e che di conseguenza possano essere scartati lotti con una percentuale effettiva di pezzi "non conformi" inferiore a quella stabilita.
**SCELTA DEL METODO**
La scelta del metodo di controllo viene generalmente basata sulle "conoscenze storiche" che si hanno o per i processi produttivi o per le  forniture (naturalmente sempre a livello del singolo particolare). In assenza di "conoscenze storiche" è bene, utilizzando il "controllo normale", verificare almeno 5 lotti di un determinato prodotto (sia esso interno o esterno), calcolare la "media del livello di qualità" per poi formulare la scelta, nell'ambito dei due piani di campionamento, tra  controllo : 
- normale
- rinforzato
- ridotto.
(Il calcolo della "media del livello di qualità" si esegue dividendo il numero complessivo dei pezzi "non conformi", individuati nei 5 campioni, per il numero complessivo dei pezzi controllati. Se l'analisi viene condotta con il sistema di campionamento doppio, si devono considerare solo i 5 primi campioni.)
### CONTROLLO NORMALE - (N)
Viene impiegato : 
- per particolari non interessati da caratteristiche Critiche
- quando normalmente si è in assenza di consolidate "conoscenze storiche"
- qualora "la media del livello di qualità", esaminata al punto precedente, risulti allineata ai valori di accettabilità stabiliti nella tabella.
### CONTROLLO RINFORZATO - (R)
Quando la "MEDIA DEL LIVELLO DI QUALITÀ'" è superiore, in forma sensibile all'L.Q.A., si deve dedurre che i lotti forniti hanno mediamente qualità peggiore di quella attesa.
Per riportare il "LIVELLO DI QUALITÀ MEDIO" al valore stabilito si deve usare un sistema di controllo più rigoroso definito, appunto, "CONTROLLO RINFORZATO".
Il "Controllo rinforzato" è comunque consigliabile a fronte di particolari interessati da caratteristiche classificate Critiche o notevolmente importanti.
## CONTENUTO DEI CAMPI
 :  : FLD T$TIC1 **Car1**
Tipo di rilievo a cui si riferisce il piano di campionamento : 
- Attributi
- Variabili
 :  : FLD T$TIC3 **Car2**
Tipo di controllo a cui si riferisce il piano di campionamento : 
- Normale
- Ridotto
- Rinforzato
 :  : FLD T$TIC2 **Car3**
Modalità di ispezione sul lotto : 
- Semplice
- Doppio
- Multiplo
 :  : FLD T$INT1 **Intestazione 1/7**
Intestazione delle colonne del piano di campionamento
 :  : FLD T$NUM1 **Numero decimali 1/7**
Numero dei decimali nella colonna descritta. Se il campo è lasciato vuoto si intende che la colonna è di tipo alfanumerico
 :  : FLD T$PIRI **Piano di riferimento**
Campo controllato nella tabella CQP. È il piano di riferimento che permette al sistema, in funzione della numerosità del lotto e del tipo di campionamento, di determinare la lettera di riferimento per l'entrata nel piano di campionamento in esame.
 :  : FLD T$CAFV **Tipo di campionamento**
Campo non controllato

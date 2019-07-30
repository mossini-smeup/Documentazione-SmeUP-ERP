 :  : PRO.SER Cod="ANA.PER" Tit="Analisi cose di un oggetto" Fun="F(EXB;D5COSO_01;ANA.PER) INPUT(Par(Con(-(O;;TAD5S;Contesto)) Tem(-(O;;TAD5O;Tema)) Per(-(O;;TAPER;Periodo)) K00(-(O;;CSF-D5COSO0FD$CODI;Codice)) K01(-(O;;CSF-D5COSO0FD$COD1;Codice 1)) K02(-(O;;CSF-D5COSO0FD$COD2;Codice 2)) K03(-(O;;CSF-D5COSO0FD$COD3;Codice 3)))"

 :  : HEA RESP(GR) USAG(AS) STAT(80)
# Analisi cose di un oggetto
Questo servizio ha l'obiettivo di fornire uno strumento di navigazione nei costi D5 e di creare interrogazioni ad hoc le cui funzioni possono essere salvate nelle schede personalizzate.

# Funzione/metodo ANA.PER

## Obiettivo funzione/metodo ANA.PER
Questo metodo fornisce tutte le possibili funzionalità di interrogazione dei costi D5 con gestione particolare dei periodi ed estraendo i dati secondo le modalità qui definite.

## Parametri
I parametri devono essere contenuti in £UIBD1 nella variabile Par(). Quando è indicato che il parametro è valore multiplo il separatore dei valori è il ";", valore singolo significa che il parametro può contenere un solo valore.

## Filtri obbligatori : 
* Con()  Valore singolo di filtro per la selezione sul campo "contesto" D$TIPA, Esempio :  Con(CNCOL)
* Tem()  Valore multiplo di filtro per la selezione sul campo "tema" D$TROT, Esempio :  Tem(F02;F03)
         Nota :  il valore multiplo nel campo Tem() permette di interrogare informazioni da diversi
               temi, tipicamente utilizzabile per i temi che contengono le repliche dei progressivi
               YTD.
## Filtri di selezione : 
* K00()  Valore multiplo di filtro per la selezione sul campo codice D$CODI. Esempio :  K00(10;11)
         E' pure possibile utilizzare allo stesso modo la variabile D$CODI(). Esempio :  D$CODI(10;11)
* K01()  Valore multiplo di filtro per la selezione sul campo codice D$COD1. Esempio :  K01(A0;C1)
         E' pure possibile utilizzare allo stesso modo la variabile D$COD1(). Esempio :  D$COD1(A0;C1)
* K02()  Valore multiplo di filtro per la selezione sul campo codice D$COD2. Esempio :  K02(XX;YY)
         E' pure possibile utilizzare allo stesso modo la variabile D$COD2(). Esempio :  D$COD2(XX;YY)
* K03()  Valore multiplo di filtro per la selezione sul campo codice D$COD3. Esempio :  K03(QA;X8)
         E' pure possibile utilizzare allo stesso modo la variabile D$COD3(). Esempio :  D$COD3(QA;X8)
* Per()  Valore multiplo di filtro per selezione sul campo periodo D$DTVA. Esempio :  Per(2014;2015)
         Può contenere anche il valore M per mese ultima chiusura o A per anno. Esempio :  Per(M)
         Nota :  il parametro Per() è gestito anche come parametro di output, vedere il paragrafo
         apposito.
* Oav..  Valori singoli per la selezione sugli OAV degli oggetti D$CODI e D$COD1-2-3.
         I parametri sono OavX() e VOavX() per indicare l'OAV e il relativo valore dell'oggetto X,
         pertanto i parametri OAV e relativo valore solo : 
         . Oav0() e VOav0() per il campo D$CODI.
         . Oav1() e VOav1() per il campo D$COD1.
         . Oav2() e VOav2() per il campo D$COD2.
         . Oav3() e VOav3() per il campo D$COD3.

## Parametri elaborazione : 
* Val()  Valore multiplo, contiene gli indici dei numeri da gestire. Esempio :  Val(48;49)
         In alternativa può contenere *ALL che significa tutti gli indici. Esempio :  Val(*ALL)
         Può infine contenere una lista indici come variabile LI. Esempio :  Val(LI(nomelista))

## Output : 
* Det()  Valore singolo, abilita la prima colonna di click per dettaglio. Esempio :  Det(1)
* Rig()  Valore multiplo, indica l'elenco dei campi utilizati come rottura delle righe.
         Se non impostato nessun campo vengono visualizzati tutti.
         Il campo D$DTVA viene decodificato rispetto al valore in esso cuntenuto, pertanto
         il servizio interpreta se contiene anno, mese o giorno.
         Esempio :  Rig(D$COD2;D$COD3;D$DTVA)
* Col()  Valore singolo. abilita un campo che deve essere gestito come n colonne, pertanto
         ogni valore in esso contenuto diventa una colonna. Esempio :  Rig(D$COD1)
* ValRC() Valore singolo. indica come devono essere trattati i campi numerici.
          Se contiene 'R' i valori Val vengono caricati come righe. Esempio :  ValRC(R)
          Se contiene 'C' i valori Val vengono caricati come colonne. Esempio :  ValRC(C)
          Se contiene ' ' i valori Val vengono tutti sommati nelle colonne (Col/Mesi/Anni)
* RepVal() Valore singolo. Permette di replicare tutte le colonne aggiungendo
           agli indici il valore contenuto, tipicamente col valore 50 per Val(27;32) vengono
           aggiunte le colonne 77 e 82. Vengono replicate anche le eventuali colonne calcolate,
           per esempio il Delta e il Delta %. Esempio :  RepVal(50)
           Nota :  questo parametro non è compatibile con la colona aggiuntiva Tot(1) in quanto
                 sommatoria di tutte le colonne.
* Mesi() Valore singolo, abilita la gestione di colonne mesi dell'anno selezionato e 0 anno attuale.
         Il valore deve essere compreso tra 0 e -10. Esempio :  Mesi(-1)
* Anni() Valore multiplo, abilita la gestione colonne anni e 0 è l'anno attuale.
         I valori devono essere compresi tra 0 e -10. Esempio :  Anni(0;-1;-2;-3;-4)
* Giorni() Valore singolo, abilita la gestione di colonne giorni di un mese fisso, che è utilizzato
           come parametro di filtro. Esempio :  Mesi(201501)
* Per()    Valore multiplo, abilita la gestione colonne a periodi fissi. Esempio :  Per(2016;2015)
* NoTit()  Valore singolo. Se impostato non emette il titolo. Esempio :  NoTit(1)
* NoZero() Valore singolo. Se impostato non emette le righe con tutti i valori a zero.
           Esempio :  NoZero(1)
* NoFlt()  Sulla sottoscheda NAVEXT disattiva i dinamismi che al click applicavano il filtro
* NoTot()  Sulla sottoscheda NAVEXT disattiva l'applicazione automatica di forme di totalizzazione

  Nota :  Solo uno dei parametri Mesi/Anni/Giorni/Per deve essere impostato come selezione periodo.
        L'uso di Col() non preclude l'uso di Mesi/Anni/Giorni/Per che in tal caso vengono unitizzati
        solo come filtro di selezione temporale dei dati che verranno caricati nelle colonne.

## Output colonne calcolate (vengono aggiunte in fondo come ultime colonne).
  Sono valori singoli che possono contenere solo "1" : 
* Tot(1) Abilita una colonna totale, come sommatoria di tutte le colonne. Esempio :  Tot(1)
* Med(1) Abilita una colonna con la media di tutte le colonne. Esempio :  Tot(1)
* Dif(1) Abilita una colonna con la differenza tra le prime 2 colonne. Esempio :  Dif(1)
* Dip(1) Abilita una colonna con % la differenza tra le prime 2 colonne. Esempio :  Dip(1)
* Raf()  Valore singolo, abilita la gestione raffronto periodi rispetto all'ultima chiusura. Il
         valore può essere M per raffronto ultimo mese o A per ultimo anno. Esempio :  Raf(M)

## Colonne calcolate da formule definite in script D5COSO_xx (xx è il S/S indici TAIGI da TAD5O)
  ParScp() contiene la Sezione.Subsezione del modello di colonne da utilizzare in output.
  Valore singolo. Esempio :  ParScp(A.A)
  Rispetto alle colonne calcolate di cui al precedente paragrafo queste vengono replicate   per ogni colonna definita nel parametro Col().
  Nella subsezione  :  : COS.COL definisce ogni singola colonna.

  Ecco alcuni esempi delle colonne disponibili : 
  * DET I dati del record selezionato
     :  : COS.COL Met="DET" Txt="Dati|attuali"      Par="01(V01-V02) 04(V04-V01) 03(V03+V10)"
  * REP Replica YTD, indicare nel parametro il valore da aggiungere, tipicamente il valore 50
    Si riferisce all'ultimo record letto, dopo un metodo LET effettua la replica YTD sui suoi dati
     :  : COS.COL Met="REP" Txt="Replica|YTD"      Par="50"
  * FOR Formula di riga, effettua la differenza tra la colonna 1 e la colonna 2
     :  : COS.COL Met="FOR" Txt="Formula|01-02"     Par="V01-V02"
  * FOC Formula di colonna, Si riferisce all'ultima colonna caricata. Nella prima riga mette la
    differenza tra riga1 e riga 2, nella quarta riga la differenza tra la quarta e la prima ..
     :  : COS.COL Met="FOC" Txt="Formula|colonna" Par="01(V01-V02) 04(V04-V01) 27(V22+V27)"
  * FOD Formula di record. Si riferisce al record selezionato. Nella prima riga mette la differenza
    tra indice 1 e 2, nella 4a riga..
    Si riferisce al record selezionato.
     :  : COS.COL Met="FOD" Txt="Formula|di record" Par="01(V01-V02) 04(V04-V01) 27(V22+V27)"
  * IN1 Incidenza da tabella IGI (opzione 1 nell'UP COS). Ogg NRP indica %, Lun lunghezza e decimali
     :  : COS.COL Met="IN1" Txt="Incidenza %" Ogg="NRP" Lun="20;2"
  * IN9 Totale quantità da tabella IGI (opzione 9 nell'UP COS)
     :  : COS.COL Met="IN9" Txt="Totale|Quantità (9)"
  * LET Lettura di un altro record lasciando fermi gli altri parametri del record selezionato
     :  : COS.COL Met="LET" Txt="Collaboratore|DOWMAR" Par="D$COD3(DOWMAR)"
    £' possibile indicare direttamente l'oggetto al posto del campo
     :  : COS.COL Met="LET" Txt="Collaboratore|DOWMAR" Par="CNCOL(DOWMAR)"
    £' possibile indicare direttamente l'oav di un oggetto su un campo
     :  : COS.COL Met="LET" Txt="Sua|Azienda"          Par="D$CODI(&CO.OAV.D$COD3(U/001))"
    £' possibile indicare direttamente l'oav di un oggetto su un altro oggetto
     :  : COS.COL Met="LET" Txt="Sua|Azienda"          Par="CNAZI(&CO.OAV.CNCOL(U/001))"
  * SEP Colonna vuota di separazione
     :  : COS.COL Met="SEP"

# Modelli, funzione/metodo ANA.MOD

## Obiettivo funzione/metodo ANA.MOD
I modelli permettono di avere dei layout predefiniti tramite la variabile Mod(), valore singolo.
Valori ammessi : 
* R esegue l'output del modello "Raffronto";
* E esegue l'output del modello "Elenco";
* A1 esegue l'output del modello "Andamento 1";
* A2 esegue l'output del modello "Andamento 2".


# Singolo record, funzione/metodo ANA.REC

## Obiettivo funzione/metodo ANA.REC
Questo servizio fornisce le funzionalità di base di interrogazione dei costi D5 estraendo
i dati di un singolo record.

## Parametri di selezione
L'accesso per singolo record tramite numero relativo di record del D5COSO0F avviene tramite
l'oggetto 1. Esempio :  1(ID;D5COSO0F;[$_RRN])

In altrnativa è possibile passare gli stessi parametri definiti nel metodo ANA.PER nel paragrafo
"Filtri di selezione" (essendo necessari alla definizione di un singolo record non sono
disponibili i filtri sugli OAV).
Per esempio :  Con(CNAZI) Tem(F02) K00(10) K01(10) K02(RA) K03(AZZPAT) Per(201502)

## Parametri elaborazione : 
Allo stesso modo dell'ANA.PER è disponibile il solo parametro Val().

## Filtro da lista oggetti.
Il metodo ANA.REC il D5COSO_01 gestisce in input la possibilità di passare una lista oggetti
da collegare al record passato tramite queste 2 variabili : 
* LisOgg(CNNOM) indica che la lista oggetti che viene passata è da collegare al campo il cui oggetto
  è CNNOM. Valore unico. Alternativo a LisFld().
* LisFld(D$COD3) indica che la lista oggetti che viene passata è da collegare all'oggetto contenuto
  in D$COD3. Valore unico. Alternativo a LisOgg().
* LisNam(STA) è il nome della lista oggetti sui parametri di cui sopra.

# Altre funzioni/metodi

## Funzione/metodo ANA.TRE
Costruisce un albero delle funzioni possibili sui dati selezionati nei parametri ricevuti.

## Funzione/metodo ANA.VAL
Costruisce l'elenco dei valori presenti nei dati selezionati dai parametri ricevuti.

## Funzione/metodo ANA.OGG
Questo metodo costruisce l'elenco dei parametri possibili per la costruzione dei dati per l'oggetto selezionato (definito nel contesto).

## Funzione/metodo ANA.PAR
Questo metodo costruisce l'elenco dei parametri presenti nella costruzione dei dati selezionati.

## Funzione/metodo ANA.DAT
Questo metodo effettua una semplice estrazione di tutti i dati selezionati.


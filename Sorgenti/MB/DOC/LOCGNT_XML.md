# Descrizione XML per servizio Gantt
Di seguito è riportato un esempio di XML per la definizione di un Gantt. Le varie sezioni sono documentate (parti in neretto) in modo da descrivere il contenuto e la funzionalità dei vari setup disponibili.
><?xml version="1.0" encoding="ISO-8859-1"?>
<Base Testo="SXML Gantt / Distinta e Schedulazione - Centro lavoro">

## Tipi di servizi implementati : 
 * _2_F(GNT,XXXYYY,OPN)= apertura del Gantt (chiamato in genere all'avvio). Richiede la definizione della griglia e del popup.
 * _2_F(GNT,XXXYYY,MOD= modifica di Gantt esistente. Vengono modificate solo le celle passate nel XML.
 * _2_F(GNT,XXXYYY,NEW)= reload totale. Tutte le celle attuali sono eliminate e vengono sostituite dalle celle definite nel XML.
 * _2_F(GNT,XXXYYY,CLO)= chiusura del Gantt. Rende definitive tutte le modifiche (se confermata)
> <Service Titolo1="SXML Gantt / Distinta e Schedulazione" Titolo2="Centro lavoro" Funzione="F(GNT;S5SER_01;OPN) 1(RI;CDL;) 2(;;) 3(;;) 4(;;) 5(;;) 6(;;) P() G(NFI)"/>
 <Header>
  <Livello Caratteristiche=" "/>
 </Header>

## Sezione di definizione funzioni di popup
E' una sezione di tipo generale e non relativa al caso specifico del Gantt. Consente di definire nuove funzioni associate al popup di oggetto.
> <UIPopup>
  <Oggetto Tipo="IR" Parametro="" Codice="" Testo="Schedulazione" Exec="R(S5SER_01C;SCH;OGG) 1([1 : 1 : 2];[1 : 3 : 10];[2])"/>
  <Oggetto Tipo="RI" Parametro="CDL" Codice="" Testo="Schedulazione" Exec="R(S5SER_01C;SCH;OGG) 1([1 : 1 : 2];[1 : 3 : 10];[2])"/>
  <Oggetto Tipo="RI" Parametro="CDL" Codice="" Testo="Matrice del centro" Exec="F(EXB;S5SER_01;LET) 1([1 : 1 : 2];[1 : 3 : 10];[2])"/>
  <Oggetto Tipo="RI" Parametro="CDL" Codice="" Testo="Calendario" Exec="A(B£FU01X;CAL;) 1([1 : 1 : 2];[1 : 3 : 10];[2]) P(CDL000031)"/>
  <Oggetto Tipo="OR" Parametro="" Codice="" Testo="Dettaglio" Exec="A(P5DV01X;05;) 1([1 : 1 : 2];[1 : 3 : 10];[2])"/>
  <Oggetto Tipo="OR" Parametro="" Codice="" Testo="Matrice dell&apos;ordine" Exec="F(EXB;S5SER_01;LET) 1([1 : 1 : 2];[1 : 3 : 10];[2])"/>
  <Oggetto Tipo="AR" Parametro="" Codice="" Testo="Matrice dell&apos;articolo" Exec="F(EXB;S5SER_01;LET) 1([1 : 1 : 2];[1 : 3 : 10];[2])"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Scelta funzione" Exec="R(S5SER_01C;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Impostazioni" Exec="R(S5SER_01C;GES;SET)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Schedulazione Modificati" Exec="R(S5SER_01C;SCH;NCH)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Schedulazione Globale" Exec="R(S5SER_01C;SCH;ALL)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Testo="Matrice">
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per articolo" Exec="F(EXB;S5SER_01;LET) 1(AR;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per centro" Exec="F(EXB;S5SER_01;LET) 1(RI;CDL;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per ordine" Exec="F(EXB;S5SER_01;LET) 1(OR;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per commessa" Exec="F(EXB;S5SER_01;LET) 1(CM;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per cliente" Exec="F(EXB;S5SER_01;LET) 1(CN;CLI;)"/>
  </Oggetto>
  <Oggetto Tipo="J1" Parametro="GRA" Testo="Grafico">
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per articolo" Exec="F(EXA;S5SER_01;LET) 1(AR;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per centro" Exec="F(EXA;S5SER_01;LET) 1(RI;CDL;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per ordine" Exec="F(EXA;S5SER_01;LET) 1(OR;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per commessa" Exec="F(EXA;S5SER_01;LET) 1(CM;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Per cliente" Exec="F(EXA;S5SER_01;LET) 1(CN;CLI;)"/>
  </Oggetto>
  <Oggetto Tipo="J1" Parametro="GRA" Testo="Liste di oggetti">
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Articoli" Exec="F(TRE;S5SER_01;SCO) 1(AR;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Centri" Exec="F(TRE;S5SER_01;SCO) 1(RI;CDL;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Ordini" Exec="F(TRE;S5SER_01;SCO) 1(OR;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Commesse" Exec="F(TRE;S5SER_01;SCO) 1(CM;;)"/>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Clienti" Exec="F(TRE;S5SER_01;SCO) 1(CN;CLI;)"/>
  </Oggetto>
  <Oggetto Tipo="J1" Parametro="GRA" Codice="" Testo="Scheda della schedulazione" Exec="F(EXD;-SCO;) 2(MB;SCP_SCH;S5_000)"/>
 </UIPopup>

## Griglia di definizione della tabella dati del Gantt
Una colonna indicata di tipo J4-ICO conterrà dei simboli grafici al posto del testo. Il valore XY indica il tipo di simbolo grafico da inserire : 
 * _1_X :  forma del simbolo secondo la tabella
 ** _2_0 :  per rombo
 ** _2_1 :  per rettangolo
 ** _2_2 :  per cerchio
 ** _2_3 :  per freccia con punta a destra (default)
 ** _2_4 :  per freccia con punta a sinistra
 ** _2_5 :  per freccia doppia con punta a destra
 ** _2_6 :  per freccia doppia con punta a sinistra
 ** _2_7 :  per freccia tripla con punta a destra
 ** _2>n_ :  per freccia tripla con punta a sinistra
 ** _2_9 :  per freccia con punta in alto
 ** _2_A :  per freccia con punta in basso
 ** _2_B :   per pipe verticale
 * _1_Y :  colore del simbolo secondo la tabella
 ** _2_1 :  per giallo
 ** _2_2 :  per verde
 ** _2_3 :  per blu
 ** _2_4 :  per bianco
 ** _2_5 :  per nero
 ** _2_6 :  per ciano
 ** _2_7 :  per rosso (default)
 ** _2>n_ :  per grigio
 ** _2_9 :  per arancio

Chiavi di colonna disponibili : 

* _1_D01 = Data iniziale dell'impegno
* _1_H01 = Ora iniziale dell'impegno
* _1_D02 = Data finale dell'impegno
* _1_H02 = Ora finale dell'impegno
* _1_S01 = Forma della cella impegno
** _2_0 Cella rettangolare standard (default)
** _2_1 Cella ovale
** _2_2 Cella rettangolare con angoli arrotondati
** _2_3 Cella a rombo
** _2_4 Cella triangolare crescente
** _2_5 Cella triangolare decrescente
** _2_6 Cella a trapezio crescente
** _2_7 Cella a trapezio decrescente
** _2>n_ Cella rettangolare senza riquadro sinistro-alto
** _2_9 Cella rettangolare senza riquadro destro-alto
** _2_A Cella rettangolare senza riquadro destro-basso
** _2_B Cella rettangolare senza riquadro sinistro-basso
* _1_L01 = Definizione intervalli per celle a livelli Esempio :  L01(0-9;10-49,50-79;80-99) definisce quattro livelli.
      NB(Per fare in modo che venga eseguita la separazione in livelli va indicata nella posizione 66 una "H")
* _1_D00? = Data dell'istante di tempo con codice ?
* _1_H00? = Ora dell'istante di tempo con codice ?
* _1_F00? =  Formato di visualizzazione dell'istante di tempo ?

? è un carattere qualsiasi che identifica univocamente un istante di tempo.
Ad esempio, se vogliamo definire l'istante di tempo A sarà necessario definire le tre chiavi D00A, H00A e F00A.
Il campo F00? contiene due numeri. Il primo definisce la forma dell'indicatore, il secondo il colore

La tabella di corrispondenza è la seguente :  F00? = XY dove : 

 * _1_X= codice forma del segnatempo
 ** _2_0 :  per rombo
 ** _2_1 :  per rettangolo
 ** _2_2 :  per cerchio
 ** _2_3 :  per freccia con punta a destra (default)
 ** _2_4 :  per freccia con punta a sinistra
 ** _2_5 :  per freccia doppia con punta a destra
 ** _2_6 :  per freccia doppia con punta a sinistra
 ** _2_7 :  per freccia tripla con punta a destra
 ** _2>n_ :  per freccia tripla con punta a sinistra
 ** _2_9 :  per freccia con punta in alto
 ** _2_A :  per freccia con punta in basso
 ** _2_B :  per pipe verticale
 * _1_Y= codice colore del segnatempo
 ** _2_1 :  per giallo
 ** _2_2 :  per verde
 ** _2_3 :  per blu
 ** _2_4 :  per bianco
 ** _2_5 :  per nero
 ** _2_6 :  per ciano
 ** _2_7 :  per rosso (default)
 ** _2>n_ :  per grigio
 ** _2_9 :  per arancio

* _1_FL1 = Flag di segnalazione posizionato in alto a destra
* _1_FL2 = Flag di segnalazione posizionato in basso a destra
* _1_FL3 = Flag di segnalazione posizionato in basso a sinistra
* _1_FL4 = Flag di segnalazione posizionato in alto a sinistra

>        FL4    ___________________________  FL1
                  |                                                     |
                  |                                                     |
        FL3    ___________________________   FL2

Il valore numerico contenuto nel campo FLx definisce il colore con cui disegnare il flag. FLx = Y dove
 * _1_Y= codice colore del flag
 ** _2_1 :  per giallo
 ** _2_2 :  per verde
 ** _2_3 :  per blu
 ** _2_4 :  per bianco
 ** _2_5 :  per nero
 ** _2_6 :  per ciano
 ** _2_7 :  per rosso (default)
 ** _2>n_ :  per grigio
 ** _2_9 :  per arancio

* _1_K01 = Identifica la colonna da utilizzare come chiave di raggruppamento
* _1_TXT = Identifica la colonna da ustilizzare come chiave per il reperimento del testo della cella
* _1_C01 = Identifica la colonna da usare come chiave per il colore
* _1_N01 = Identifica la colonna da usare come campo note di cella da visualizzare nella finestra di preview
* _1_N02 = Identifica la colonna da usare come campo note di cella da visualizzare nella statusbar del modulo grafico
* _1_G01 = Identifica la lista dei gruppi per spostamento di gruppo (codici separati per ;)
* _1_G02 = Flag per lista gruppo (1 solo gruppi passati nel G01, 0 o blank, tutti i gruppi)
* _1_M01 = Identificatore attività di tipo Master/Slave
* _1_HID = Identifica colonna che controlla l'Hide di una cella. Se 1 la cella esiste ma non è disegnata, se 0 viene disegnata
* _1_FIX = Identifica colonna che controlla la Zona. Può avere valore assegnato o essere vuota ed è utilizzata negli spostamenti di gruppo di tipo congelato.

Gestione work periods (zone del Gantt che devono essere evidenziate con un zebratura colorata)
* _1_DW1? = Identifica la colonna che contiene la data di inizio del workperiod identificato dal codice ?
* _1_HW1? = Identifica la colonna che contiene l'ora di inizio del workperiod identificato dal codice ?
* _1_DW2? = Identifica la colonna che contiene la data di fine del workperiod identificato dal codice ?
* _1_HW2? = Identifica la colonna che contiene l0ora di fine del workperiod identificato dal codice ?
* _1_CW1? = Identifica la colonna che contiene il colore da utilizzare per tracciare il workperiod ?
Codici colori : 
* _2_1 per giallo
* _2_2  per verde
* _2_3  per blu
* _2_4  per bianco
* _2_5  per nero
* _2_6  per ciano
* _2_7  per rosso (default)
* _2>n_  per grigio
* _2_9  per arancio
> <Griglia>
  <Colonna Cod="XXNMEM" Txt="Indice per modifica" Tip="" Lun="07" IO="H" Ogg="NR" Dpy="" Fill=""/>
  <Colonna Cod="SFCLAV" Txt="Risorsa" Tip="" Lun="15" IO="O" Ogg="RICDL" Dpy="" Fill=""/>
  <Colonna Cod="SFOPER" Txt="Fase" Tip="" Lun="06" IO="O" Ogg="" Dpy="" Fill=""/>
  <Colonna Cod="SFCOAR" Txt="Articolo" Tip="" Lun="15" IO="O" Ogg="AR" Dpy="" Fill=""/>
  <Colonna Cod="SFDEAR" Txt="Descrizione Articolo" Tip="" Lun="10" IO="O" Ogg="" Dpy="" Fill=""/>
  <Colonna Cod="S1FAMI" Txt="Famiglia" Tip="" Lun="10" IO="O" Ogg="--" Dpy="" Fill="C01"/>
  <Colonna Cod="SFNDOC" Txt="Ordine" Tip="" Lun="10" IO="O" Ogg="OR" Dpy="" Fill=""/>
  <Colonna Cod="SFPRIO" Txt="Priorità" Tip="" Lun="02" IO="O" Ogg="TAB§A" Dpy="" Fill=""/>
  <Colonna Cod="S§QTOR" Txt="Qtà schedulata" Tip="" Lun="08" IO="O" Ogg="NR" Dpy="" Fill=""/>
  <Colonna Cod="S§QORD" Txt="Qtà ordinata" Tip="" Lun="08" IO="O" Ogg="NR" Dpy="" Fill=""/>
  <Colonna Cod="S§DTIN" Txt="Data inizio" Tip="" Lun="08" IO="O" Ogg="D8-YYMD" Dpy="" Fill="D01"/>
  <Colonna Cod="S§HRIN" Txt="Ora inizio" Tip="" Lun="06" IO="O" Ogg="I12" Dpy="" Fill="H01"/>
  <Colonna Cod="S§DTFI" Txt="Data fine" Tip="" Lun="08" IO="O" Ogg="D8-YYMD" Dpy="" Fill="D02"/>
  <Colonna Cod="S§HRFI" Txt="Ora fine" Tip="" Lun="06" IO="O" Ogg="I12" Dpy="" Fill="H02"/>
  <Colonna Cod="S§HTOT" Txt="Ore residue" Tip="" Lun="06" IO="O" Ogg="NR" Dpy="" Fill=""/>
  <Colonna Cod="S§HATR" Txt="Ore attrezzaggio" Tip="" Lun="06" IO="O" Ogg="NR" Dpy="" Fill=""/>
  <Colonna Cod="SFSTOP" Txt="Stato operazione" Tip="" Lun="01" IO="O" Ogg="FLP5IRIS0F14" Dpy="" Fill=""/>
  <Colonna Cod="S§DFRI" Txt="Data fine richiesta" Tip="" Lun="08" IO="O" Ogg="D8-YYMD" Dpy="" Fill="D00R"/>
  <Colonna Cod="S§DFSC" Txt="Data fine schedulata" Tip="" Lun="08" IO="O" Ogg="D8-YYMD" Dpy="" Fill="D00S"/>
  <Colonna Cod="S1GRRI" Txt="REP-CDL" Tip="" Lun="15" IO="O" Ogg="--" Dpy="" Fill="K01"/>
  <Colonna Cod="S1CDC" Txt="Centro Costo" Tip="" Lun="10" IO="O" Ogg="CC" Dpy="" Fill=""/>
  <Colonna Cod="S1DEAR" Txt="Note" Tip="" Lun="15" IO="O" Ogg="--" Dpy="" Fill="N01"/>
 </Griglia>

### Contenuto del Gantt
In questo caso inseriamo due sole attività
> <Righe>
  <Riga Tipo="IR" Parametro="" Codice="284" Testo="" Fld="0000001|001|6000|312100580702010|ANELLO F.I|F.I.1.058|M435650||2|211|20041117|000000|20041117|000100|0,01||I|20040420|00000000|-001||Prova di inserimento di un testo di nota molto lungo per testae l'effetto dello spezzettamento su righe"/>
  <Riga Tipo="IR" Parametro="" Codice="457" Testo="" Fld="0000002|001|4200|312100850702013|ANELLO F.I|F.I.1.085|M435762||30|59|20041117|000100|20041117|000200|0,01||I|20040423|00000000|-001||Prova di inserimento di un testo di nota molto lungo per testae l'effetto dello spezzettamento su righe"/>
 </Righe>

### Gestione messaggi di errore
Se esito <> OK e livello di errore > 30 viene mostrato un messaggio di errore
> <Messaggi>
  <Messaggio Testo="Funzione ricevuta S5SER_01 OPN RICDL" Livello="00"/>
 </Messaggi>

 <Esito Stato="OK"/>

## Sezione Buttons
La sezione buttons consente di attivare o disattivare alcune delle funzionalità del Gantt
        Move = consente (1) o impedisce (0) lo spostamento delle celle.
        HorizontalMove = consente (1) o impedisce (0) lo spostamento orizzontale di una cella (moviimento nel tempo)
        GroupMove = consente (1) o impedisce (0) lo spostamento di una cella su un nuovo gruppo (cambio gruppo)
        DetailMove =  consente (1) o impedisce (0) lo spostamento di una cella su una nuova riga di dettaglio (spostamento riferito ad altra cella)
        Resize = consente (1) o impedisce (0) il ridimensionamento delle celle
        Save = abilita (1) o disabilita (0) il SAVE all'uscita dello schedulatore
        Detail = consente (1) o impedisce (0) la richiesta di visualizzazione di un dettaglio di gruppo
        Groups = Gestione visualizzazione dettaglio-somma.
                  Groups = 0 -> Attivi sia il dettaglio che il riepilogo di gruppo
                  Groups = 1 -> Attivo il solo riepilogo di gruppo (no dettaglio)
                  Groups = 2 -> Attivo il solo dettaglio (no riepilogo di gruppo)
 Groups = 3 -> Ordinamento, un solo gruppo ordinato per chiave K01
> <Buttons>
  <Button Name="Move" Status="0"/>
  <Button Name="GroupMove" Status="0"/>
  <Button Name="HorizontalMove" Status="0"/>
  <Button Name="DetailMove" Status="0"/>
  <Button Name="Resize" Status="0"/>
  <Button Name="Save" Status="0"/>
  <Button Name="Detail" Status="1"/>
  <Button Name="Groups" Status="0"/>
 </Buttons>

La sezione Setup/Program/GNT consente di impostare alcuno parametri del Gantt
        Open :  se true il Gantt si presenta con i gruppi esplosi, se false si presenta chiuso (comportamento di default)
        Title :  se true viene mostrato il pannello di header che contiene i titoli, se false non viene mostrato (default)
        MoveOnStart :  se true il gantt viene avviato già con la modalità di move attiva. Per default il move è disattivato.
        ResizeOnStart :  se true il gantt viene avviato già con la modalità di resize attiva. Per default il resize è disattivato.
        IniView :  passa il codice della vista da caricare all'avvio del gantt
        Key :  chiave identificativa dello schedulatore. Serve per il salvataggio dei setup. Se non passata viene calcolata.
        PopupMove :  se true lo spostamento di una cella da menù di popup è consentito. Per default non è consentito (false).
        EmptyGroups :  se true visualizza anche i gruppi vuoti, se false non visualizzarli (default true)
        ColumnIcons :  se true visualizza le icone sull'header delle colonne di tabella. Per default true.

        - Nodo StartTime :  individua il tempo di inizio per la visualizzazione del Gantt
        - Nodo EndTime :  individua il tempo di fine per la visualizzazione del Gantt
        - Nodo Groups :  passa la lista dei gruppi possibili, come codici separati da punto e virgola

         N.B. :  la definizione di un tempo di start e di end per la visualizzazione fissa le dimensioni della finestra di visualizzazione della parte destra del Gantt al momento dell'apertura dello stesso.

        - I nodi di tipo TimeEvent permettono di evidenziare dei termini temporali con il formato grafico di una riga verticale tracciata su tutto il Gantt nel colore selezionato.
        I campi di definizione di un TimeEvent sono : 
              - Name :  nome associato al time event. E' anche il testo visualizzato nel caso sia attiva la visualizzazione della descrizione
              - Date :  giorno del time event, nel formato YYYYMMDD
              - Hour :  istante del time event nel formato hhmmss con minuti e secondi in formato centesimale
              - Color :  colore di tracciamento della riga verticale
                                    1 per giallo
                                    2 per verde
                                    3 per blu
                                    4 per bianco
                                    5 per nero
                                    6 per ciano
                                    7 per rosso (default)
                                    8 per grigio
                                    9 per arancio
              - Label :  1 se viene mostrato il nome del time event (sulla barra della timeline), 0 se non deve essere mostrato.
       - Colors :  definisce la lista colori da associare al color manager. Ogni colore è identificato da un codice colore univoco (id), da un valore RGB che definisce il colore e da una eventuale descrizione.
       - WorkPeriod :  definisce un work period a livello globale, cioè valido per tutte le righe del gantt (linee di gruppo comprese)
         I parametri di definizione sono gli stessi del work periods definito a livello di singola riga.
> <Setup>
       <Program>
             <GNT Open="false" Title="false" ResizeOnStart="false" MoveOnStart="false" IniView="XYZ" Key="1234567890">
                  <StartTime Date="20061008" Hour="000000"/>
                 <EndTime Date="20061010" Hour="240000"/>
                <TimeEvent Name="Istante di tempo1" Date="20041117" Hour="125000" Color="1" Label="0"/>
                <TimeEvent Name="Istante di tempo2" Date="20041125" Hour="189900" Label="1"/>
                <Groups>200;300;400;800</Groups>
                <Colors>
                    <Color id="BIANCO" Desc="Mia descrizione molto lunga e annoiante">R255G255B255</Color>
                    <Color id="NERO" Desc="Altra dec">R000G000B000</Color>
   <Color id="ROSSO" Desc="">R255G000B000</Color>
   <Color id="VERDE" Desc="">R000G255B000</Color>
   <Color id="RANDOM" Desc=""/>
   <Color id="BLU" Desc="">R000G000B255</Color>
                </Colors>
               <WorkPeriod Name="Period A" IniDate="20041125" IniHour="000000" EndDate="20041126" EndHour="000000" Color="9"/>
               <WorkPeriod Name="Period B" IniDate="20041119" IniHour="000000" EndDate="20041121" EndHour="000000" Color="3"/>
           </GNT>
      </Program>
  </Setup>
</Base>


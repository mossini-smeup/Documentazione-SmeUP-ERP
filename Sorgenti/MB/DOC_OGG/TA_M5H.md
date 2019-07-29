# M5H - Modello atp
## OBIETTIVI
Descrivere le modalità con le quali viene eseguito il calcolo della data o della quantità nella funzione Avaliabe to Promise.
## SOTTOSETTORI
Non gestiti
## CONTENUTO DEI CAMPI
 :  : FLD T$M5HA __Gruppo fonti__
Contiene il gruppo fonti che guida il calcolo della disponibilità :  salvo esigenze particolari deve contenere una sola fonte di disponibilità libera.
In caso di multiplant completo, nella fonte di disponibilità libera dovrà essere impostato di non utilizzare la schiera plant contenuta nel suo gruppo fonti, ma quella ricevuta dall'analisi disponibilità.
 :  : FLD T$M5HB __Tipo distinta__
È un elemento della tabella BRL. Definisce il tipo distinta usato nell'esplosione dei componenti. Se non impostato si assume il tipo distinta 'ART'.
 :  : FLD T$M5HC __Data partenza__
Se impostato, è la data di partenza dell'Atp.
Se non impostato si assume 'domani'.
Va preferibilmente impostata una data definita in modo implicito (tramite / :  ad esempio oggi + 3 giorni..), in modo da non dover modificare continuamente questa tabella.
 :  : FLD T$M5HD __Appiattimento al più tardi__
Inizialmente gli impegni vengono datati al più presto.
Se questo campo è impostato, gli impegni posti sui rami non appartenenti al percorso critico verranno spostati al più tardi, con la data finale allineata al componente critico. In questo modo si potrà recuperare l'eventuale disponibilità libera che trovano lungo questo avanzamento.
>
_9_Esempio : 
La situazione degl impegni ATP nel tempo è la seguente : 
>.===A===|
.==B==...|
.===C====|
.=====D====|
.=E===.....|

Il tratteggio '==x==' è il tempo di approvvigionamento del codice x.
Il tratteggio '...' è lo slittamento ammesso.
Il percorso critico è A/C/D.

Se è stato impostato l'appiattimento al più tardi, la situazione diventa : 
>.                   ===A===|
.             ==B==|
.          ===C====|
.=====D====|
.     =E===|

I componenti non critici B ed E vengono allineati rispettivamente a C e a D.
 :  : FLD T$M5HE __Arrotondamento al lotto__
Se impostato, gli impegni vengono arrotondati al lotto (minimo/multiplo), e viene memorizzata, nell'archivio degli impegni provvisori, l'eccedenza (quantità arrotondata al lotto - quantità originale).
Essa può essere vista, nella scansione di disponibilità, come fonte futura positiva, ed usata dalle analisi ATP, fino alla successiva pianificazione.
Se è presente il lotto massimo e la politica dell'articolo prevede il trattamento del lotto massimo '2', (suddivisone in parallelo), quando la quantità da pianificare è superiore al lotto massimo nella determinazione della data di fine ordine, si considera il lotto massimo al posto della quantità da pianificare.
 :  : FLD T$M5HF __Tipo ciclo di carico__
È un elemento della tabella BRT. Se non è impostato vuol dire che non si intende tener conto del carico nell'analisi ATP.
Se impostato, definisce il tipo ciclo che viene scandito per acquisire il componente di carico.
 :  : FLD T$M5HG __Tipo capacità__
Il tipo capacità definisce la modalità di acquisizione della capacità. Può assumere i seguenti valori : 
 '1'  vista MPS.
  ...
 :  : FLD T$M5HH __Parametro capacità__
Il parametro è in funzione del tipo.
Se vista MPS è così composto : 
>Pos.1/6 :  Codice piano (obbligatorio).
>Pos.7 :  Se impostato considera il piano con codice più alto con radice uguale al codice impostato, se lasciato in bianco considerare solo il piano impostato.
>Pos.8/10 :  Codice vista.
>Pos.11 :  I/F se assegnare il carico al periodo in cui cade l'inizio o la fine dell'impegno.
 :  : FLD T$M5HI __Tipo azione sovracapacità__
Il tipo azione sovracapacità definisce l'azione da intraprendere in caso di sovracapacità.
Può assumere i valori : 
 '1'  slittamento utente.
  ...
 :  : FLD T$M5HJ __Parametro azione sovracapacità__
Il parametro è in funzione del tipo.
Se lo slittamento utente è così composto : 
>Pos.1 :  Suffisso del pgm M5M5hc_x che muove date di inizio e fine.
>Pos.2/6 :  parametri di condizionamento specifici del programma.
 :  : FLD T$M5HT __Trattamento scarti__
È un valore V2/DBSCA :  definisce la modalità del trattamento degli scarti nell'esplosione della distinta base.
 :  : FLD T$M5HU __Arrotondamento da unità di misura__
È un valore V2/SI/NO :  se impostato, la quantità dei componenti verrà arrotontata secondo quanto definito nella tabella della sua unità di misura.
 :  : FLD T$M5HV __Atp logistico__
Se impostato, (e se si è impostata, in M51 la pianificazione per ente, altrimenti viene forzato a blanks) si assume che l'atp abbia lo stesso comportamento logistico della pianificazione.
Questo carattere rappresenta il suffisso 'x' del programma M5M5H0_x, che viene lanciato all'atto della scrittura dell'assieme di partenza :  questo programma ritorna, in modo specifico per l'applicazione, il destino dell'asseime (che verrà riportato nell'assieme di riferimento).
Ad ogni livello si determina poi l'ente preferenziale dell'articolo (è l'esecutore, che viene riportato nell'oggetto di riferimento).
L'esecutore diventa il destino dei componenti (che viene riportato nell'assieme di riferimento).
Si costituisce in questo modo, in ogni riga di Atp, la catena logistica esecutore / destino, nei campi oggetto e assieme di riferimento.
 :  : FLD T$M5HW __Disponibilità per ente__
È un valore V2/SI/NO. È significativo in presenza di atp logistico. Se impostato, la scansione per determinare la disponibilità libera viene eseguita per l'ente destino della riga di atp che si sta trattando.
 :  : FLD T$M5HK __Data minima__
Se impostata, è la data minima alla quale viene ritornato l'atp :  se la data, dopo l'analisi dei materiali, è al di sotto di essa, viene portata a questo valore (con appiattimento dei livelli inferiori). Viene poi eseguita, se richiesta, l'analisi delle capacità, la quale potrebbe far avanzare ulteriormente la data atp.
Si consiglia di impostare questa data in modo implicito.
 :  : FLD T$M5HL __Data massima__
Se impostata, è la data massima alla quale viene ritornato l'atp :  se nell'analisi delle capacità, essa viene superata, si fissa  l'assieme a questa data, e lì si impostano i carichi (a tutti i livelli), che genereranno un sovraccarico.
Si consiglia di impostare questa data in modo implicito.
 :  : FLD T$M5HM __Suffisso programma filtro date__
Se impostato, le finestre di data minima e massima sono ritornate da un programma utente 'M5M5HF_x', dove x è il valore qui impostato. Ad esempio, è possibile far dipendere questa finestra dall'articolo di cui si calcola l'atp. La finestra della tabella è sempre il default, in mancanza di queste date.
 :  : FLD T$M5HS __Suffisso programma aggiustamento date__
Se impostato, nella determinazione delle date viene eseguito il programma utente 'M5M5HD_x', dove x è il valore qui impostato.
La correzione può essere eseguita, ad esempio, per tener conto di date 'fisse' di consegna del fornitore.
 :  : FLD T$M5HN __Parametri pianificazione per riferimento__
È un valore V2/SI/NO :  se impostato, ed in tabella M51 è impostato che i parametri di pianificazione siano per riferimento (ed il riferimento è l'ente, in caso contrario viene forzato a NO), i dati di pianificazione stessi (i tempi di approvvigionamento ed eventualmente i lotti minimi e multipli), saranno assunti dall'ente preferenziale.
 :  : FLD T$M5HO __Arrotondamento giorni lavorativi__
Se impostato, le date minima e massima verranno arrotondate al primo giorno lavorativo (rispettivamente maggiore o uguale e minore o uguale). Il calendario sarà quello definito dalla risorsa impostata nel primo magazzino del gruppo fonti per l'analisi disponibilità.
Questo campo non influisce sul calcolo dei tempi di approvvigionamento (in gg lavorativi o solari) nel piazzamento delle date ATP, che è guidato da quanto impostato nella tabella generale della pianificazione (M51) per gli ordini di produzone, di acquisto, e di lavorazione esterna.
 :  : FLD T$M5HP __Modo trattamento pronto__
Se lasciato in bianco, e se l'atp è coperto totalmente dalla giacenza, viene ritornata la data odierna avanzata alla data minima (se impostata).
Se impostato, definisce la data alla quale viene ritornato l'atp, se esso è coperto totalmente.
Esso può assumere i seguenti valori : 
_7_'1' :  Se l'atp è coperto totalmente dalla giacenza viene ritornata la data odierna avanzata del tempo di rettifica dell'articolo. Se è invece coperto da fonti future, viene portato alla data inizio finestra.
_7_'2' :  Se l'atp è coperto totalmente dalla giacenza si comporta come nel caso '1'. Se invece è coperto da fonti future mantiene la data dell'atp, controllando che non sia inferiore alla data odierna avanzata, del tempo di rettifica dell'articolo, nel qual caso assume quest'ultima data.
Qualora si passa una data dall'esterno, essa sostituisce quella calcolata se maggiore di essa.
 :  : FLD T$M5HQ __Tipo/risorsa calendario commerciale__
Se si definisce il tipo e la risorsa, viene considerato nell'avanzamento delle date il suo calendario.
 :  : FLD T$M5HR.T$M5HQ
 :  : FLD T$M5HZ __ATP per configurazione__
Se impostato questo campo, verrà trattata, nel calcolo dell'ATP la configurazione ricevuta (impostata a video in simulazione, oppure presente nella riga documento in datazione documenti id ciclo esterno).
Non si può scegliere contemporaneamente l'ATP logistico e l'ATP per configurazione.
Non è inoltre necessario (anche se opportuno) che l'MRP abbia come oggetto di rottura la configurazione.
Trattare la configurazione nell'ATP significa due cose : 
1. Esplodere la distinta base con la configurazione.
2. Calcolare la disponibilità libera con la configurazione. Non è possibile, a differenza dell'ATP logistico, scegliere se considerare o meno l'oggetto di rottura nel calcolo della disponibilità (tramite il campo disponibilità  per ente).
Questo per la natura diversa delle due rotture :  nell'ATP logistico si tratta lo stesso oggetto in luoghi diversi (e quindi è legittimo scegliere se considerare o meno questa suddivisione), mentre nell'ATP per configurazione si trattano oggetti diversi, quindi non ha senso considerarli come se fossero indistinguibili.
Questo campo può assumenre i seguenti valori : 
_7_' ' :  non viene trattata la configurazione.
_7_'1' :  la configurazione ricevuta viene trattata sull'assieme ma non viene trascinata sui componenti.
_7_'x' :  la configurazione viene trascinata sui componenti. In questo caso verosimilmente c'è la necessità di ridurla.
Viene eseguito, per ogni legame, il programma M5M5HK_x (dove x è il suffisso impostato in questo campo) in cui si implementa l'algoritmo di riduzione della configurazione.
 :  : FLD T$M5H1 __Solo livello__
Se impostato questo campo, verrà considerato l'ATP solo al livello dell'articolo per cui è stato richiesto. In asenza di copertura, si avanzerà del suo tempo di approvvigionamento.
 :  : FLD T$M5H2 __Multiplant__
Va impostato in presenza di MRP multpilant completo. In tal caso l'ATP suggerirà, in presenza di politiche di trasferimento, ordini di trasferimento dal plant di competenza a quello di fabbisogno.
 :  : FLD T$M5H3 __Calcolo criticità__
Se impostato l'appiattimento al piu' tardi determina i componenti "rami" critici, e calcola i giorni di distanza dalla criticità.

# GM1 - Parametri gestione magazzini
## OBIETTIVO
Impostare i parametri che guidano la gestione di magazzino.
## CONTENUTO DEI CAMPI
 :  : FLD T$GM1N __Numeratore movimenti__
È un elemento della tabella CRNGM.
È il numeratore dei movimenti di magazzino e costituisce la chiave univoca di questo archivio.
Deve essere definito numerico di 9 posizioni.
 :  : FLD T$GM1C __Numeratore colli__
È un elemento della tabella CRNGM.
È il numeratore dei colli e costituisce la chiave univoca di questo archivio.
Può essere definito liberamente (numerico o alfanumerico) fino ad un massimo di 15 posizioni.
 :  : FLD T$GM1A __Area magazzini__
È un elemento della tabella IGA.
È utilizzato nella chiusura di magazzino; è l'area dell'archivio degli indici riservato a tale chiusura.
 :  : FLD T$GM1T __Tema magazzini__
È un elemento della tabella IGT.
È utilizzato nella chiusura di magazzino; è il tema dell'archivio degli indici riservato a tale chiusura.
 :  : FLD T$GM1S __Sintesi di magazz.__
È un elemento della tabella IGS.
È utilizzato nella chiusura di magazzino; è la sintesi di magazzino dell'archivio degli indici, riservato a tale chiusura.
 :  : FLD T$GM1B __Tipo costo assunto__
È un elemento della tabella TCO.
È il tipo costo assunto utilizzato nelle valorizzazioni di magazzino.
 :  : FLD T$GM1L __Livello di costo__
È il livello da utilizzare nelle valorizzazioni di magazzino. Per il significato dei valori inserisci '?'
 :  : FLD T$GM1D __Numeratore identificativo riga di movimentazione__
È un elemento della tabella CRN.
È il numeratore  dell'identificativo delle righe delle richieste di movimentazione e costituisce la chiave univoca di questo archivio.
Deve essere definito numerico di 9 posizioni.
 :  : FLD T$GM1E __Passo numero righe__
Definisce il passo con cui viene assegnata la numerazione alle righe delle richieste di movimentazione. Se non assunto, si assume 1.
Questo campo è significativo nel caso in cui il documento di movimentazione sia strutturato in testata e righe :  il passo definisce il numero di riga nell'ambito di una stessa testata.
Non va confuso con il campo precedente, che definisce l'identificativo univoco della riga. Il numero di riga potrà essere duplicato, nel caso in cui una riga di richiesta di movimentazione, all'atto dell'allocazione o dell'impegno, si suddivida (ad esempio in più ubicazioni).
 :  : FLD T$GM1F __Modalità gestione contenitori__

 :  : FLD T$GM1G __Programma di calcolo numero collo__
Definisce il nome dell'eventuale programma di calcolo del numero collo di una spedizione. Nel caso non sia specificato, verrà utilizzato il calcolo standard che utilizza il numeratore presente in questa tabella. (Programma esempio GMGMQ1_XX).
 :  : FLD T$GM1H __Calcolo peso automatico colli__
È un elemento V2 SI/NO. Se impostato a "SI", quando crea un collo in gestione delle spedizioni, aggiorna in automatico il peso del collo durante l'operazione di confezionamento. (_9_Esempio :  se si sta confezionando articoli, legge il peso in anagrafica e lo somma al peso complessivo del collo). Il peso lordo viene calcolato sommando il peso dei vari componenti del collo + una componente di tara dell'unità di movimentazione (tab GMB) presente nel tipo collo.
 :  : FLD T$GM1I __Metodo di rintracciabilità__
Definisce quale informazione del movimento di magazzino viene utilizzata per legare il componente prelevato all'assieme, in cui
è utilizzato ai fini della rintracciabilità. Se abbiamo uno scarico automatico senza ordine, potrebbe essere il numero di documento, in altri casi potrebbe essere il numero ordine su cui vengono eseguiti prelievi e versamenti.
 :  : FLD T$GM1J __Gestione lotti da classe funzionale__
È un elemento V2 SI/NO. Se lasciato a blanks, gli articoli che non hanno classe funzionale si intendono movimentati con il codice lotto; se impostato, si intendono non gestiti a lotti. Se la classe funzionale è impostata, è da essa che si assume l'informazione della movimentazione o meno dell'articolo con il codice lotto.
 :  : FLD T$GM1K __Suffisso programma costruzione metodo GMY__
Definisce l'eventuale programma che deve essere richiamato dal programma di valorizzazione delle giacenze (o di una foto), al fine di reperire nel modo corretto la tabella GMY che definisce i criteri di valorizzazione degli inventari.
In generale, il condizionamento della valorizzazione dipende dal "cosa" (articolo) e dal "dove" (area/tipo giacenza, magazzino, fornitore, ecc.). Il programma implementa tali logiche.
_9_Esempio :  se si vuole che le giacenze in conto deposito siano diverse per fornitore, si costruirà la tabella unendo area e codice fornitore; il programma la cercherà, in questo modo, per quella particolare area ecc.
In questo campo si definisce il suffisso del nome del programma GMFO01E_x (dove x è il suffisso).
 :  : FLD T$GM1M __Richiamo pgm specifico GMC in estrazione Foto giacenze__
È un elemento V2 SI/NO. Se impostato a "SI", durante l'esecuzione del programma di estrazione della Foto delle giacenze, nel passo di ricostruzione giacenza fissata "alla data", ad ogni ri-applicazione di movimento di magazzino letto dallo storico (se presente), viene richiamato il "programma specifico" definito nell'elemento di tabella GMC relativo.
La rilevanza del richiamo è data dalla funzione espletata dal "programma specifico", se interna ai soli movimenti e giacenze di magazzino, o se estesa ad altre aree applicative (quindi da non rieseguire ad ogni estrazione di Foto).
 :  : FLD T$GM1O __Scenari in valorizzazione fiscale__
È un elemento V2 SI/NO. Se impostato, vengono attivati diversi ambienti di valorizzazione fiscale (sui diversi scenari) :  in questo caso, prima dell'esecuzione di ogni funzione riguardante la valorizzazione, viene richiesto lo scenario.
Gli scenari vengono impostati nella tabella GM3 e lo scenario assunto è '**'.
Va ricordato che non è necessaria la presenza dello scenario assunto :  in mancanza, si considera che siano vuoti tutti i suoi campi.
Nello scenario vengono impostate le modalità della valorizzazione. In particolare viene fissato l'oggetto intestatario della valorizzazione, e se non presente o non presente alcun scenario (quindi assunto '**') l'oggetto intestatario sarà 'AR' (articolo).
 :  : FLD T$GM1Q __Revis. mov. a storno__
È un elemento V2 SI/NO. Definisce se la modalità generale di revisione dei movimenti di magazzino è di tipo "con movimento di storno", oppure diretta sul movimento di magazzino interessato.
Ha rilevanza in caso di "Scollegamento documenti" oppure "Revisione movimenti di magazzino". Nel caso di impostazione per "storno", assume i seguenti comportamenti : 
-    in caso di cancellazione, viene scritto un movimento di "storno" identico all'originale ma con quantità moltiplicata per -1.
-    in caso di revisione, viene scritto un movimento identico di storno, come nel caso della cancellazione e, quindi, scritto il movimento nuovo dopo la correzione.
 :  : FLD T$GM1R __Tipo evento segnalazione negativi__
È un elemento della tabella P5D.
Se impostato, ogni qualvolta la giacenza di un articolo viene modificata con un movimento di magazzino e va in negativo, viene generata una segnalazione nell'archivio eventi, con il tipo evento qui impostato (con causale e categoria evento assunte dai corrispondenti valori di default del tipo evento).
L'evento riporta le seguenti informazioni : 
-    N.registrazione di magazzino che ha provocato il negativo.
-    Estremi del record di giacenza che va in negativo : 
.    Magazzino.
.    Articolo.
.    Area.
.    Tipo Giacenza.
.    Chiavi 1/5 del tipo giacenza.
La segnalazione del negativo viene generata indipendentemente dal fatto che prima del movimento la giacenza fosse già negativa o meno.
_9_Esempio : 

 :  : PAR F(01) L(TAB)
- Giacenza prima|Movimento|Giacenza dopo
- 10|-12|-2
- 10|-3|-13
- 10|+3|-7


In tutti questi casi viene data segnalazione del negativo, anche se solo nel primo caso il movimento provoca l'insorgenza del negativo. Nel secondo caso la situazione viene peggiorata, nel terzo viene migliorata ma non in modo sufficiente.
 :  : FLD T$GM1U __Segnalazione presenza di transazioni errate in GMTRAN__
È un elemento V2 SI/NO. Definisce se si desidera avere una segnalazione circa la presenza di transazioni errate nel file GMTRAN, ogni volta che si avvia il programma di interrogazione delle giacenze.
 :  : FLD T$GM1V __Gestione quantità collegate__
Se impostato, in stampe e interrogazioni dell'archivio giacenze, vengono rappresentate le giacenze alternative di un articolo. Se valorizzato a "1" la funzione si ottiene su richiesta, se impostato a "2" il sistema assume sempre questo comportamento
 :  : FLD T$GM1Z __Contr.Inserim. GMC__
Se impostato (valore 1), si attiva il controllo in fase di inserimento delle causali di magazzino, tabella GMC, della codifica della causale stessa. La causale dovrà essere composta nella forma XXYY dove : 
XX=Area di magazzino.
YY=Causale della transazione (deve essere un elemento della tabella GM*CM).
Inoltre, è possibile inserire causali "neutre" (che non utilizzano nessuna area, quindi di tipo statistico) inserendo la sigla fissa 'ST' al posto dell'area. In questo caso l'inserimento di YY è libero.
 :  : FLD T$GM1X __Gest.risalite(+=ges)__
In questo campo è possibile cambiare la modalità di risalita di alcuni dati magazzino/articolo.
Se un dato ha la modalità impostata, la risalita non si ferma al primo record valido trovato, ma al primo record con quel dato compilato.
È possibile specificare in modo diverso il comportamento dei singoli campi.
I valori che è possibile mettere in ognuno dei 5 caratteri a disposizione sono : 
1 :  Tecnica di gestione.
2 :  Ubicazione assunta.
3 :  Famiglia contenitori + Quantità per contenitore.
4 :  Scorta minima.
5 :  Punto di riordino + Lotto economico.
Se, per esempio, si vuole avere un'ubicazione assunta gestita per classe articolo e la scorta minima gestita per singolo articolo, bisogna scrivere in uno dei 5 caratteri del campo il valore '2'. Scrivendo anche il valore '4', nel caso in cui sia presente un record per singolo articolo (che però non avesse compilato il campo della scorta minima), verrebbe eseguita una lettura della prima scorta minima presente negli altri livelli di risalita (per esempio della classe articolo).
Digitando un + nel primo carattere del campo, si apre una videata che aiuta nell'inserimento delle singole risalite.
 :  : FLD T$GM1$ __Aggiustamento GMA__
Programma di aggiustamento dati magazzino/articolo.
Se impostato, la routine £GMA richiamerà al termine della sua esecuzione il programma GMGMA0_x, che potrà modificare i valori restituiti nella DS £GMADS
 :  : FLD T$GM1W __Gruppo azioni di movimentazione magazzino__
Se impostato, permette il trasferimento materiale direttamente dall'interrogazione giacenza a parità di area e tipo, ove previsto ed autorizzato.
 :  : FLD T$GM1Y __Suff.Parz.Lista__
Il campo rappresenta il suffisso del programma GMMO01L_x  (dove x = al contenuto del campo della tabella).
Valorizzando il campo si abilita il lancio del programma in oggetto che consente di effettuare parzializzazioni
specifiche nella lista dei movimenti di magazzino (GMMO01L)
 :  : FLD T1GM1A __Suff.Exit Movimenti)__
Se impostato, viene lanciata la exit GMTRGEN_x (dove x è questo suffisso) subito dopo la exit
specifica impostata a livello di causale.
La presente exit non viene eseguita se ha lo stesso nome di quella definita nella causale.
Ricordiamo che a livello di causale si imposta l'intero nome della exit, e non il solo suffisso,
quindi l'omonimia è possibile, anche se improbabile.
E' inoltre possibile impostare, nella exit a livello di causale, che non venga lanciata la exit
generale.
 :  : FLD T1GM1B   Exit generale controlli visualizzatore movimenti
Il campo definisce il suffisso del programma GMMV01D_x. Se attivato e presente viene richiamato
come exit generale per i controlli su tutti i visualizzatori dei movimenti di magazzino.
In questa exit è possibile inserire i controlli comuni a tutti i visualizzatori.
Riferirsi al prototipo della exit GMMV01D_X presente in GMSRC, per l'implementazione e la
relativa documentazione.

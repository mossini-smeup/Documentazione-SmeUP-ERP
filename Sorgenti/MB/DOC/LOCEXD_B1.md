## Gestione della 'Copertina' delle sezioni (elemento Cover)
Se nella label di una matrice e' presente un simbolo rosso significa che per il report di quella matrice e' stata definita una copertina stndard che e' possibile vedere cliccando due volte sul simbolo rosso : 
![03COMEXD04](http://localhost:3000/immagini/LOCEXD_B1/03COMEXD04.png)Aprendo l'XML della matrice vedo l'elemento Cover che mi definisce la struttura della copertina : 
![LOCEXD_035](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_035.png)La definizione della struttura della copertina e' passata negli input o in alternativa e' presa dal servizio (LOA15_SE) -> se negli input gli passo un Img(NomeImmagine) usa quell'immagine come sfondo, se non passo nulla usa [SFO.001]. Il logo glielo passo sempre negli input come Log(NomeLogo) oppure usa [LGO.001]. Il T01 lo legge negli input come T01(TitoloPrincipale) se non lo metto va su (SPAR(11) idem con T02 e T03 (vanno su (SPAR(12) e (SPAR(13)). Il titolo 4 invece viene visualizzato solo se passato.

## Variabili statiche
### Nuova gestione variabili di Looc.Up (condivise Java/Delphi / AS400 se __)
Se gli passo nel WAIT(__NomeVariabile) lui sa che deve memorizzare la variabile anche in AS (record del B£MEDE0F scritto tramite £G00); inoltre può essere utilizzata all'interno di un servizio RPG, in quanto viene ritornata nella variabile £UIAD1. Riguardo a cio' sono presenti degli esempi in MyLoocUp -> Per lo sviluppatore -> Esempi -> Capire LoocUp -> Funzioni con interazione -> 01.FIN.F Funzioni con W.

### Gestione variabili 'Array' nella scheda (in particolare per Drag&Drop)
E' possibile passare stringhe di variabili concatenate; ad esempio e' possibile effettuare una selezione multiple e droppare gli elementi selezionati in un'altra sezione :  in questo caso viene passata una variabile che in realta' e' l'elenco di piu' istanze separate da un ;  : 
![03COMEXD10](http://localhost:3000/immagini/LOCEXD_B1/03COMEXD10.png)In caso di selezione multipla su una matrice, vengono create delle variabili di Sezione nominate FROM.NomeColonnaMatrice. In caso di albero la logica e' la stessa di quella appena esposta; l'unica differenza e' che nell'albero, non essendoci i nomi colonne come nella matrice, le variabili di sezione si chiamano FROM.SELECTED.T1, FROM : SELECTED.P1, FROM.SELECTED.K1. Esempio 1 :  Abbiamo una matrice contenente una lista di Fornitori (CNFOR) e ne selezioniamo 3 : 
Le colonne
![LOCEXD_043](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_043.png)Le colonne della matrice si chiamano : ID_TP per il tipo (colonna nascosta), ID_OG per il codice e ID_DE per la descrizione. Nell'immagine sotto in evidenza le variabili che ci interessano : 
![LOCEXD_044](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_044.png)Esempio 2 :  Abbiamo un albero contenente una lista di Collaboratori (CNCOL) e ne selezioniamo 5
![LOCEXD_045](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_045.png)Il contenuto delle variabili sara' : 
![LOCEXD_046](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_046.png)
## Implementazioni
### Nuove notifiche NOTIFY (SUB, SCHEDA, FIRSTSCHEDA, SELF)
E' un campo inserito nel wizard della funzione : 
![03COMEXD06](http://localhost:3000/immagini/LOCEXD_B1/03COMEXD06.png)Notifica della fine di una funzione; il controllo ritorna al chiamante e, piu' precisamente, alla sezione o alle sezioni indicate tra ( ) dopo il NOTIFY. Tra parentesi possono esserci anche piu' sezioni, nel caso devono essere separate da '\'

*SUB ritorna alla SUBSEZIONE su cui c'e' il focus e la aggiorna :  ad esempio in questo caso e' stato aggiunto il notify su un drop : 
G.DIN When="Drop" Exec="F(FBK;B£SER_25;DED.DEE) 1(TA;B£U;&AM.UT) 2(;;&PA.NomCar) NOTIFY(*SUB) INPUT(TPaOgg([FROM.TIPOGG]) CodOgg([FROM.CODOGG]))" In pratica il dinamismo fa in modo che quando droppo sulla subsezione A gli elementi droppati vengano cancellati dalla subsezione B di partenza. Se non mettessi il notify quando dropperei sulla subsezione A non avrei l'aggiornamento della subsezione B di (su cui è il fuoco) e quindi non capirei quali elementi sono gia' stati eliminati e quali no.
*SCHEDA ritorna alla scheda o sottoscheda che contiene la subsezione che ha il focus e la aggiorna
*FIRSTSCHEDA ritorna alla scheda principale/contenitore/1° livello
*SELF ritorna alla sezione da cui e' stata lanciata la funzione e la aggiorna
*YES ritorna a tutta la finestra

### Funzioni virtuali EXEC (CLOSE, REFRESH, EXECUTE, EXIT, DINAMIC) Esempi
In ogni posto dove posso definire il richiamo di una funzione, posso inserire una delle parole chiave sopra per indicare che alla fine dell'esecuzione della funzione, va eseguito anche : 

Close  :  chiude scheda
Refresh  :  esegue il refresh della scheda
Exit  :  chiude LOOCUP
Dinamic  :  esegue un dinamismo sulla sottosezione di partenza

![LOCEXD_036](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_036.png)
## Funzioni W
Sono tutte le funzioni del J1_STR. In pratica viene chiamata una funzione che risponde qualcosa. Per testarle vedere J1/STR_SIMG30, facendo F4 nel campo del codice oggetto e poi di nuovo F4 mi si apre questa : 
![03COMEXD08](http://localhost:3000/immagini/LOCEXD_B1/03COMEXD08.png)Ad esempio facendo F4 due volte nel J1 STR_EDT viene chiamato un editor, scrivendo nell'editor e poi facendo F12 viene restituito in stringa quello che e' stato scritto nell'editor. Oppure facendo F4 sul J1 STR_SIMTRE mi viene prima visualizzata una schermata come questa : 
![LOCEXD_037](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_037.png)Facendo nuovamente F4 viene visualizzato l'albero delle applicazioni in cui e' possibile effettuare una selezione (anche multipla). Le applicazioni selezionate mi verranno elencate in questa finestra bianca : 
![LOCEXD_038](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_038.png)![LOCEXD_039](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_039.png)E da qui riportate nel campo J1 STR_SIMTRE : 
![LOCEXD_040](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_040.png)L'attesa di una risposta viene pilotata dal campo Wait della funzione :  se lo compilo con VAR(NomeVariabile) la variabile al momento della conferma F6 viene valorizzata con l'XML ritornato dalla funzione richiamata; questa variabile e' accessibile solo da LOOCUP (Delphi/Java). Ad esempio nella chiamata dell'albero la funzione e' : 
![LOCEXD_041](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_041.png)In questo caso il risultato dell'XML e' : 
![LOCEXD_042](http://localhost:3000/immagini/LOCEXD_B1/LOCEXD_042.png)
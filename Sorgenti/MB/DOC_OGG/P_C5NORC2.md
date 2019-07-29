Lanciando questa funzione, all'utente viene presentata una schermata splittata in due sezioni verticali :  nella sezione di sinistra vengono presentati i movimenti risultanti dalla contabilità, nella sezione di destra i movimenti risultanti dal flusso ricevuto dalla banca. Da questa schermata l'utente può andare manualmente ad associare i movimenti banca con quelli contabili con gli stessi effetti della spunta automatica.
Le principali opzioni disponibili sono quelle riportate  seguito; tutte le opzioni (da inserire nello spazio bianco a sinistra di ogni movimento e visualizzabili con il '?' nel medesimo campo) sono costituite da due caratteri, ma per la maggior parte di esse il secondo serve solo ad indicare se l'opzione debba avere effetto sulla sezione dei movimenti contabili (carattere "T") o sulla sezione dei movimenti banca (carattere "B"); per queste viene riportato solo il primo carattere : 
- 1  = seleziona movimento per spunta (che verrà effettuata solo quando viene premuto il comando F06)
- D  = deseleziona movimento (se già selezionato)
- F  = forza la spunta di un movimento di una sezione senza che vi sia corrispodenza nell'altra
- A  = annulla la spunta (di un movimento per il quale la spunta è già stata confermata)
- 11 = lancia la creazione interattiva di una registrazione contabile, che si presenterà con il riporto automatico delle informazioni presenti sul movimenti banca su cui viene fatta questa opzione. Se la registrazione viene confermata automaticamente vengono spuntati la registrazione creata ed il movimento banca correlato (spiegata dettagliatamente inseguito).
- AN = Permette di annullare il movimento ricevuto dalla banca. I movimenti annullati verranno esclusi da tutte le operazioni di conciliazione. Un volta annullati possono essere visualizzati tramite l'F17.
- RI = Permette di ripristinare un movimento annullato.

Se una riga viene presentata con le date sottilineata, è per indicazione del fatto che quella riga ha come contropartite altre righe banca che sono in uno stato di conciliazione differente.

Tramite F17 si va invece nelle impostazioni :  ad esempio se le date sono discordanti con Ripresa date si va a riprendere la data valuta della banca; con Ripresa note, riprende anche la descrizione di quello che passa la banca (è identico a scrivere VB nello spazio bianco di ogni singola spunta nella schermata generale delle riconciliazioni); mentre in Movimenti si può scegliere quali filtrare (spuntati, tutti,da annullare, da spuntare).
Nel caso tra gli elementi contabili non si trovi il corrispettivo dell'elemento bancario, allora si procede alla creazione di una registrazione contabile (per abbinare a una causale ABI una casuale contabile propria).
Scrivere 11 nel campo bianco dell'elemento banca interessato e nella successiva schermata (come da figura) selezionare il tipo di registrazione (a seconda della scelta potrebbe compilare in automatico gli spazi vuoti sottostanti o dover compilare gli eventuali obbligatori).

![C5D030_035](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORC2/C5D030_035.png)
A questo punto si possono verificare due possibili scenari; nel primo occorre , attraverso il '?' nello spazio bianco sulla colonna conto, selezionare dal menu l'elemento da associare in modo da azzerare il residuo, e poi confermare con F6.

![C5D030_036](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORC2/C5D030_036.png)
Come seconda possibilità può avvenire che, ad esempio selezionando la registrazione relativa agli incassi clienti o pagamento RID, il rimando sia a una schermata più specifica come quella sotto riportata.

![C5D030_037](http://localhost:3000/immagini/MBDOC_OGG-P_C5NORC2/C5D030_037.png)
Con riferimento all'esempio si scrive S.P.A. in ragione sociale (nella descrizione dà S.P.A., che uso come filtro perricercare le papabili associazioni)
Metto il ? a fianco della riga che voglio selezionare (si possono selezionare anche più righe se necessario) :  selezionare 'Salda Rata' se i singoli importi non corrispondono con il residuo, 'R' se l'importo coincide o se si vuole forzare a zero un'eventuale differenza che crea squilibrio nel residuo (in questo occorre mettere 1 sotto la colonna A a fianco del residuo che si vede nell'ultima colonna);il residuo può essere anche assegnato manualmente senza forzarlo proseguendo con un doppio F06,secondo regole simili a quelle descritte nel primo scenario.

Impostando tramite gli elementi della C5U con codifica RBAN + Causale ABI è inoltre possibile far si che venga proposta una causale e/o un conto (attenzione che entrambi fanno scattare nella conciliazione automaticha la creazione della registrazione in modo automatico).
Nel codice della C5U è inoltre possibile aggiungere anche il segno dare/avere per differenziare causale/conto a seconda non solo della causale ma anche del segno.

 :  : DEC T(TA) P(C5U&AZ) K(RBAN[TA.V§O]) I(**Registrazioni automatiche da Corporate >>)
 :  : DEC T(TA) P(C5U&AZ) K(RBAN[TA.V§O]D) I(**Registrazioni automatiche da Corporate solo Dare >>)
 :  : DEC T(TA) P(C5U&AZ) K(RBAN[TA.V§O]A) I(**Registrazioni automatiche da Corporate solo Avere >>)

#
#
# GESTIONE NOTE STRUTTURATE
# OBIETTIVO
L'obiettivo che si pone questo programma è quello di gestire in modo dinamico e flessibile le condizioni di creazione delle note strutturate. Dati una serie di parametri definiti nel programma è possibile controllare le incongruenze tra questi parametri e i dati nelle tabelle.
1.1.0.0.0.0.1 NOTE OPERATIVE
Per poter accedere a queste informazioni è necessario mettere l'opzione '/' nel campo dedicato alla gestione delle Note Strutturate, così facendo si apre una finestra in cui appaiono una serie di informazioni che specificano  : 
- in che modo si stanno gestendo i dati  (interrogazione / visualizzazione / immissione)
- i vincoli che sono stati impostati al momento della creazione del programma; quindi se il vincolo corrisponde ad 1 quando si interroga la tabella con il ! o il ? vengono visualizzate solo le opzioni relative alle Note Strutturate, con 2 quelle riguardanti le Liste di Distribuzione e con il codice 3 solo quelle relative alle Informazioni.
Se il campo non ha valori si assume che non esistono vincoli
- il campo ORIGINE indica se il contenitore delle note strutturate (elemento della tabella NSC) è definito nel programma o è specificato in una tabella.
Se è specificato in una tabella a video si libera il campo di interrogazione della tabella in questione
- il campo CONTENITORE specifica a quale elemento della tabella NSC si riferiscono le note dell'applicazione
- i PARAMETRI di TABELLA e di PROGRAMMA specificano di che tipo sono le tre chiavi per accedere alle note. Se l'applicazione riscontra delle incongruenze tra questi campi è possibile entrare in modifica della tabella NSC e cambiare i valori
'Codice' e 'Parametro Codice'
I campi ORIGINE e CONTENITORE se dipendono da una tabella possono essere gestiti. Per visualizzare le informazioni relative alle tabelle è possibile interrogare il campo  usando le opzioni che sono associate alla tabella in questione, se si vogliono conoscere le opzioni associate ad una tabella si deve interrogare il campo con un ! o ? o /.
Il programma B£NST1 gestisce anche l'interrogazione della tabella
B£R costruendo in modo mirato una schiera di opzioni valide per la gestione delle note.
Quindi se si sta usando la funzione di interrogazione per un qualsiasi documento la lista delle opzioni valide per la gestione delle Note Strutturate sarà relativa alle sole opzioni di interrogazione, ad esempio :  VC, IC, SC, IL, ecc....
# NOTE TECNICHE
## Descrizione campi : 
A livello di specifiche di programma per attivare la funzione di gestione dell'ambiente delle Note Strutt. è necessario che il campo £NSTMT (modalità richiamo programma) venga gestito, i valori che può assumere sono 01 - 02 - 05 oppure può assumere quelli che si ricevono dalle autorizzazione, quindi 11, 12, 15.
Se tale campo non è utilizzato nel programma resta la vecchia gestione delle note strutturate.
Gli altri parametri da definire nella routine iniziale sono  : 
- £NSTTC      :  è l'elemento della tabella NSC che specifica a quale contenitore delle note strutturate ci si riferisce
- £NSTPG      :  è il nome del programma che chiama questa gestione
- £NSTTO      :  è il tipo di origine  :  o da tabella e quindi si specifica TA nel campo, o definito a programma e quindi il campo sarà BLANKS
- £NSTPO      :  è il parametro origine, se £NSTTO = TA devo definire la tabella a cui fare riferimento, altrimenti il campo resta BLANKS
- £NSTEO      :  è l'elemento della tabella £NSTPO se tale campo è diverso da BLANKS
- £NSTT1/2/3  :  tipo codice 1/2/3 sono i tipi delle chiavi di accesso alle note
- £NSTP1/2/3  :  parametro codice 1/2/3, dato il Tipo Codice è possibile specificare anche il parametro
- £NSTVI      :  con questo campo si possono specificare i vincoli riguardanti le funzioni della tabella
B£R
= si gestiscono solo le Note Strutturate
2 = si gestiscono solo le Liste di Distribuzione 3 = si gestiscono solo le Informazioni
E' possibile usare anche delle combinazioni tra queste funzioni, ad es. 1/2, 2/3,1/3
Se il campo non ha valori si assume che non ci siano vincoli sulle opzioni della tabella B£R (1/2/3).
Per capire quali elementi della tabella scelgliere è stato fatto il controllo sul campo T$TIFU (Tipo Funzione) che assume i seguenti valori NOTE, INFORM, LISTA
# TABELLE
###
###

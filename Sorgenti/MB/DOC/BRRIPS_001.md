# Introduzione
E' possibile collegare ad una riga di ciclo una serie di funzioni, richiamabili sia dalla lista, sia dal dettaglio, per gestire il dettaglio del ciclo, le note, i parametri, le risorse secondarie, ecc.
La routine che guida queste operazioni è la BRG.
Le singole azioni codificate sono elementi (B£J) di una B£H di elemento A-F2xxx (dove xxx è il tipo ciclo), se assente si risale all'elemento A-F2.
Si suggerisce di codificare, come sottosettore delle azioni nelle B£H, il valore F2.
Per diversificare le azioni in diversi tipi ciclo (mantenendo lo stesso sottosettore), si suggerisce di impostare opportunamente i limiti nell'elemento di B£H.

# Funzioni standard
Sono state realizzate 10 funzioni standard, per ciascuna delle quali è previsto un programma che le sviluppa.
E' inoltre possibile popolare gli elementi di B£J in modo standard richiamando (T BRG) con funzione e metodo  BAS / COS. Questa funzione popola gli elementi nel sottosettore F2.
Attenzione :  dopo aver eseguito il popolamento si consiglia di rivedere tutti gli elementi creati, in modo da completarli con i campi non popolati, e da controllare l'effettiva presenza di tutti i codici proposti.

Gli elementi standard sono i seguenti (creati nel sottosettore F2)

## Dettaglio della riga di ciclo
Nome Elemento proposto :  A10
Programma :  BRBRG_01
Struttura parametri : 
- Posizione 1 - 3 :  'DET' (fisso)
### Funzione eseguita
Richiama il dettaglio in manutenzione (02)  o interrogazione (05) o ne presenta i campi (funzione '+' mostra dettaglio)

## Valori
Nome Elemento proposto :  A12
Programma :  BRBRG_02
Struttura parametri : 
- Posizione 1 - 3 :  'DET' (fisso)
### Funzione eseguita
Richiama il dettaglio in manutenzione (02)  o interrogazione (05) o ne presenta
i 10 valori di tempo (funzione '+' mostra dettaglio)

## Componenti di carico
Nome Elemento proposto :  A14
Programma :  BRBRG_03
Struttura parametri : 
- Posizione 1 - 3 :  'DET' (fisso)
### Funzione eseguita
Richiama il dettaglio in manutenzione (02)  o interrogazione (05) o ne presenta i 10 componenti di carico (funzione '+' mostra dettaglio)

## Componenti di costo
Nome Elemento proposto :  A16
Programma :  BRBRG_04
Struttura parametri : 
- Posizione 1 - 3 :  'DET' (fisso)
### Funzione eseguita
Richiama il dettaglio in manutenzione (02)  o interrogazione (05) o ne presenta i 10 componenti di costo (funzione '+' mostra dettaglio)

## Materiali alla fase
Nome Elemento proposto :  B10
Programma :  BRBRG_05
Struttura parametri : 
- Posizione 1 - 3 :  'MAT' (fisso)
- Posizione 4 - 6 :  Tipo distinta (elemento di BRL) :  se assente viene assunto ART
### Funzione eseguita
Gestisce i materiali alla fase, richiamando in manutenzione (02) o in
interrogazione (05) la funzione di assegnazione materiali alla fase, o ne presenta l'elenco (funzione '+' mostra dettaglio)

## Ciclo di collaudo
Nome Elemento proposto :  C10
Programma :  BRBRG_06
Struttura parametri : 
- Posizione 1 - 3 :  'COL' (fisso)
- Posizione 4 - 7 :  Ciclo di collaudo (elemento di CRJ) - Campo obbligatorio
### Funzione eseguita
Gestisce i cicli di collaudo, richiamando in manutenzione (02) o in interrogazione (05)  la gestione dei cicli di collaudo della fase, o ne presenta i valori (funzione '+' mostra dettaglio)

## Attività eseguite sulla fase
Nome Elemento proposto :  D10
Programma :  BRBRG_07
Struttura parametri : 
- Posizione 1 - 3 :  'ATT' (fisso)
### Funzione eseguita
Gestisce le attività eseguite per la fase, richiamando in manutenzione (02) o in interrogazione (05) la lista delle attività eseguite, o ne presenta l'elenco (funzione '+' mostra dettaglio).

## Note
Nome Elemento proposto :  E10
Programma :  BRBRG_08
Struttura parametri : 
- Posizione 1  3 :  'NOT'  (fisso)
- Posizione 4  7 :  Contenitore (elemento di NSC) - Campo obbligatorio
- Posizione 8  10 :  Tipo informazione (elemento di NSI) - Campo obbligatorio
- Posizione 11 12 :  Tipo chiave 1 (V2/BRPCC) - Campo obbligatorio
- Posizione 13 14 :  Tipo chiave 2 (V2/BRPCC)
- Posizione 15 16 :  Tipo chiave 3 (V2/BRPCC)
In questo elemento non sono obbligatori i valori della seconda e terza chiave (almeno una deve esserci). E' cura dell'installatore garantire la congruenza tra tra l'elemento di NSC impostato e i valori delle chiavi.
### Funzione eseguita
Gestisce le note per la fase, richiamando in manutenzione (02) o in interrogazione (05) la gestione delle note strutturate, o presenta l'elenco delle note presenti
(funzione '+' mostra dettaglio).

## Parametri
Nome Elemento proposto :  F10
Programma :  BRBRG_09
Struttura parametri : 
- Posizione  1 -  3  :  'PAR' (fisso)
- Posizione  4 -  6  :  Categoria (Elemento della C£E) (1)
- Posizione  7 -  8  :  Tipo chiave 1 (V2/BRPCC)
- Posizione  9 - 10  :  Tipo chiave 2 (V2/BRPCC)
- Posizione 11 - 13  :  Parametro singolo (2)
- Posizione 14 - 14  :  Categoria da ciclo collegato (Valore SI/NO)
- Posizione 15 - 17  :  Categoria (Elemento della C£E)  (3)
- Posizione 18 - 20  :  Parametro (Elemento della B£N del sottosettore della C£E prececente)  (4)
La determinazione della categoria dei parametri avviene in due modi : 
Se non impostato il flag 'Categoria da ciclo collegato' si assume la categoria (1).
Se invece si imposta il flag 'Categoria da ciclo collegato' si devono impostare la categoria (3) ed il parametro (4).
Se presente, per l'oggetto codice collegato (R§CODC), un valore per questo parametro, in questa categoria, esso (che si assume sia una categoria parametri) sostituisce la (1).
In tal modo si ottiene l'effetto di una diversificazione dinamica dei parametri della fase, in base ad una caratteristica 'esterna'.
Si devono impostare i tipi chiave 1 e 2 in modo congruente alla griglia presente nella categoria (impostata o derivata).
Per le precedenti ragioni, non è stata introdotta nessuna obbligatorietà nella compilazione dei campi :  è cura dell'installatore garantire la completezza e la congruenza dell'impianto.
E' possibile inoltre, se non è stata abilitata la deviazione della categoria, definire un parametro, nel campo parametro singolo (3), con i seguenti effetti : 
. La segnalazione di presenza parametri viene controllata solo su questo parametro
. Nella funzione mostra dettagli (+) viene presentato solo questo parametro.
Le altre funzioni :  Dettaglio (modifica, copia, visualizzazone e annullamento) e Applicazione (copia e cancellazione totale) operano su tutti i parametri della categoria.
### Funzione eseguita
Gestisce i paramentri della fase, richiamando in manutenzione (02) o in interrogazione (05) la gestione dei parametri, o presenta l'elenco dei paramentri
(funzione '+' mostra dettaglio).

## Risorse produttive secondarie
Nome Elemento proposto :  G10
Programma :  BRBRG_10
Struttura parametri : 
- Posizione  1 -  3  :  'RPS' (fisso)
- Posizione  4 -  6  :  Tipo aggancio (Elemento della BRJ) - Campo obbligatorio
- Posizione  7 -  8  :  Tipo chiave 1 (V2/BRPCC)
- Posizione  9 - 10  :  Tipo chiave 2 (V2/BRPCC)
- Posizione 11 - 13  :  Elemento BRK - Campo obbligatorio
E cura di chi imposta la tabella garantire la congruenza tra i campi definiti nell'elemento di BRJ imposato ed i tipi chiave 1 e 2.
### Funzione eseguita
Gestisce le risorse produttive secondarie della fase, richiamando in manutenzione (02) o in interrogazione (05) la loro gestione, o ne presenta l'elenco (funzione '+' mostra dettaglio)

## RichIamo da manutenzione tabelle B£J
E' possibile creare altri elementi in modo guidato, selezionando, nella codifica dell'elemento B£J, l'applicazione BR (nel campo "Nome programma"), quindi il contesto BRGFAS_0, ed infine la funzione (corrispondente ad una delle 10 precedentemente descritte), che riempirà il campo del programma.
Si presenterà il consueto formato di sottostringatura dei parametri aggiuntivi, diverso a seconda del programma scelto.

# Lancio azioni
Dalla lista delle righe di un ciclo di un oggetto, con l'opzione 12 (Scheda - Gestione ) o 15 (Scheda - Visualizzazione), si passa ad un ulteriore lista che riporta tutti gli elementi di B£J definiti in precedenza.
Accanto al codice e alla descrizione della B£J è segnalata la presenza di valori, ed è riportato il tipo di sviluppo.
Le principali opzioni ammesse sono le seguenti : 
02/03/04/05 :  modifica/copia/cancella/visualizza :  azioni polimorfe che lanciano la funzione in base al tipo di sviluppo (note, parametri, dettaglio ....).
+  :  Mostra dettaglio :  la lista viene espansa; al di sotto della riga di sviluppo vengono riportati gli elementi relativi :  azione polimorfa che riporta un dettaglio diverso in base al tipo sviluppo.
-  :  Nasconde dettaglio :  viene chiusa una lista espansa.
12  :  modifica impostazioni (si passa alla manutenzione dei parametri aggiuntivi dell'elemento della B£J (anch'essa polimorfa :  la sottostringatura è diversa in funzione del tipo sviluppo).

## Autorizzazioni
Le autorizzazioni al lancio di queste funzioni sono specifiche, e quindi possono diversificarsi da quelle delle stesse funzioni lanciate in modo 'classico'.
In particolare la classe è 'ABILITA', la funzione è 'B£J' + sottosettore della B£J + Elemento della B£J.

# Risorse produttive secondarie
E' possibile collegare ad una coppia di oggetti presenti in una riga di ciclo (definita dall'elemento di B£J di tipo RPS tramite l'elemento di BRJ che ne specifica il tipo, e i due tipi chiave che ne fissano la posizione) un ulteriore oggetto, che completa l'univocità della chiave (contenuto nell'elemento di BRK, definito anch'esso nella B£J).
L'effettiva chiave univoca delle risorse secondarie è : 
- Elemento BRJ
- Chiave 1 (del ciclo :  tipizzata in BRJ)
- Chiave 2 (del ciclo :  tipizzata in BRJ)
- Elemento BRK
- Chiave 3 (inserita manualmente :  tipizzata in BRK)
- Data inizio validità (per poter trattare variazioni nel tempo).

In tal modo si possono collezionare vari oggetti per una riga di ciclo.
Oltre alla chiave 3, si possono inserire ulteriori informazioni, la cui natura è guidata dal modello, presente sempre nella BRK.
Oltre ai modelli standard (che iniziano con *) è possibile definirne di specifici (programmi che configurano il formato di dettaglio di manutenzione dei dati).

Ad esempio. è possibile codificare gli attrezzi utilizzati in una riga di ciclo.
L'impostazione della B£J è la seguente : 
BRJ = A/F (articolo/fase)
Tipo chiave 1 = 02 (Codice asseme del ciclo)
Tipo chiave 2 = 04 (Fase)
BRK= elemento che definisce la terza chiave :  AR/STA (se il tipo articolo STA individua gli stampi).

La manutenzione di queste informazioni si esegue dalla lista degli sviluppi (B£J).
L'opzione 02 lancia la lista delle risorse produttive secondarie presenti per la BRK, con la possibilità di modificarne il dettaglio, o di aggiungerne di nuove.
Va tenuto presente che l'oggetto inserito (come terza chiave) non può essere modificato, in quanto fa parte della chiave univoca dell'archivio. Per variarlo lo si deve annullare ed inserire il nuovo valore.

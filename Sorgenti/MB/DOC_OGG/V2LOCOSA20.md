## Obiettivo
Gestire attraverso un'unico componente il salvataggio delle informazioni di "Setup" collegate ad un componente.
Le funzioni di gestione delle MDV dell'ambiente 5250, se richieste in ambiente grafico, verranno gestite dal nuovo componente.

## Struttura
Tutte le informazioni saranno identificate tramite due caratteristiche principali : 
1) La struttura, questa definisce la modalità di presentazione delle informazioni
2) Il contesto, il contesto è paragonabile al sottosettore di una tabella, lega le informazioni di una stessa struttura a eventi diversi.

## Gestione delle Memorizzazioni Video 5250
Attraverso il nuovo componente, vengono mantenute le stesse funzionalità oggi presenti nell'ambiente 5250.
Per attivare la gestione grafica bisogna utilizzare il carattere '\', se seguito dal nome della MDV questa verrà letta senza passare dalla gestione.
L'oggetto ID MEDAV00F non è in grado di recuperare il contesto, se ci si riferisce ad una MDV di livello utente, per questo motivo è stato disabilitata la possibilità di utilizzare le funzioni associate all'oggetto.

## Gestione dei setup dei componenti grafici
Oltre alle normali operazioni di salvataggio del setup sono state rese disponibili le seguenti possibilità : 

1) Definizione di un Setup di Componente
2) Possibilità di fondere il setup principale con attributi derivati da un Setup di riferimento

Se si decide di utilizzare un Setup di riferimento verranno salvati solo gli attributi differenti dal Setup di riferimento.
Questo permetterà, una volta modificato il setup di riferimento, di avere la propagazoione delle variazioni su tutti i setup a cui si riferisce.
Il Setup di riferimento, deve essere un setup standard di componente (J3_SET_STD) o un proprio setup.

### Setup standard di componente
I setup di componente devono risiedere nello script J3_SET_STD presente nel sorgente SCP_SCH.
Ad ogni setup deve essere assegnato un nome.

## Comunicazione
La comunicazione del Setup avviene attraverso il parametro INPUT della funzione (£UIBD1) nel quale viene passato l'intero XML di setup. Esso viene quindi depurato di eventuali nodi diversi, mantenendo il solo nodo <Setup>.

## Il Setup dell'utente *JOB
Il setup attualmente in uso viene identificato con utente *JOB. Su questo setup possono essere eseguite tutte le normali operazioni di gestione dei setup.

## Ultimo utilizzo *LAST
La MDV  dell'ultimo utilizzo viene identificata con nome *LAST. Su questa MDV possono essere eseguite tutte le normali operazioni di gestione della MDV.

## Autorizzazioni USRLVL
 :  : DEC T(TA) P(B£P) K(USRLVL)
La funzione che caratterizza la classe è "LOA20_SE"
Se abilitati almeno al livello 01 sarà concesso il salvataggio su qualsiasi utente e/o gruppo, altrimenti verrà concessa autorizzazione solo al proprio utente e al gruppo di appartenenza.

## Autorizzazioni
 :  : DEC T(TA) P(B£P) K(D)
Le autorizzazioni sono oggi gestite a livello generale, non sono quindi impostabili per Struttura o Contesto.
La funzione che caratterizza la classe è "LOA20_SE"

Elenco azioni : 
01 Aggiunta
02 Modifica
03 Copia
04 Cancellazione
05 Visuallizza

## Prototipi di chiamata del setup
**Gestione**
A(EMU;LOA20_SE;SCH) P(Str(**[Struttura]**) Con(**[Contesto]**)) SS(CGr(**[Componete_Grafico]**)) INPUT(**[Immagine_del_Setup_Corrente]**)
**Scrittura di un nuovo Setup**
A(EMU;LOA20_SE;WRI) P(Str(**[Struttura]**) Con(**[Contesto]**) UteFrm(**[Utente_di_copia]**) NamFrm(**[Nome_di_copia]**) Ute(**[Utente]**) Nam(**[Nome]**))
**Cancellazione di un Setup**
A(EMU;LOA20_SE;DEL) P(Str(**[Struttura]**) Con(**[Contesto]**) Ute(**[Utente]**) Nam(**[Nome]**))
**Modifica di un nuovo Setup**
A(EMU;LOA20_SE;UPD) P(Str(**[Struttura]**) Con(**[Contesto]**) Ute(**[Utente]**) Nam(**[Nome]**))
**Copia di un nuovo Setup**
A(EMU;LOA20_SE;WRI) P(Str(**[Struttura]**) Con(**[Contesto]**) UteFrm(**[Utente_di_copia]**) NamFrm(**[Nome_di_copia]**) Ute(**[Utente]**) Nam(**[Nome]**))

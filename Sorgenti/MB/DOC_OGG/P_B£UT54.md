# Costruzione menu utenti
Con questa funzione, attraverso l'autorizzazione o meno delle azioni di menu presenti, si possono costruire menù specifici per gli utenti appartenenti ad un gruppo utente.

## Lancio della funzione
La funzione può essere lanciata dalla funzione "Menù a parametri per gruppo utente" della gestione UT5.

## Formato guida
Il formato guida è il seguente : 

![B£UT54_01](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT54/BXUT54_01.png)
Inserire : 

- **Gruppo autorizzazione**, è un elemento della tabella B£*_GU e rappresenta il gruppo utente per cui costruire il menu specifico. Tutti gli utenti appartenenti al gruppo assumeranno lo stesso menù.
- **Codice menù da autorizzare**, è il sottosettore della tabella MEA in cui sono descritte le azioni appartenenti al menu da autorizzare.
- **Azione iniziale - Azione finale**, campi non obbligatori, se compilati flitrano la lista delle azioni.
- **Menù iniziale di riferimento**, campo non obbligatorio, è utile quando abbiamo azioni mea in sottosettori diversi dove ad esempio il menù principale è nel sottosettore 00 mentre i menù secondari sono in altri sottosettori, per applicazione; vedi il paragrafo note tecniche per la spiegazione del funzionamento.

Inseriti i dati con - ENTER - si passa alla lista delle azioni di menù : 

![B£UT54_02](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT54/BXUT54_02.png)
In questa lista sono possibili le azioni seguenti : 

- **AM = Abilita tutto il menù**, questa azione è possibile solo sulla riga dell'intero menù, se impostata permette di autorizzare direttamente tutte le azioni del menù. Quando tutto il menù è autorizzato la riga viene evidenzata (reverse rosso) e compare la scritta **Abilitato tutto il menù; in questa condizione le singole righe sono in colore rosso e le opzioni non sono attive.
- **DM = Disabilita tutto il menù**, questa azione è possibile solo sulla riga dell'intero menù e se l'intero menù era stato in precedenza abilitato tutto, se impostata toglie le autorizzazioni a tutte le azioni del menù.
- **A = Abilita**, questa azione è possibile solo sulle righe delle azioni, se impostata permette di autorizzare l'azione. Quando l'azione è autorizzata la riga viene evidenzata (alta intensità) e compare la scritta **Abilitata**.
- **D = Disabilita**, questa azione è possibile solo sulle righe delle azioni, se impostata toglie l'autorizzazione all'azione. Quando l'azione è disabilitata la riga perde l'evidenza e compare la scritta **Disabilitata**.


Completata l'attività il comando funzione F6 conferma le attività eseguite ed esce dalla lista, mentre il comando funzione F15 conferma le attività eseguite e resta nella lista aggiornata.
Se si esce senza premere F6 o F15 gli aggiornamenti vengono persi.

# Note tecniche
Questo genere di autorizzazioni viene attribuito attraverso il parametro multiplo __xx__, presente nella categoria __MEA__. Se il parametro non esiste il programma crea automaticamente l'elemento xx nella tabella B£N_ME.

Quando è gestita l'autorizzazione per la singola azione l'oggetto dei parametri è il codice azione con prefisso il sottosettore (es. BR0101 Gestione articoli), mentre quando è autorizzato l'intero menù allora l'oggetto dei parametri è il sottosettore seguito da due asterischi, es. V5**.

**Per fare in modo che vengano usati questi menù nella gestione ambienti deve essere impostato il tipo accesso G = Menù SMEUP :  Parametri Gruppo B£U.

Quando le azioni di menu sono su più sottosettori diversi della tabella MEA (esempio sottosettore 00 = Menù principale, C5 = Menù Contabilità, V5 = Menù Acquisti, ....), per gestire le abilitazioni anche sui menù di livello inferiore, la tabella MEA che richiama il sottosettore del Menù di livello inferiore deve essere compilata come segue : 
![B£UT54_03](http://localhost:3000/immagini/MBDOC_OGG-P_B£UT54/BXUT54_03.png) * Programma/Azione, deve essere il codice del sottosettore
 * Parametro, fisso &UG (User group)

In questi casi, che sono quelli consigliati nel modello di installazione TTR, volendo autorizzare ad esempio le azioni della gestione materiali (menù GM) bisogna autorizzare le azioni mettendo nel codice menù da autorizzare "GM" e poi autorizzare l'azione che richiama il menù mettendo nel codice menù da autorizzare "00". **Se si utilizza il campo menù iniziale di riferimento si possono gestire entrambe le autorizzazioni contemporaneamente, nell'esempio di cui sopra metteremo GM nel campo menù da autorizzare e 00 nel campo menù iniziale di riferimento, si presenterà la lista delle azioni presenti nel menù GM e con l'autorizzazione si attiveranno insieme sia le autorizzioni sulle azioni dentro il menù GM sia l'autorizzazione nel menù 00 per l'azione che richiama il menù gestione materiali.
L'automatismo opera sia quando l'autorizzazione viene data che quando viene tolta.

Queste abilitazioni sono per Gruppo Utente, se all'interno del menù del gruppo utente si vogliono definire delle autorizzazioni specifiche a determinate azioni o menù/sottomenù per singolo utente allora si rimanda alla classe di autorizzazioni utente __MENU__, la cui spiegazione è nel paragrafo "Classi particolari" della documentazione applicativa del modulo B£AUTO.

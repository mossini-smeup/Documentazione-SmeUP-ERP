# Versione 1
 * Gestione con xsl : fo

# Versione 2
 * Generazione tramite iText
 * Supporto XML della scheda (senza la gestione delle variabili) per quanto riguarda le sezioni di tipo MAT, TXT, IML, IMG, TRE, TRA, HTM, CHA.
 * Caratteristiche di configurabilità del documento :  Formato, Copertina, Indice, Header, Footer.
 ** Formato :  PageFormat (A4, A3, Letter), Orientamento (Vertical, Landscape), Margini di pagina (sx, dx, alto, basso), Overlay (file pdf), Colore titoli capitoli e sezioni
 ** Copertina :  Titolo, Colore Font, Colore sfondo
 ** Indice :  Colore titolo, colore testi
 ** Header :  Logo, testo, numerazione pagina, colore sfondo, colore testo
 ** Footer :  Logo, testo, numerazione pagina, colore sfondo, colore testo

# Versione 3
 * Configurazione di stampa tramite G30 - Caratteristiche supportate
 ** Setup formato
 *** PDF, HTML, RTF
 ** Setup documento
 *** Pagesize
*** Orientamento
 *** Margini
 ** Setup copertina
 *** Presenza copertina
 *** Informazioni di copertina
 *** Colore testo copertina
 *** Colore sfondo copertina
 ** Setup indice
 *** Presenza indice
 *** Colore testo capitoli
 *** Colore testo sezioni
 ** Setup header
 *** Presenza contatore di pagina
 ** Setup footer
 *** Presenza contatore di pagina

# Versione 4
 * Stampa delle sezioni della scheda (testo, matrice, albero, lista immagini orizzontale e verticale)
 * Stampa della documentazione attiva
 ** Gestione dei livelli di sviluppo che il generatore PDF ricorrerà nei link ad altri file di documentazione
 ** Stampa "AllinOne" :  creazione di un unico file PDF
 ** Stampa non "AllinOne" :  creazione di una cartella di progetto contenente n files PDF, uno per ogni file di documentazione che viene trovato e collegati da link ipertestuali

# Versione 5
Creato il generatore di PDF dagli Spool. Si appoggia sul servizio _B_B£SER_06.
Effettuata divisione in base alla tipologia di documento generato (PDF Documentazione, PDF Scheda, PDF Spool).
A livello generale abilitate le opzioni per :  la visualizzazione del XML della stampa per debugging, disabilitare l'elaborazione del contenuto per stampe debugging, per salvare il setup di stampa nella sessione e non richiederlo con gestione del ripristino della richiesta.

## Doc Generator subv. 2.5
 * Sistemata la gestione delle immagini incluse tramite il tag **IMG** anche internamente ai **PAR**.
 * Supporto delle liste annidate

## Sch Generator subv. 2.3
 * Portate le sezioni di scheda a livello di Sezioni PDF anzichè di capitoli per limitare le dimensioni del documento e migliorare la leggibilità
 * Abilitata nel setup della stampa l'opzione per avere le tabelle splittate o meno
 * Nella stampa delle liste immagini (sezioni IML)  e dell' immagine oggetto aggiunta la label con la descrizione dell'oggetto (per ora fissa in seguito opzionale da setup)
 * Nella stampa dei Chart :  utilizzo del Chart generato dalla scheda per l'inclusione nel PDF

## Spool Generator subv. 2.1
 * Possibilità di portare uno spool AS in PDF tramite la scheda degli Spool utente (_B_MB-SCP_SCH-B£SPLF).
 * Definizione dello script di configurazione (MB-SCP_CFG-EDT_SPL) che definisce la sintassi del file di schema (ricercato in MB-SCP_SPL) per la generazione di una stampa grafica degli spool AS.
 * Le specifiche supportate sono : 
 **  :  : INC per l'inclusione come sfondo di un file PDF;
 **  :  : ROW per la definizione della rappresentazione di parte dello spool come paragrafi del documento, potendo definire Font (Stile, Dimensione, Tipo), Colore, Altezza riga.
 **  :  : TXT per la rappresentazione, secondo coordinate assolute nel foglio di parte dello spool come testo, potendo definire Posizionamneto, Font (Stile, Dimensione, Tipo), Colore, Altezza riga, Colore Sfondo.
 **  :  : BOX per la rappresentazione grafica di un riquadro, secondo coordinate assolute nel foglio, potendo definire Posizionamento, Altezza e Larghezza, Eventuale Label associata, Font (Stile, Dimensione, Tipo), Colore, Altezza riga della label (se presente), Colore bordi della box.
 **  :  : ROX per la rappresentazione grafica di un riquadro con bordi arrotondati, secondo coordinate assolute nel foglio, potendo definire Posizionamento, Altezza e Larghezza, Eventuale Label associata, Font (Stile, Dimensione, Tipo), Colore, Altezza riga della label (se presente), Colore bordi della box.
 **  :  : NPG per forzare un salto pagina.
 **  :  : PAG per il posizionamento di una immagine secondo coordinate assolute nel foglio, potendo definire Il percorso dell'immagine da includere, Posizione nel foglio e dimensioni del riquadro.
 **  :  : LIN per il tracciamento di una linea secondo coordinate assolute nel foglio, potendo definire Colore della linea e punto di partenza e di arrivo.
 **  :  : BCD per la rappresentazione un barcode secondo coordinate assolute nel foglio, potendo definire Tipo di barcode fra i tipi supportati e visualizzati nel wizard, Sezione dello spool dove è presente il valore, Posizione nel foglio del barcode.
 * Possibilità di associare, per ora manualmente poi direttamente dal servizio AS, un file di schema alla stampa dello spool AS in PDF per la resa grafica del contenuto dello spool.

# Versione 5.1 del 28 Ottobre 2005
 * Aggiunta la possibilità di definire una password di apertura del documento generato.
 * Aggiunta la possibiltà di impaginare il PDF 2 pagine in una.

## Doc Generator subv. 2.6
 * Supportato il tipo paragrafo L(TAB) che permette di rappresentare una tabella.
 * Le righe sono indicate tramite il trattino (**-**) ad inizio riga
 * Ogni riga contiene i valori delle celle separati da pipe (**|**)
 * Se la prima riga contiene una serie di numeri la cui somma da 100 viene interpretata come definizione delle percentuali di dimensionamento delle colonne
 * Nel caso in cui il dimensionamento delle colonne sia presente (punto 3) la seconda riga viene presa come intestazione della tabella, altrimenti viene presa la prima.

Esempio : 

|  T(Esempio tabella) |
| 30|50|20 |
| ---|----|----|
| **Test**|_1_tabella**|_3_HTML** |
| riga|dati|esempio |
| 


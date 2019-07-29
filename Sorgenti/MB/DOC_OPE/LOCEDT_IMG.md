# Introduzione
Un'immagine viene inserita con la seguente TAG, dove P(...) definisce il percorso.
 :   : IMG P([SME.IMG]\TAB£A\S5\S5IRIS\FIG_060.jpg)

Il percorso delle immagini relative alla documentazione attiva delle applicazioni è : 
 * [SME.IMG] - radice del percorso
 * TAB£A - cartella delle applicazioni
 * S5 - nome dell'applicazione
 * S5IRIS - nome del modulo
 * FIG_060.jpg - nome dell immagine

# Utilizzo in HTML
Nell'HTML l'immagine viene incorportata senza ridimensionamento.

# Utilizzo in PDF
Nell'XML l'immagine può essere ridimensionata con le seguenti parole chiave : 
 * R(xx) riduzione, dove xx è la percentuale di riduzione (1 - 99)
 * H(yyy) ridimensionamento verticale, dove yyy è la percentuale rispetto ai margini di scrittura del documento (dimensione verticale foglio - margine superiore - margine inferiore). Se il numero è superiore a 100 o inferiore a 10 viene forzato a 70.
 * W(yyy) ridimensionamento orizzontale, dove yyy è la percentuale rispetto ai margini di scrittura del documento (dimensione orizzontale foglio - margine sinistro - margine destro). Se il numero è superiore a 100 o inferiore a 10 viene forzato a 70.

Relativamente ai punti postscript : 
 * il formato A4 verticale ha come dimensioni :  larghezza 595, altezza 842
 * il formato A4 orizzontale ha come dimensioni :  larghezza 842, altezza 595

L'attributo R ha la precedenza su H e W, l'attributo W ha la precedenza su H

Se l'immagine è troppo estesa rispetto alla pagina (dopo averla eventualmente ridimensionata in presenza di parole chiave), viene comunque ridotta alla dimensione della pagina, operando sulla dimensione critica e riducendo l'altra proporzionalmente.

Nell'XML l'immagine può essere identificata con la parola chiave "IMGREF" come segue : 
 :   : IMG P([SME.IMG]\TAB£A\S5\S5IRIS\FIG_060.JPG) ImgRef(XXX)
L'attributo  può essere aggiunto utilizzando il wizard, compilando correttamente il campo "Label di riferimento" con l'identificativo scelto. L'identificativo scelto deve contenere solo caratteri alfanumerici e deve essere un identificativo univoco.
L'immagine potrà essere richiamata in qualsiasi punto del testo con la sintassi seguente evidenziata in colore _2_blu : 
testo testo testo _2_ImgRef (XXX) testo testo testo ...

# Suggerimenti per la cattura delle immagini da video
Si consiglia di catturare le copie schemo su terminali di piccole dimensioni, in modo da non penalizzarne la consultazione su di essi.
Il formato può essere JPG, con riduzione al 90%, oppure si consiglia di utilizzare il formato PNG che rispetto al JPG garantisce una qualità migliore anche quando le dimensioni vengono ridotte.

# Suggerimenti per il dimensionamento delle immagini in stampa PDF
Per stampe di videate si consiglia una riduzione al 40% :  R (40)
Per stampe di schede si consiglia una riduzione al 35% :  R (35).

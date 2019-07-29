# Premessa

L'Aggiunta di una voce personale nella MEA standard può avere effetti a livelli diversi a seconda di come questa voce viene configurata.
Definendo in modo opportuno questa nuova voce, essa può trovare posto : 
* Tra le ACTIONS di un MODULO, compilando correttamente il campo T$MEAL "modulo appartenenza". Riempiremo quindi questo campo con "BRARTI" se vogliamo inserire nelle actions di questo modulo una nuova voce di menù; è ovvio che tale voce personale dovrà essere inserita nel sottosettore BR, essendo il BRARTI un modulo di questa applicazione (le prime due lettere del modulo indicano l'applicazione cui esso appartiene). 
* Tra i MODULI di una APPLICAZIONE, mettendo la "D" nel campo T$MEAE "Tipo Azione" e lasciando invece il campo T$MEAL "modulo appartenenza" vuoto. Questo avrà come effetto quello di aggiungere una voce all'interno della sezione di destra della schermata iniziale di Looc.UP. 
* Nel MENU DI ACCESSO, ovvero nella sezione di sinistra della scheda di partenza, a livello di area applicativa/applicazione :  in questo caso sarà necessario aggiungere la voce personale al menù di accesso dell'utente nel sottosettore 00.

Per un maggiore daettaglio si rimanda al capitolo "Personalizzazione dei menù di accesso" presente nella documentazione riportata di seguito : 
- [Menù di Accesso Utente](Sorgenti/MB/DOC/B£MENU_02)


# Passi operativi

Ecco dunque cosa fare per aggiungere una voce personale a un menù standard.

1) Collegarsi al proprio ambiente e digitare il comando UP TAB o scegliere l'applicazione B£TABE e di conseguenza la voce "Gestione elementi" tra le actions.
2) Scegliere il settore MEA e il relativo sottosettore all'interno del quale si vuole aggiungere la voce personale.
Ricordimao che i sottosettori della MEA corrispondono alle applicazioni standard di Sme.UP, eccezzione fatta per il sottosettore generale "00" che racchiude le voci del menù iniziale.
3) Indicare l'opzione "01" di inserimento e digitare il codice progressivo della voce di menù che si intende aggiungere.
4) Procedere poi alla compilazione di tutti i campi della tabella, prestando particolare attenzione ai campi che sono stati citati che influenzano la posizione in cui la voce comparirà.
Occorre prestare particolare attenzione al campo "Ordinamento" perchè è tramite il valore riportato in questo campo che la voce personale troverà la giusta collocazione nel menù.
Si consiglia di lasciare questo campo vuoto se si vuole che la voce trovi posto prima di tutte le altre voci, di compilarlo con "999999999" se si vuole che la voce sia l'ultima, o di compilarlo con una qualsiasi altra combinazione se si vuole che la voce appaia in un determinato posto.
Per comprendere meglio l'utilità di questo campo e il suo scopo, si rimanda alla documentazione specifica della voce "rordina menù" presente tra le actions del modulo B£MENU.
 :  : DEC T(MB) P(DOC_VOC) K(M_B£MENU)


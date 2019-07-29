# Obiettivo
Interfacciare il parametro delle voci dei menù smeup. Attraverso tale costruzione vengono identificati in modo univoco i differenti menù smeup.

**NOTA BENE**
La definizione di un menù Smeup ha natura eterogenea, per tale motivo la sua identificazione avviene secondo differenti criteri di codifica : 
* "*codiceSSMEA" :  identifica un menù costruito a partire dalle voci di un SSMEA
* "*xx;xxxxxxxx" :  identifica un menù parametrico costruito a partire dai parametri degli elementi della tabella MEA
* "A_codiceTAB£A" :  identifica il menù di un'applicazione (cioè di un elemento della tabella B£A)
* "M_codiceTAB£AMO" :  identifica il menù di un modulo (cioè di un elemento della tabella B£AMO)
* J1parametroJ1 :  identifica il menù di un oggetto J1
* J7parametroJ7 :  identifica il menù di un oggetto J7
* J9parametroJ9 :  identifica il menù di un oggetto J9
* S_codicefilesorgente :  identifica il menù di un membro di un file sorgente
* I_codicefiledati :  identifica il menù di record di un file dati
* O_SEtipoSE :  identifica il menù di una delle istanze che fanno capo all'oggetto SE
* O_OJ_USR :  identifica il menù di utente di sistema
* O_classeoggetto :  identifica il menù di una classe oggetto (istanza oggetto OG)
* CodicescriptSCP_MNU :  identifica un menù non ricollegabile ad un particolare oggetto, ma definito a partire da un particolare codice script di menù.

Ad eccezione delle prime due, le sopracitate codifiche corrispondono poi anche al codice del membro di script di menù che viene ricercato per l'elaborazione del menù stesso, ma rispetto a questo è importante notare che non è detto che il codice vi coincida :  sono infatti previste alcune risalite attraverso cui, in assenza dello script di riferimento principale, viene preso in riferimento uno script di riferimento secondario : 
* "A_codiceTAB£A" => O_TAB£A
* "M_codiceTAB£AMO" => O_TAB£AMO
* J1parametroJ1 => J1
* J7parametroJ7 => J7
* J9parametroJ9 => J9
* O_classeoggetto => O_tipooggetto => O_

# Funzioni e metodi
* " " Controllo/Decodifica di un parametro
* "RIT" Dato un oggetto ritorna il codice del parametro di menù di riferimento
* "RIM" Dato un oggetto ritorna il codice del parametro di menù di riferimento e lo script SCP_MNU da leggere per l'elaborazione delle voci

# Altri Parametri di Input
* £IMPI_VP :  Parametro Voce
* £IMPI_TP :  Tipo Oggetto di Riferimento
* £IMPI_CD :  Codice Oggetto di Riferimento

# Campi di Output
* £IMPO_MS :  Codice messaggio ritorno
* £IMPO_FI :  File messaggio ritorno
* £IMPO_35 :  Se On = Codice errato
* £IMPO_36 :  Se On = eseguita ricerca alfabetica
* £IMPO_VP :  Parametro Voce di menù
* £IMPO_DE :  Descrizione Parametro Voce di Menù
* £IMPO_TP :  Tipo Oggetto di Riferimento del Menù :  se il menù è il menù di riferimento di un un oggetto viene in questo campo riportata la classe di tale oggetto es. M_B£BASE => TAB£AMO
* £IMPO_CD :  Codice Oggetto di Riferimento del Menù :  se il menù è il menù di riferimento di un un oggetto viene in questo campo riportata l'istanza di tale oggetto es. M_B£BASE => B£BASE
* £IMPO_SC :  Script di Riferimento per l'elaborazioni delle voci del menù


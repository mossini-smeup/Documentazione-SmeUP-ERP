# CFS - Sezioni del Questionario
 :  : DEC T(ST) K(CFS)
## OBIETTIVO
Definire le sezioni che compongono un questionario. Una sezione è un contenitore di domande, quindi la sua definizione consiste nel Definire da quali domande è composta.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM  **Sezione**
 :  : FLD T$DESC  **Descrizione**
 :  : FLD T$CFSF  **Metodo costr.domande**
È un codice che, unitamente al parametro costruzione domande,  identifica il criterio con il quale le domande vengono aggiunte alla sezione. I possibili valori sono : 
- Blank Domande con Prefisso=Sezione
Vengono inserite nella sezione le domande il cui codice inizia con il codice della sezione stessa.
In questo caso il Parametro Costruzione Domande è lasciato vuoto
- 52    Definite in parametro
Le domande di questa sezione saranno scritte in un parametro della sezione stessa.
- 53    Con prefisso indicato
Vengono inserite nella sezione le domande che iniziano con il prefisso specificato nel campo seguente.
- 54    Da programma utente
L'utente può scrivere un programma che calcola le domande da inserire nella sezione. Il nome del pgm è inserito nel campo seguente
- F-    File
Le domande di questa sezione sono le intestazioni dei campi di un file. Il nome del file viene specificato nel campo seguente.
- T-    Tabella
Le domande di questa sezione sono le intestazioni dei campi di una tabella. Il nome della tabella viene specificato nel campo seguente.
- Q-    Questionario
Vengono inserite tutte le domande di un altro questionario.
Il nome del questionario viene specificato nel campo seguente.
- C-    Cat.parametri
Il testo delle domande inserite nella sezione è la descrizione dei parametri associati all'oggetto specificato nel campo seguente.
 :  : FLD T$CFSG  **Param. costr.domande**
Il contenuto di questo campo dipende dal valore del campo "Metodo costruzione domande". Fare riferimento alla sua documentazione.
 :  : FLD T$CFSH **Induzione dinamica**
Non più gestito.
Specifico quale programma chiamare per ottenere un aggiornamento nella struttura/risposte del questionario.
 :  : FLD  T$CFSA **Tipo ripetizione**
È un codice che indica il tipo di ripetizione. Se la sezione viene definita ripetibile, il campo seguente specifica il numero di ripetizione. I valori possibili sono : 
- Blank la sezione non è ripetibile
- N     la sezione è ripetuta n volte
- D     la sezione è ripetuta tante volte quante è indicato nella risposta della domanda specificata
 :  : FLD T$CFSB **Numero o Domanda**
Indica quante volte la sezione è ripetuta :  può contenere un numero o il codice di una domanda del questionario in cui la sezione si trova
 :  : FLD T$CFSC **Questionario Legato**
Indica il codice del questionario che viene incluso dalla sezione. Se la sezione è stata definita come ripetibile, si otterrà la possibilità di ripetere il questionario.
 :  : FLD T$CFSD   **Abilita desc.estese**
Abilita la visualizzazione delle descrizioni estese per la sezione e le domande che vi appartengono.
Le descrizioni estese sono dei testi che si possono associare ad ogni sezione e domanda del configuratore.
Sono delle descrizioni aggiuntive, per poter aiutare l'utente nella compilazione.
Le descrizioni etese di sezione sono poste o all'inizio o alla fine della sezione e prima o dopo ogni domanda.
Il testo è memorizzato nelle note strutturate.
Il contenitore per le sezioni è il TA;NSC;CFS
Il contenitore per le domande è il TA;NSC;CS
le 3 chiavi sono Tipo Questionario, Codice Questionario, Sezione/Domanda
Il capitolo è TA; NSICF; DPR per i testi che compaiono prima dell'oggetto e DPO per i testi che compaiono dopo l'oggetto.



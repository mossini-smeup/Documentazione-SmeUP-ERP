# B§P - Percorsi pgm client
 :  : DEC T(ST) K(B§P)
## OBIETTIVO
Permettere la costruzione di un percorso per collegare dati e/o programmi ad un oggetto, mediante il richiamo di un programma PC.
## CONTENUTO DEI CAMPI
 :  : FLD T$B§PD **Servizio/Nodo di rete**
Sono due codici che fanno riferimento a due tabelle.
È possibile utilizzare tali tabelle liberamente per le parti ripetitive dei percorsi. Possiamo ad esempio definire come "SERVIZIO" il percorso base di accesso a OFFICE.
 :  : FLD T$B§PA **Percorso**
È il percorso vero e proprio che si accoda alla parte precedentemente derivata da servizio e nodo di rete.
È possibile, sia digitare il percorso vero e proprio, che utilizzare una particolare sintassi che lo farà costruire dinamicamente sulla base dell'oggetto passato (un cliente, un articolo o un doc. della qualità).
Questa sintassi DEVE essere racchiusa tra parentesi quadre. Il programma B£IMM2 si occupa della traduzione.
Esistono 2 tipi di costrutti : 
- 1-Alias di un attributo :  la sintassi è [A.xxx.yy] dove xxx è un attributo dell'oggetto (es. I/13) e yy identifica l'elemento della tabella C£K, ossia il contesto dell'alias. Esempio [A.I/13.AT] verrà tradotto nella stringa '\Base_up\' se avrò fornito questa stringa come valore dell'alias identificato dalla coppia di oggetti che il contesto AT della C£K stabilisce.
Nel nostro esempio comparirà '\Base_up\' se il valore di I/13 dell'oggetto (il documento) in questione vale 'B£'.
L'elemento AT di C£K, infatti, lega il valore di un attributo di un oggetto (es. B£ ) ad un valore ** (es. la stringa '\Base_up\')
- 2-Valore di un attributo :  Esempio [V.xxx] dove xxx è un attributo dell'oggetto.
Il programma sostituirà alle parentesi quadre il valore dell'attributo dell'oggetto in questione.

È possibile utilizzare un Wizard che guidi nella costruzione della stringa desiderata. Questa procedura guidata si avvia digitando la stringa '[?]' o la stringa '[!]' in qualsiasi punto della riga.
 :  : FLD T$B§PB **Programma**
Può assumere i seguenti significati : 
-    *OAV
Concatenare l'attributo dell'oggetto specificato nel parametro. Ad esempio :  se per un articolo voglio utilizzare come immagine quella del suo gruppo distinta, dovrò indicare come parametro : 
I/05
-    *OAVSI
Concatenare il significato dell'attributo dell'oggetto specificato nel parametro. A differenza di *OAV verrà utilizzato il campo significato dell'attributo (descrizione) al posto del campo valore (codice)
Deve essere utilizzato qualora la lunghezza del campo superi i 15 caratteri
-    Programma
Un programma specifico che costruisce l'intero PATH.
Vedere il prototipo B£IMM1_00

# NSC - Scheletro Standard
## CONTENUTO DEI CAMPI
 :  : FLD T$KYC1 __Definizione chiavi di collegamento__
Una sigla che caratterizza una delle entità del sistema informativo.
Potremo ad esempio avere : 
AR = Articoli
CL = Centri di lavoro
.. = Ecc.
** = Codifica libera
 :  : FLD T$KYC2.T$KYC1 __Definizione chiavi di collegamento__
 :  : FLD T$KYC3.T$KYC1 __Definizione chiavi di collegamento__
 :  : FLD T$ARCH __Archivio che contiene le note.__
Specifica il codice dell'archivio che contiene i documenti caratterizzati da questo tipo contenitore. Esso deve essere
presente in tabella NSA e può essere un membro del file oppure una cartella di OFFICE
 :  : FLD T$AMKB __Ammesso codice bianco.__
È possibile inserire note per un codice bianco, in modo da poter costruire un insieme di NOTE ASSUNTE, quando si entra
per un dato codice.
 :  : FLD T$SSLD __S/S Lista distrib.__
Viene precisato il sottosettore della tabella NSL contenente la lista di persone a cui potrebbe essere distribuito
l'oggetto, precisato dalle tre chiavi prima definite.
 :  : FLD T$NSI1 __Tipo note__
È possibile indicare fino a 5 tipi di note valide per questo contenitore. Valgono in particolare i seguenti casi : 
A.   Nessun tipo specificato.
Tutti i valori presenti nella tabella NSI sono validi.
B.   Un solo valore specificato.
Tale valore è obbligatorio e viene assunto se non indicato.
C.   Elenco di valori.
Se il campo è bianco, si presenta un finestra dei soli valori ammessi, valori specificati come sottosettore del tipo
informazione (S/S Tipo Informaz.).
Mediante il carattere "*" è possibile indicare una scelta multipla. Immettendo, ad esempio, TA* intendo definire validi
tutti i capitoli che iniziano con TA.
 :  : FLD T$PGGS __Programma elaborazioni speciali__
Nel caso un codice sia '**' e ci sia specificato il nome del programma nel campo Pgm.gest.speciali, allora per la
decodifica del campo con codice '**' e/o per la gestione della risalita delle note strutturate (nel caso non ci siano
note con le tre chiavi precisate) si utilizzerà il programma precisato.
 :  : FLD T$PGLD __Programma Lista di Distribuzione__
Nel caso si vada a rispondere, nelle liste di distribuzione, riguardo ad un oggetto distribuito e si vogliano avere
maggiori dettagli sull'oggetto stesso.
Il programma di risposta a liste di distr. verifica se vi è precisato il programma. In caso affermativo lo chiama,
qualora l'utente voglia avere maggiori precisazioni sull'oggetto distribuito.
 :  : FLD T$NSCC __Conferma abbandono__
Se impostato a '1', in caso di uscita dall'editazione con il tasto F12 o F03, verrà presentata una finestra
di conferma di uscita senza memorizzazione. L'impostazione di questo campo condizionerà tutti i capitoli
(tabella NSI) gestiti per il contenitore. È possibile, inoltre, impostare questo comportamento a livello di
singolo capitolo, attraverso l'apposito campo presente nella tabella NSI
 :  : FLD T$NSCF __File appartenenza__
È un campo facoltativo ed indica in quale file saranno contenute le note gestite da questo elemento.
È necessario ricordare che il file in questione è NTSTRu0f, dove u=identifica il file. Inoltre il valore di
questo campo, se lasciato 'bianco', assume 'U' (il file di default quindi e NTSTRU0F)

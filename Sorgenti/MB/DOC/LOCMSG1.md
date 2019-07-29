Il componente messaggi si occupa della gestione dei messaggi : 
 F(01)
- inviati dal server e contenuti nell'xml in arrivo;
- prodotti direttamente dal client.


Ogni volta che un xml contiene degli elementi di tipo <Messaggio>, questi vengono elaborati dal componente che in base alle loro caratteristiche li visualizza e/o archivia. Inoltre, anche il client può sfruttare questo componente generando messaggi in questo modo : 

 F(01)
- UIMessageInfo vMsg = new UIMessageInfo (40, "Sorgente", "Descrizione breve", "Descrizione ampia");
- vMsg.showMessage(null);
- UIMessageController.getMsgManager().addMessage(vMsg); 


 F(02)
- Creo il messaggio chiamando il costruttore al quale passo i parametri adeguati 
- Mostro a video il messaggio tramite un JOptionPane 
- Aggiungo il messaggio al gestore dei messaggi 


Il messaggio mostrato è di tipo informativo e causa l'apertura di un JOptionPane contenente la "Descrizione breve" affiancata da un'icona diversa a seconda della gravità del messaggio.

## Come è fatto un messaggio
Un messaggio generico è composto da
 :  : PAR F(01) L(PUN)
- Tipo (£JaxMTyp)
-- _2_ I  = Visualizzano il messaggio e prevedono "OK" come unica risposta possibile per l'utente
-- _2_ C  = Visualizzano il messaggio e permettono all'utente di accettare ("OK") o rifiutare ("CANCEL") un'azione in corso
-- _2_ Q  = Visualizzano il messaggio e permettono all'utente di scegliere tra più funzioni possibili su cui cliccare
- Gravity (£JaxMGra) oggetto V2MSGRA : 
-- costante_2_ £Jax_GraInf  ('INFO')
-- costante_2_ £Jax_GraWrn  ('WARNING')
-- costante_2_ £Jax_GraErr  ('ERROR')
- Mode (£JaxMMod) oggetto V2MSMOD : 
-- costante_2_ £Jax_ModHH ('HH' Messaggio non visibile)
-- costante_2_ £Jax_ModTN ('TN' Notifica temporanea a scomparsa)
-- costante_2_ £Jax_ModPN ('PN' Notifica permanente da chiudere)
-- costante_2_ £Jax_ModPM ('PM' Messaggio modale)
- Testo (£JaxMTxt)
- TestoCompleto (facoltativo) (£JaxMTx2)


Qualsiasi tipo di messaggio tra quelli elencati memorizza la risposta nel campo Answer del messaggio stesso, permettendo di recuperare successivamente la risposta data (anche per necessità del programmatore, poichè al campo Answer corrisponde l'attributo Answer dell'oggetto UIMessageObject)

## L'archivio
Tutti i messaggi (visualizzati e non, di qualsiasi gravità) vengono archiviati ed è possibile visualizzarne lo storico tramite il menù di Loocup da Servizi --> Messaggi.
Ciò che appare è una tabella di gestione.
Ad ogni riga di tale tabella corrisponde un singolo messaggio con tutte le proprie caratteristiche e del quale si può vedere il dettaglio attraverso il doppioclick sulla cella relativa alla descrizione.
La toolbar sottostante permette di eliminare uno o tutti i messaggi contenuti, di visualizzare tutti i messaggi o solamente quelli relativi all'ultimo xml ricevuto e di accedere a questa documentazione.

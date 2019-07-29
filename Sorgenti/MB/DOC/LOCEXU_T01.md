# PREMESSA
L'obiettivo è rendere un servizio di aggiornamento utile per la maggior parte delle matrici di visualizzazione che presentano i dati trattati dal servizio.
Ad esempio, un servizio di aggiornamento su BRARTI0F deve poter funzionare su tutte le matrici di visualizzazione che contengono campi del BRARTI0F trattati dal servizio stesso.

Dal momento che il legame tra campi trattati da un matrici di aggiornamento EXU e campi visualizzati in matrici di visualizzazione EXB è costituito dal nome delle colonna nelle matrici di visualizzazione è buona norma, per il futuro, assegnare nomi di colonne standard nelle matrici di visualizzazione.
In questo modo, ad esempio, un servizio di aggiornamento che tratta i campi di un file di Sme.up (es. BRARTI0F) riesce a funzionare in tutte le matrici che dichiarano le proprie colonne come campi dello stesso file.

Un servizio di aggiornamento potrebbe gestire anche : 

- Campi di tipizzazione dei campi con tipo variabile, in modo da abilitare la corretta navigazione in Loocup anche su questi ultimi
- Campi di descrizione

quindi è opportuno standardizzare anche la nomenclatura di tipo e descrizione del campo di un file.
In definitiva : 

- Se una colonna di matrice rappresenta un campo di un file va chiamata con il nome del campo (esempio :  T§CDCL)
- Se la colonna rappresenta la tipizzazione di un campo di un file il nome del campo va preceduto dal suffisso "$_" (esempio :  $_T§CDCL, valorizzato con 'CNCLI' piuttosto che 'CNFOR')
- Se la colonna rappresenta la descrizione di un campo il nome del campo va preceduto dal suffisso "£_" (esempio :  £_T§CDCL, valorizzato con 'Mario Rossi')


# Collegamento a una matrice EXB
Per associare l'esecuzione di un servizio di aggiornamento a una matrice di visualizzazione in una scheda è sufficiente agire su alcuni parametri dell'istruzione G.SET.MAT nello script della scheda stessa.
I parametri minimi da impostare sono : 

- ReadOnly="No"
- UpdSvc="Nome del servizio di aggiornamento"


Altri parametri utili per specificare il funzionamento del servizio sono : 

- UpdPar, libero per passare parametri o variabili utili per l'esecuzione del servizio. Se una matrice non contenesse tutti i campi necessari al servizio per costruire la chiave al record che deve aggiornare i campi mancanti dovrebbero essere passati qua, ad esempio come UpdPar="KEY1(valore) KEY2(valore)"
- DeferUpd (default "No") :  se impostato a "Yes" chiama il servizio di aggiornamento solo quando l'utente clicca con il pulsante destro sul tab della subsezione in cui è contenuta la matrice e sceglie "Salvataggio dati", passando a quel punto tutte le Line relative alle righe modificate dall'utente. Se impostato a "No", invece, effettua automaticamente una chiamata all'aggiornamento quando l'utente preme Invio o doppio clic oppure quando si sposta in verticale tra le righe della matrice.


# CLI -  LISTENER DI CASELLA DI POSTA IMAP
Implementa un ascoltatore di caselle di posta IMAP in grado di reagire all'arrivo di una mail

## Il codice del listener
Il codice di questo listener è 07

## Cosa fa
Il listener ogni intervallo stabilito nella definizione dei listener controlla il contenuto di una casella di posta IMAP e, se rileva l'arrivo di nuove mail, emette un evento per ogni nuovo messaggio

## Che struttura dati passa al server AS
Il listener genera una funzione F(EVT; < nome servizio > ; < nome metodo >) P(From( < mittente > ) Subj( < oggetto mail > )LISTENER( < codice listener >). Fatto questo legge l'XML che viene tornato dall'AS e reagisce di conseguenza.
Nel caso non si definisca il metodo nella definizione del listener di default verrà utilizzato MSG.ADD, quindi la funzione sarà F(EVT; < nome servizio > ; MSG.ADD) P(From( < mittente > ) Subj( < oggetto mail > )LISTENER( < codice listener >)
## I parametri specifici
Oltre a gestire i parametri generali dei listener Loocup per i quali si rimanda alla documentazione in
- [Listeners di Loocup](Sorgenti/MB/DOC_OGG/V3_CLI)
il listener 07 gestisce anche i seguenti parametri riportati nel campo Parameter : 

- Poll :  definisce il tempo di polling con cui viene scatenato il giro
- Echo :  emette una finestra che comunica l'invio all'AS l'arrivo del messaggio. Se il valore è 1 la visualizza
- Server :  server imap a cui si collega
- Account :  casella di posta da controllare
- Pass :  password di autenticazione
- Folder :  Cartella IMAP da controllare (generalmente INBOX)


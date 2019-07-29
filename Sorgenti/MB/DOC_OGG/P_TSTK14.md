
## Funzioni / Metodi
### NTF   Funzioni su notifica (tipo record ' ')
I record con tipo record ' ' sono le notifiche vere e proprie. Contengono il contatore di un tipo notifica.
* **INZ  ** Inizializza record (riceve tipo notifica, destinatario)
* **WRI  ** Scrive (controlla tipo record ' '; restituisce IDOJ)
* **RESET** Azzera (riceve tipo notifica, destinatario)
* **ADD  ** Incrementa (riceve tipo notifica, destinatario)
* **SUB  ** Decrementa (riceve tipo notifica, destinatario)
* **UPD  ** Aggiorna (da IDOJ; controlla tipo record ' ')
* **DEL  ** Cancella (da IDOJ; controlla tipo record ' ')
* **DELALL** Cancella tutte le notifiche di un tipo (riceve tipo)
### COS   Info costruzione (tipo record 'C')
I record con tipo record 'C' contengono le informazioni relative a quando è stato costruito l'ultima volta un tipo notifica pull dal LOA60_LM.
* **WRI  ** Scrive info costruzione (riceve tipo notifica; restituisce IDOJ
* **DEL  ** Cancella info costruzione (riceve tipo notifica)
### RIG   Funzioni su singola riga (tipo record 'S')
I record con tipo record 'S' contengono delle righe singole. Servono come record di appoggio quando un tipo notifica non calcola la numerosità a partire da un file di database specifico.
* **INZ  ** Inizializza record (riceve tipo notifica)
* **WRI  ** Scrive   (controlla tipo record 'S'; restituisce IDOJ)
* **UPD  ** Aggiorna (da IDOJ; controlla tipo record 'S')
* **DEL  ** Cancella (da IDOJ; controlla tipo record 'S')
* **DELUTE** Cancella righe per tipo notifica e destinatario
### ESE   Funzioni di esecuzione (riceve tipo notifica, destinatario)
* **MAIL ** Invia notifica via mail
* **APP  ** Invia notifica ad app mobile
Se un tipo notifica è push (attributo Cos="" nel tag A60.COS dello script LOA60_xx) all'incremento/diminuzione di un tipo notifica vengono eseguite anche la ESE/MAIL e la ESE/APP (in base a quanto configurato nello script LOA60_xx).
Nel caso di notifiche pull (generate dal costruttore il cui suffisso è specificato nell'attributo Cos="xx" nel tag A60.COS dello script LOA60_xx) è invece necessario eseguire esplicitamente le funzioni di esecuzione nel costruttore stesso.

## Parametri di input
### Tipo Notifica (£K14I_TN)
Tipo notifica (SESUB.A60) che corrisponde ad una subsezione di uno script LOA60_xx di SCP_SET.
### Destinatario  (£K14I_DT)
Utente (TAB£U) destinatario della notifica.
### Idoj          (£K14I_ID)
Idoj dei record da aggiornare / cancellare quando usato.
### Azienda       (£K14I_AZ)
Se non passata viene assunta dall'ambiente tramite £G00.

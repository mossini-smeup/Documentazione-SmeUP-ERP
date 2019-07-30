 :  : HEA RESP(LS) STAT(00) USAG(LS) DTAG(20060113)
# OBIETTIVO
Facilitare all'utente la scrittura di una condizione dove sono presenti variabili e operatori logici. In particolare è possibile
-	Eseguire un controllo sintattico sulla condizione quali ad esempio la congruenza delle parentesi
-	ricercare le variabili e gli operatori

# OPEN e NOTE PROVVISORIE
### Modo operativo
Tutte le funzioni sono implementate dal servizio B£SER_17
Il client al bottone controllo sintattico chiama RUL.VER
Il servizio verifica esistenza caratteri di ricerca (! oppure?)
Se presenti costruisce la nuova funzione che deve essere chiamata. RUL.OGG dello stesso servizio con il carattere - negli oggetti da ricercare.
Il client, se presente il carattere - lancia la funzione stessa che finirà per portare al server la risposta
Il server sostituisce la risposta al posto del carattere e rifornisce la stringa della condizione
Il client la presenta e consente di procedere.

Ad ogni enter abbiamo il controllo
Al tasto F6 associamo la conferma, che restituisce il contenuto al richiedente di origine

### Idee di sviluppo
- Potremmo attaccare la scheda della regola dove ci sono traduzione ecc. ecc.
- Mettere icona dell'oggetto J1 RUL, J1 FUN, V3 ASE B£SER17
-

# FUNZIONI/METODI


 :  : PRO.SER Cod="RUL.VER.1" Tit="Regole. Verifica correttezza formale" Fun="F(EXB;B£SER_17;RUL.VER)"

 :  : PRO.SER Cod="RUL.OGG.2" Tit="Regole. Richiesta oggetto di ricerca" Fun="F(EXB;B£SER_17;RUL.OGG)"


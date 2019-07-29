### Cella J4BTN


Con la nuova versione di Looc.UP "Le Vele" sono state aggiunte le nuove celle di matrice di tipo "J4BTN".
Queste celle vengono disegnate come icone interne alla matrice, al click sulle quali viene eseguita un fun.
Per utilizzare è sufficiente definire nella griglia una colonna con il tipo di oggetto "J4BTN".
Nelle righe, alla cella corrispondente, il valore dovrà essere composto da

Tipo Icone;Parametro Icona;Codice Icone;Testo;Funzione da lanciare al click.

Ad esempio : 

VO;COD_SOS;00111;Apri;F(EXD;*SCO;) 1(CN;CLI;123) G(NFIR)

Grazie a queste celle sarà possibile eseguire una fun (definita in linea direttamente dal servizio) senza dover definire un dinamismo (che in questi casi spesso necessitava dell'enable), disaccoppiando la scheda dal servizio.
Inoltre, il controllo della funzione da eseguire e dell'icona da emettere è molto più puntuale, perchè la logica è tutta nel servizio.

Ovviamente ci possono essere più colonne J4BTN nella stessa matrice.

L'oggetto è definito nel client, quindi non necessita di aggiornamenti della DEV, ma solo di Looc.UP.



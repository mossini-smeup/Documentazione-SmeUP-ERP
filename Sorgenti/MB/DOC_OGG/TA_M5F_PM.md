## Parametri
>Se l'origine è PM (parametri)
Parametro 1 : 
-    Pos.1/3   Categoria parametri (elemento della tabella C£E) :  la griglia che
.              definisce i due campi chiave dei parametri deve essere
.              obbligatoriamente '£P3' (magazzino/articolo).
-    Pos.4/6   Valore parametro (elemento della tabella B£N del sottosettore
.              presente nella categoria). In questo parametro devono essere
.              obbligatori la gestione delle quantità e lo sviluppo per date.
.              Questo parametro può prevedere o meno un oggetto (con eventuale
.              sviluppo multiplo).
.              Nel primo caso, se è un oggetto che costituisce un filtro per la
.              disponibilità, e se esso è diverso da quello ricevuto, la fonte non
.              viene considerata (ad esempio, se è una configurazione diversa
.              dalla configurazione ricevuta). Se, inoltre, l'oggetto è tipizzato
.              (ente o risorsa) il parametro viene trascurato se il tipo è diverso da
.              quello  ricevuto (ad esempio, se si imposta un parametro multiplo per
.              cliente, e  l'analisi disponibilità passa il tipo ente 'fornitore',
.              anche senza passare un fornitore specifico).
.              Se, al contrario, il parametro non ha oggetto, oppure se l'oggetto
.              non è un filtro della disponibilità, vengono ritornati i valori,
.              sviluppati per data, del primo elemento trovato.
-    Pos.7     Modalità trattamento blanks. Con questa impostazione viene deciso il
.              modo di trattare i parametri con oggetti che sono filtro della
.              disponibilità, quando l'oggetto ricevuto è blanks.
.              -- ' ' Trattamento blanks dettagliato. Vengono ritornati, in
.                     successione, i valori di tutti i parametri sviluppati per data
.                     ciascuno con il proprio oggetto.
.              -- '1' Trattamento blanks specifico. Vengono ritornati solamente
.                     i valori, sviluppati per data, del parametro il cui oggetto è
.                     blanks, se esso è presente
-    Pos.8     -- ' ' se considerare come data fonte la data di fine intervallo.
.              -- '1' se considerare come data fonte la data di inizio intervallo.
-    Pos.9     -- ' ' se considerare tutti i periodi.
.              -- '1' se considerare solo i periodi con data inizio intervallo
.                     maggiore di oggi.
.              -- '2' se considerare solo i periodi con data inizio intervallo
.                     maggiore o uguale a oggi.
.              -- 'A' se considerare solo i periodi con data fine intervallo
.                     maggiore di oggi.
.              -- 'B' se considerare solo i periodi con data fine intervallo
.                     maggiore o uguale a oggi.


## Parametri
>Se l'origine è PM (parametri) : 
Parametro 1 : 
>Pos.1/3 :  Categoria parametri (elemento della tabella C£E) :  la griglia che
.              definisce i due campi chiave dei parametri deve essere
.              obbligatoriamente '£P3 (magazzino/articolo).
>Pos.4/6 :  Valore parametro (elemento della tabella B£N del sottosettore presente
.              nella categoria). In questo parametro deve essere obbligatoria la
.              gestione delle quantità e non essere attivo lo sviluppo per date.
.              Questo parametro può prevedere o meno un oggetto (con eventuale
.              sviluppo multiplo). Nel primo caso, se è un oggetto che costituisce
.              un filtro per la disponibilità, e se esso è diverso da quello
.              ricevuto, la fonte non viene considerata (ad esempio, se è una
.              configurazione diversa dalla configurazione ricevuta). Se inoltre
.              l'oggetto è tipizzato (ente o risorsa), il parametro viene trascurato
.              se il tipo è diverso da quello ricevuto (ad esempio, se si imposta un
.              parametro multiplo per cliente, e l'analisi disponibilità passa il
.              tipo ente 'fornitore', anche senza passare un fornitore specifico).
.              Se il parametro non ha oggetto, oppure se l'oggetto non è un filtro
.              della disponibilità, viene ritornato il suo valore, o la la somma di
.              tutti i suoi valori (se multiplo), senza alcun controllo.
>Pos.7 :    Modalità trattamento blanks.
.              Con questa impostazione viene deciso il modo di trattare i parametri
.              con oggetti che sono filtro della disponibilità, quando l'oggetto
.              ricevuto è blanks.
.              - ' '  Trattamento blanks dettagliato :  vengono ritornati, in
.                     successione, i valori di tutti i parametri, ciascuno con il
.                     proprio oggetto.
.              - '1'  Trattamento blanks specifico :  viene ritornato solo, se presente,
.                     il valore del parametro il  cui oggetto è blanks.
.              - '2'  Trattamento blanks totalizzato :  viene ritornata la somma dei
.                     valori di tutti i parametri.


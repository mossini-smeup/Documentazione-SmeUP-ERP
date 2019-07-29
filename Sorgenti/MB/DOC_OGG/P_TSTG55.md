# GESTIONE AVANZATA COSTI
## OBIETTIVI
Ritornare il costo o un elemento di costo o una riclassifica di costo di un oggetto.
Nel caso in cui nel tipo costo richiesto sia specificato un tema legge i costi nell'archivio D5COSO0F, altrimenti
richiama la £G17 (che legge i costi dal COSAR00F)
Funziona anche come interfaccia dell'archivio D5COSO0F.
## FUNZIONI/METODI (£G55FU/£G55ME)
### LET
Lettura
    -     -
Costo di un oggetto.
### D5C
Un record del D5COSO.
### INT
Interrogazione costo tramite modulo D0.
### CONTESTO (£G55CO)
E' un campo che specifica il tipo + parametro dell'oggetto interessato e che deve essere presente nella tabella D5S.
Un esempio potrebbe essere DRBOF (oggetto tipo DR e parametro BOF.)
### OGGETTO (£G55OG)
E' il codice dell'oggetto interessato (ha tipo-parametro specificato nel contesto).
### TIPO COSTO / TEMA (£G55TC)
Nel caso in cui il metodo non sia D5C indica il tipo costo (tabella TCO) che interessa, altrimenti indica il tema del
D5COSO (tabella D5O con sottosettore specificato nella tabella del contesto (D5S)).
Se non viene riempito viene preso come tipo costo il Tipo costo assunto 1 presente nella tabella CS1.
### LIVELLO (£G55LV)
E' un elemento della tabella D0B che rappresenta una riclassifica delle componenti di costo.
### ELEMENTO IGI (£G55EI)
E' un elemento della tabella IGI (sottosettore specificato nel tema). Serve nel caso serva una componente di costo (o
un elemento del D5COSO nel caso del metodo D5C) ben specificata.
### NATURA COSTO (£G55NC)
E' un elemento della tabella D0A
La natura permette di aggregare le componenti di costo. Ogni componente di costo (cioè ogni elemento della IGI nel
caso in cui i costi siano salvati nell'archivio D5COSO) può avere una natura associata la quale può avere una natura
collegata.
La /COPY restituisce la somma di tutti i valori che hanno la stessa natura o natura collegata.
Si può specificare se bisogna considerare gli elementi singoli della tabella IGI o le sue riclassifiche (elementi che
iniziano per A o per B) mettendo o *blanks o 'A' o 'B' nel campo Elemento
### IGI (£G55EI).
Esempio : 
Natura    Descrizione              Natura collegata
ME        Montaggio elettrico      MM
MM        Manodopera montaggio     MD
MD        Costo manodopera
MI        Manodopera indiretta     MD
Supponendo di volere il costo del montaggio elettrico si dovrà interrogare per natura ME (ovviamente dovranno esistere
nella tabella IGI degli elementi con natura costo uguale a ME).
Se invece si volesse sapere il costo della manodopera si interrogherà per natura MD e la /COPY sommerà tutti gli
elementi che avranno come natura costo o MD o MM o ME o MI (bisogna stare attenti ad eventuali doppi valori).
La catena delle nature collegate può essere lunga a piacere.
### PERIODO (£G55PE)
E' un elemento della tabella PER. E' il periodo di validità del costo.
### DATA (£G55DT)
E' la data di validità del costo.
## Attenzione
Viene effettuata la seguente risalita : 
Se costo salvato per periodo (vedi tabella D5O dei temi)
1. periodo specificato
2. dalla data risale al periodo (il tipo periodo è specificato nel tema)
3. eventuale periodo di default specificato nella tabella TCO
Se costo salvato per data (vedi tabella D5O dei temi)
1. data finale del periodo specificato
2. data specificata
3. data finale dell'eventuale periodo di default specificato nella tabella TCO
### BLOCCA RISALITA (£G55BR)
Se impostato non viene effettuata la risalita sul tipo costo assunto specificato nella tabella TCO.
### ALTRE CONDIZIONI (£55T,£55P,£55O)
E' possibile passare fino a 10 tipi (£55T), parametri (£55P) e codici (£55O) che verranno utilizzati per riempire la
chiave del
D5COSO nel caso in cui il tema del D5COSO abbia anche delle sottochiavi (per esempio un costo articolo memorizzato per
configurazione o per cliente).
La sequenza di riempimento delle schiere è ininfluente.
## VALORI RESTITUITI
Il singolo valore richiesto nel campo £G55CS
Il dettaglio delle componenti di costo nella schiera £55D
L'eventuale chiave del record in £G55FC
Il significato dei valori nella schiera £55S
## CONSIDERAZIONI
Per la restituzione del valore £G55CS viene seguita la seguente gerarchia
1. elemento IGI specificato
2. natura costo specificata
3. livello di costo specificato (presente in D0B)
4. elemento con natura costo uguale a
TC se livello non passato
T1 se livello passato uguale a 1
T2 se livello passato uguale a 2
T3 se livello passato uguale a 3
T4 se livello passato uguale a 4
T5 se livello passato uguale a 5

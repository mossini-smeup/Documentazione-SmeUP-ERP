## Quantità giornaliera
Se l'origine è QG (quantità giornaliera)
Questa fonte (di tipo metafonte in quanto elabora un gruppo fonti) ritorna dati sintetici giornalieri, selezionati in base al tipo filtro che la caratterizza.
Si assume che tale fonte sia futura, ma può ritornare anche fonti implicitamente 'presenti', vale a dire con data a zero, (ad esempio in presenza di giacenza o scorta minima nel gruippo fonti).
>Parametro 1 : 
-    Pos.1/10  Gruppo fonti per calcolare la copertura giornaliera.
Parametro 2 : 
-    Pos.1     Tipo filtro
.              'A' - Fabbisogno lordo :  Per ogni giorno in cui vi sono fabbisogni
.                    (eventi con quantità negativa) ne viene ritornata la somma,
.                    cambiata di segno.
.              'B' - Fabbisogno netto :  Per ogni giorno viene calcolata la somma
.                    delle quantità degli eventi :  se essa è negativa, viene
.                    ritornata cambiata di segno.
.              'C' - Copertura lorda :  Per ogni giorno in cui vi sono coperture
.                    (eventi con quantità positiva) ne viene ritornata la somma.
.              'D' - Copertura netta :  Per ogni giorno viene calcolata la somma delle
.                    quantità degli eventi :  se essa è positiva, viene ritornata.
.              'E' - Eventi lordi :  Vengono ritornate, per ogni giorno, se presenti,
.                    la copertura lorda ed il fabbisogno lordo (con segno -)
.              'F' - Eventi netti :  Per ogni giorno in cui c'è variazione di
.                    disponibilità viene ritornata tale variazione, con segno + se
.                    è un incremnento e con segno - se è un decremento.
.                    Tale fonte è l'insieme delle coperture nette e dei fabbisogni
.                    netti (cambiati di segno), in quanto nello stesso giorno ci può
.                    ci può essere solo uno dei due.
.                    La disponibilità che viene ritornata con questa fonte è la
.                    disponibilità puntuale, in ogni giorno in cui essa subisce
.                    variazioni.
.              'G' - Disponibilità puntuale :  Per ogni giorno in cui c'è variazione
.                    di disponibilità viene ritornato il valore (con segno) della
.                    disponibilità a fine giornata.
.                    Tale valore è ottenibile, come 'effetto collaterale' anche con
.                    il filtro 'E', ma solo con questa impostazione è possibile
.                    comprendere l'andamento della disponibilità in un unico servizio
.                    che tratta sempre la quantità dell'evento £M5DQT).
-    Pos.2     Filtro disponibilità
.              ' ' - Nessuno
.              '+' - Positiva
.              '-' - Negativa
.              Vale solo per il tipo filtro 'G'.
.              Se impostato, verrà rispettivamente ritornata solo la parte non
.              negativa o non positiva dell'andamento della disponibilità.
.              Se vi sono più giorni consecutivi in cui la quantità e a zero (perchè lo
.              è realmente oppure perchè è stata forzata a tale valore, esssendo
.              esterna al filtro), viene riportato solo il primo giorno.
-    Pos.3     Suddivisione per oggetto di rottura. Se impostato, se la
.              pianificazione è impostata per codice di rottura e l'articolo è
.              pianificato a rottura, viene eseguito il calcolo separato per ogni
.              oggetto di rottura (che viene ritornato dalla disponibilità nel campo
.              predisposto :  commessa, configurazione, ecc..)


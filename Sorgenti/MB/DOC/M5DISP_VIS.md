# Stampa disponibilità
Si può impostare un gruppo fonti oppure scegliere le fonti una ad una in modo specifico per ogni lancio.

## Forme previste
 * **Dettaglio per data**; viene riportato ogni evento, prima le fonti attuali (ordinate per il parametro di ordinamento della tabella), poi quelle future (ordinate per data e parametro di ordinamento)
 * **Dettaglio per fonte**; come dettaglio per data, ordinata però per fonte (parametro di ordinamento della tabella) e all'interno di ogni fonte per data
 * **Riepilogo per giorno**; viene riportata una riga per ogni giorno e all'intero per fonte
 * **Riepilogo per fonte**; viene riportata una riga per ogni fonte
 * **Sintesi per giorno**; viene riportata una riga per ogni giorno
 * **Sintesi per articolo**; viene riportata una riga per ogni articolo

Per eseguire la stampa occorre avere nella B£Q_AR l'elemento £01 così impostato
>Set. B£Q FORME DI RAPPRESENTAZIONE      Sub. AR FORME STAMPA PER ARTICOLI
Ele. £01                                                           Archivio 0
Descrizione          Stampa disponibilità                          Attr.Vis
Obbl/Prot/Non vis 01
"                 02
"                 03
"                 04
"                 05
"                 06
"                 07
"                 08
"                 09
"                 10
Programma specifico  M5SD01S            DISP Stampa Analisi Disponibil
Programma richiesta  M5SD01G            DISP Stampa Analisi Disponibil
Programma ordinam.
Obblig.conferma                         NO
Rimane dopo inserim.                    NO
Livello protezione   89                 STATO 90


**Nota Bene**; ricordo che qualora si voglia far apparire sempre una riga di una fonte esistente (anche se = 0), tipicamente una giacenza, basta impostare il flag apposito (T$M5EF    Presenta anche se 0) nella tabella della fonte.

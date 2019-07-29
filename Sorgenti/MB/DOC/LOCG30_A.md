## Informazioni generali
Il modulo questionario gestisce la compilazione di questionari di vario tipo e di varia provenienza.
Con questionario si intende un insieme di domande, suddivise in una o più sezioni.

## Tipizzazione
Un questionario è un oggetto SmeUp di tipo RE.

 :  : R01 Scheda di riferimento è CFBASE

 :  : PAR T(Classificazione SmeUp dei questionari) F(01)


- Q- :  questionari standard, con o senza regole, in cui le risposte vengono fornite partendo dalla prima sezione e proseguendo fino all'ultima
- T- :  questionari per la manutenzione delle tabelle sono mono sezione, tranne nel caso in cui ci siano i dati utente da definire (F15 attivo)
- L- :  questionari di tipo setup :  sono script che vengono salvati nella file SCP_CFG (mono o multi sezione).
- U- :  questionari in cui la struttura delle domande o non è definita in uno script oppure è ottenuta estraendo da uno script una parte.
- S- :  questionari le cui risposte definiscono un setup per un programma AS400. Tali questionari sono definiti in uno script e divisi per sezioni. Il nome del questionario è composto dal nome del modulo concatenato con / concatenato con il nome della sezione.

 :  : PAR T(Forma di presentazione dei questionari - TIPO) F(01)


- Mono sezione :  sono questionari composti da una sola sezione. Tipico esempio sono i questionari creati per la manutenzione tabelle (RE-T-)
- Forma a tab :  sono questionari composti da 1 a n sezioni. Le regole non sono gestite. L'utente può decidere da quale sezione cominciare la compilazione in quanto non esiste un ordine prestabilito
- Forma a albero :  sono questionari in cui l'inserimento delle risposte avviene partendo dalla prima sezione visibile e procede fino all'ultima sezione. se sono presenti regole, queste vengono valutate o al cambio di sezione o nel momento in cui viene fornita una risposta.


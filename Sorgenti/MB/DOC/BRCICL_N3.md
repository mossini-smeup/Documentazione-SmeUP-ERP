# Modalità scansione ciclo del documento
La scansione del ciclo del documento è richiamata in 2 modi : 
 - scansione ciclo per ritorno operazioni (con ereditarietà al ciclo articolo)
 - scansione per copia dal ciclo articolo a quello del documento

In tutto le possibili scansioni sono 3 : 
 * **scansione documento** :  si esegue una scansione di produzione con le sole operazioni valide (stato blank)
 * **scansione articolo per ritorno operazione** :  si esegue una scansione di produzione con le sole operazioni valide (stato blank) e, come ciclo, il ciclo impostato nell'ordine di produzione (se è una riga V5 non si può fare perchè l'informazione manca)
 * **scansione articolo per copia in ciclo documento** :  si imposta sempre il ciclo contenuto nell'ordine di produzione, ma si imposta di ritornare tutti gli stati (con "*" nello stato di input)

In questo modo si ottiene che : 
 * nella scansione del ciclo ereditata dall'articolo si hanno solo le fasi valide (del ciclo impostato)
 * nella costruzione del ciclo dell'ordine si hanno tutte le fasi del ciclo impostato
 * nella scansione del ciclo dell'ordine si hanno solo le fasi valide . Per variare le fasi valide del ciclo di un documento, si entra in variazione e si attivano / disattivano le varie operazioni modificando gli stati :  infatti nel ciclo del documento esistono tutte le operazioni (attive e inattive).

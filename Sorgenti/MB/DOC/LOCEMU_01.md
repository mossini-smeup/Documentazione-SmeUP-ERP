## Associazione di funzioni ad un formato video
Si crea un campo video nascosto W$£FUN, lungo 1024, in cui si scrivono tag XML che daranno origine a bottoni con chiamate a funzioni di Looc.up.
I tag XML, scritti consecutivamente nel campo, sono : 
**Oggetto Testo="Descrizione" Exec="F(TRE;*LIS;) 1(ST;;D5S)" i="M11"**
dove
**Testo** contiene la descrizione che compare sul bottone in Looc.up
**Exec**  contiene la chiamata alla funzione di Looc.up
**i** (opzion.) specifica un'icona diversa da quella standard da associare al bottone in Looc.up; tale icona deve essere contenuta nella sottodirectory Looc.up_ICO di Looc.up

E' possibile gestire le forzature di un sibfile tramite il pgm funizzato B£UT25B funzione DET,
deve ricevere come oggetto 1 il video

Il contenuto del campo W$£FUN può essere aggiornato dinamicamente anche in base al contenuto di altri campi del video.

Un esempio di questa tecnica è contenuto nel programma D5CO03L.

## Funzione LOOC.up dall'interno di un programma RPG
In modo analogo a quando si emette un formato video (comando EXFMT) è possibile richiedere il richiamo di una funzione. Ciò è stato ottenuto estendendo i codici operativi del sistema (WRITE, UPDATE, READC, ecc) con nuovi codici operativi (ovviamente validi solo in ambiente LOOC.up e con i seguenti significati : 

- **WRLOO (Esecuzione semplice)** :  La funzione richiesta e l'emulazione lanciata funzionano in modo indipendente, l'emulazione in questo caso è ferma fintanto che non premo un tasto.
- **EXLOO (Esecuzione modale)** :  La funzione viene eseguita ed il controllo passa alla finestra LOOCUP, quindi l'emulazione rimane bloccata fino a che non ritorno dalla funzione lanciata
- **RELOO (Esecuzione e ritorno)** :  La funzione viene eseguita ed il controllo torna automaticamente  all'emulazione, senza il bisogno di interazione.


 :  : DEC T(OJ) P(*PGM) K(JAEMU1)

## Chiamare un programma non "funizzato"
Usare il programma funizzato B£FU01X passando come parametro il comando CALL PgmXXX e i suoi parametri

## Funzione da lanciare al termine del programma (RFunction)
 :  : DEC T(OJ) P(*PGM) K(JAEMU1)

![LOCBAS_038](http://localhost:3000/immagini/LOCEMU_01/LOCBAS_038.png)
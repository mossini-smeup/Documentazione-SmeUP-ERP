 :  : PRO Cod(A01) Txt(Introduzione) STAT(00) RESP(BUFSIL)

 :  : ATT Cod(001) Txt(Aprire la propria UPP)  STAT(10) RESP(LANSIL)
01. Accedere a Smeup con una libreria personale (W_nomeutente)
Assumiamo di essere sul sistema di sviluppo.
Abitualmente esiste fra gli ambienti quello che chiamiamo SVIU (Sviluppo + libreria personale)

02. In SpotLight digitare "UPP"
Comprendere tutto delle funzioni di ricerca e individuazione di una UPP
La UPP di gestione delle UPP è l'oggetto SU A£_001
Il menù che appare è quello dell'uso di tale UPP
 :  : DEC T(J1) P(FUN) D(A.Gestire le UPP) K(F(EXD;*SCO;) 1(SU;;A£_001) INPUT(SU_Sub(CO)))

03. Provare e capire tutte le forme di ricerca

04. Accedere alla UPP A£_001 sia come utilizzatore che come gestore
La modalità di accesso sarà in modifica nel prossimo periodo

05. Creare una "UPP Personale" (Nel menù della UPP o con apposito comando in lista
Verrà creata una UPP dal nome A£_USR nella propria libreria

06. Se l'ambiente comprende la propria libreria dovrà apparire una UPP dal nome A£_USR

07. Accedere alla gestione della UPP come gestione e come utilizzo

08. Cambiare la descrizione della UPP (Assume il proprio nome)
Si consiglia di assegnare un nome che consenta di identificare la UPP e contemporaneamente che la UPP è per i propri esercizi

 :  : ATT Cod(002) Txt(Gestire la propria UPP)  STAT(10) RESP(LANSIL)
01. Accedere a "Copertura funzionale"
In copertura funzionale scegliere il + su scheda

02. Arire le fonti che interessano
Filtrare la classificazione A/B/C scegliendo A
Aprire (icona +) le fonti che interessano

03. Ritornare alla scelta UPP
03.A  Scegliere Usare la UPP
03.B  Vedere la scheda modello che si presenta
Il modello è come per tutte le fonti la scheda della UPP Sketch (A£_000)

 :  : ATT Cod(003) Txt(Modificare i dati della propria UPP)  STAT(10) RESP(LANSIL)
01. Nel menù di gestione scegliere "modifica"
02. Comprendere tutte le caratteristiche
03. Verificare l'effetto di tali modifiche

 :  : ATT Cod(004) Txt(Assegnare le responsabilità)  STAT(10) RESP(LANSIL)
01. In "Sviluppare" scegliere "Proprietà UPP"
Assegnare le responsabilità.
Nella UPP per la gestione delle UPP è indicato come assegnare le responsabilità definendo i collaboratori. Ad ognuno potrò assegnare un ruolo (usa l'Wizard per i valori ammessi)
02. Verificare il risultato scegliendo "Controllo responsabili"
03. Scegliendo un responsabile verificare le sue possibilità

 :  : PRO Cod(A02) Txt(Le variabili) STAT(00) RESP(BUFSIL)
 :  : ATT Cod(001) Txt(Modificare le variabili)
Entrare in gestione variabili e assegnare una qualsiasi variabile con identificazione del valore assegnato e della sua classe
 :  : ATT Cod(002) Txt(Vedere l'effetto della definizione di una variabile)

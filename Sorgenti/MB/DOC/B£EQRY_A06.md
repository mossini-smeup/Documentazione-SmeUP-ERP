# Generalità

Una query di ricerca può essere utilizzata in una scheda qualsiasi. Il suo richiamo può avvenire tramite le funzionalità del modulo LOSUIR, attraverso l'utilizzo delle istruzioni G.SUB.UQR, G.SET.UQR, e D.FUN.UQR.

Attraverso tali funzionalità inoltre possibile applicare alla query, setup e dinamismi, definiti localmente nella scheda specifica.

Per un maggiore dettaglio si rimanda alla scheda del modulo LOSUIR.

 :  : DEC T(TA) P(B£AMO) K(LOSUIR)

# Accesso da un oggetto tramite SQL

Differente discorso vale qualora si voglia accedere ad un oggetto semplicemente utilizzando l'SQL. In questo caso si danno i seguenti consigli operativi : 
* Di basare sempre l'accesso sql, riprendendo i dati di riferimento restituiti dalla /COPY £IVD
* Sfruttare le funzionalità della /COPY £SQLD piuttosto che eseguire le istruzioni SQLRPGLE in loco

 :  : DEC T(MB) P(QILEGEN) K(£IVD) L(1)
 :  : DEC T(MB) P(QILEGEN) K(£SQLD) L(1)


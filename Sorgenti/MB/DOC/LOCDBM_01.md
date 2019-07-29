# Introduzione
Il modulo LOCDBM e' stato pensato per facilitare le funzioni di migrazione di dati tra database esterni e l'AS400.
Durante lo sviluppo sono state aggiunte varie funzionalità tra cui
 - Funzionalità di anteprima :  è possibile visualizzare un'anteprima dei dati che verranno migrati su AS400.
 - Funzionalità di accesso a metadati.
 - Funzionalità di esportazione :  da matrice a file.
 - Funzionalità di aggiornamento di database esterni all'AS400
 - Funzionalità di esportazione di dati da AS400 verso altri DB

Con database esterni si intendono database non accessibili direttamente tramite l'AS400, quali ad esempio database Oracle, file CSV o Excel.

Le tecnologie utilizzate sono basate su driver JDBC, questo consente di accedere a qualunque DB che supporti tale tecnologia. E' anche supportata la tecnologia ODBC, ma questo impone il vincolo di avere la fonte dati installata sul client dove viene eseguito Loocup.

Questo componente ha un'interfaccia grafica costituita da un Wizard, disponibile solamente in LoocUp.

Il componente non è utilizzabile direttamente, non ha quindi un setup.

Le sue funzionalità sono accessibili tramite i servizi interni JA_00_19 e JA_00_39.

Allo stesso modo gli esempi di utilizzo sono agganciati agli oggetti V3 ASE JA_00_19 e V3 ASE JA_00_39.

# Anteprima dati
Questa funzionalità accede alla fonte dati esterna e restituisce una matrice. Non essendo prevista la paginazione va posta attenzione al volume di dati. Si rischia di bloccare Loocup.
I metodi che restituiscono i dati possono limitare il numero di righe del recordset.


# Importazione di dati
Il processo di importazione accede alla sorgente e copia i dati in un file dell'AS400.

## Come avviare il componente
E' possibile avviare il componente tramite la chiamata a funzione _7_F(DBM;;).
Questa funzione ha la particolarità di indicare solo il componente :  i parametri verranno richiesti direttamente dal componente, mediante l'utilizzo di un wizard.

Può essere utile in alcuni casi aggiungere la voce della funzione ad una voce di menù : 
 :  : PAR F(04)
** : **** : ****C.SEZ Cod="Menù"**
** : **** : ****C.MNU Pos="M.O" Txt="IMPORT DB"    Fun="F(DBM;;)"**


## Nota tecnica
Il componente DBM si appoggia ai servizi JA_00_19 e JA_00_39.
 :  : DEC T(V3) P(ASE) K(JA_00_19) D(Servizio di importazione) O(D)
 :  : DEC T(V3) P(ASE) K(JA_00_39) D(Servizio di scrittura su AS400) O(D)

# Problematiche del componente
L'accesso ai file Excel con i driver JDBC presenta dei bug, dichiarati da Microsoft, che impediscono la lettura di colonne a contenuto misto (numerici-alfanumerici).
Alla data del 29/9/2012 e' in fase di test un approccio alternativo che supera questo problema.


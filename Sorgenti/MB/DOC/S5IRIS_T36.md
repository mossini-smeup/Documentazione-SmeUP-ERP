


# Macchina Preferenziale
Il suffisso utilizzato è il codice "A"
## Obiettivo
Consentire di scegliere la risorsa preferenziale anche se non è la più scarica tenendo conto di un ritardo massimo ammissibile oppure di una data al più tardi iin cui l'operazione deve iniziare.
In questo esempio abbiamo deciso di utilizzare i seguenti campi dell'archivio S5IRIS : 
* S6AA01  è la macchina preferenziale
* S6NU01  è il ritardo massimo ammissibile
* S6FL40  Flag metodo calcolo. Vale "1" nel caso di scelta entro ritardo massimo, "2"  nel caso di data al più tardi.
La data massima al più tardi in questo è la data inizio schedulata al più tardi della fase che presenta una risorsa preferenziale.
## Soluzione
Exit "passacarte"  al programma  mongolfiera che contiene la logica
 :  : DEC T(MB) P(BCDSRC_ESE) K(S5SMX_02A)
 :  : DEC T(MB) P(BCDSRC_ESE) K(S5SMX_05A)
 :  : DEC T(MB) P(BCDSRC_ESE) K(S5SMX_11A)

Programma Mongolfiera
 :  : DEC T(MB) P(BCDSRC_ESE) K(XS5SM01_A)


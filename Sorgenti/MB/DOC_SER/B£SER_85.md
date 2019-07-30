 :  : HEA RESP(LS) STAT(10)
# OBIETTIVO
Invio di una e-mail

# FUNZIONI E METODI

## OGGETTI COLLEGATI
 :  : DEC T(V2) P(LOCOS) K(A17)

 :  : PRO.SER Cod="MAILTE_SP" Tit="Invio e-mail" Fun="F(INP;B£SER_85;MAILTE) SP(Mod(C) Nom(B£SER_85/A) Out(INP))"

 :  : PRO.SER Cod="MAI.OGG" Tit="Invio e-mail in base a tipo mail LOA17" Fun="F(INP;B£SER_85;MAI.OGG) 1(SE;SUB.A17;-(O;;SESUB.A17;Tipo Mail))  2(-;-;-) SP(Mod(C) Nom(B£SER_85/A) Out(INP))"

xxPRO.SER Cod="MAILTE" Tit="Invio e-mail" Fun="A(EMU;B£SER_85;MAILTE) INPUT(ME(AS400) FR(-(O;;**;From;;70)) EM(-(O;;**;To;;5000)) CC(-(F;;**;Cc;;5000)) BC(-(F;;**;Bcc;;5000)) SJ(-(O;;**;Oggetto;;50)) TX(-(F;;**;Testo;;30000)) AT(-(F;;**;Allegato)) CA(-(F;;V2SI/NO;Cancella allegato dopo l'invio)) RC(-(F;;V2SI/NO;Richiesta conferma)) CO(-(F;;V2SI/NO;Notifica consegna)) )"

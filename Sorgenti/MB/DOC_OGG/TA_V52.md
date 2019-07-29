# V52 - Origine dati documento
 :  : DEC T(ST) K(V52)
## OBIETTIVO
Definisce le modalità con cui si assumono, per ogni tipo documento, le informazioni derivate dagli enti.
## CONTENUTO DEI CAMPI
 :  : FLD T$ELEM **Elemento**
 :  : FLD T$N,01 **Campi di derivazione**
Si imposta uno dei seguenti tipi di derivazione : 
- ' '   -    Intestatario documento;
- '1'  -    Ente conferma;
- '2'  -    Ente fatturazione;
- '3'  -    Ente spedizione;
per i seguenti campi : 
--    Priorità
--    Pagamento
--    Spedizione
--    Consegna
--    Imballo
--    Spese 1
--    Spese 2
--    Spese 3
--    Valuta
--    Lingua
--    Vettori
--    Ass.Iva
--    Zona
--    Agente
--    Banca
--    Cat.Contabile
--    Raggrupp. bolle
--    Ente utilizzato per la ripresa valori nei listini
 :  : FLD T$N,02.T$N,01
 :  : FLD T$N,03.T$N,01
 :  : FLD T$N,04.T$N,01
 :  : FLD T$N,05.T$N,01
 :  : FLD T$N,06.T$N,01
 :  : FLD T$N,07.T$N,01
 :  : FLD T$N,08.T$N,01
 :  : FLD T$N,09.T$N,01
 :  : FLD T$N,10.T$N,01
 :  : FLD T$N,11.T$N,01
 :  : FLD T$N,12.T$N,01
 :  : FLD T$N,13.T$N,01
 :  : FLD T$N,14.T$N,01
 :  : FLD T$N,15.T$N,01
 :  : FLD T$N,16.T$N,01
 :  : FLD T$N,17.T$N,01
 :  : FLD T$N,18.T$N,01
 :  : FLD T$N,19.T$N,01
 :  : FLD T$N,20.T$N,01
 :  : FLD T$N,21.T$N,01
 :  : FLD T$N,22.T$N,01
 :  : FLD T$N,23.T$N,01
 :  : FLD T$N,24.T$N,01
 :  : FLD T$V52A **Criterio di ripresa**
Definisce le modalità di ripresa delle informazioni, quando viene variato uno degli Enti del documento.

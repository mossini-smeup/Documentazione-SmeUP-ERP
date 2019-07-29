# Obiettivo
Applica funzioni di crittografia ed hashing ad una stringa

# Funzioni e metodi
## ENC       Cripta
**Crittografa una stringa in chiaro ricevuta in input**
###  RC2          Algoritmo RC2 + HEX
**Crittografa la stringa con algoritmo RC2 e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro e una chiave di almeno 6 caratteri
_4_Output
Restituisce in output la stringa criptata e trasformata in esadecimale
###  AES-128      Algoritmo AES-128 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, crittografa la stringa UTF-8 con** **algoritmo AES-128 CBC e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro e una chiave esadecimale di 16 caratteri
_4_Output
Restituisce in output la stringa criptata e trasformata in esadecimale
###  AES-192      Algoritmo AES-192 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, crittografa la stringa UTF-8 con** **algoritmo AES-192 CBC e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro e una chiave esadecimale di 24 caratteri
_4_Output
Restituisce in output la stringa criptata e trasformata in esadecimale
###  AES-256      Algoritmo AES-256 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, crittografa la stringa UTF-8 con** **algoritmo AES-256 CBC e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro e una chiave esadecimale di 32 caratteri
_4_Output
Restituisce in output la stringa criptata e trasformata in esadecimale
###  BASE64       Base64 (stringa con conv.UTF-8)
**Converte la stringa in chiaro dal CCSID del job a UTF-8, e trasforma la stringa risultante** **in Base64.**
_4_Input
Riceve in input la stringa in chiaro
_4_Output
Restituisce in output la stringa trasformata in Base64
###  BASE64_BIN   Base64 (binario)
**Trasforma la stringa in chiaro in Base64 senza eseguire nessuna conversione precedente.**
_4_Input
Riceve in input la stringa in chiaro
_4_Output
Restituisce in output la stringa trasformata in Base64

## DEC       Decripta
**Decripta una stringa criptata ricevuta in input**
###  RC2          Algoritmo RC2 + HEX
**Converte la stringa criptata da esadecimale e decripta la stringa con algoritmo RC2**
_4_Input
Riceve in input la stringa criptata (covertita in esadecimale) e una chiave di almeno 6 caratteri
_4_Output
Restituisce in output la stringa in chiaro
###  AES-128      Algoritmo AES-128 + HEX
**Converte la stringa criptata da esadecimale, decripta la stringa ottenuta con** **algoritmo AES-128 CBC e converte la stringa risultante da UTF-8 al CCSID del job.** _4_Input
Riceve in input la stringa criptata (covertita in esadecimale) e una chiave esadecimale di 16 caratteri
_4_Output
Restituisce in output la stringa in chiaro
###  AES-192      Algoritmo AES-192 + HEX
**Converte la stringa criptata da esadecimale, decripta la stringa ottenuta con** **algoritmo AES-192 CBC e converte la stringa risultante da UTF-8 al CCSID del job.** _4_Input
Riceve in input la stringa criptata (covertita in esadecimale) e una chiave esadecimale di 24 caratteri
_4_Output
Restituisce in output la stringa in chiaro
###  AES-256      Algoritmo AES-256 + HEX
**Converte la stringa criptata da esadecimale, decripta la stringa ottenuta con** **algoritmo AES-256 CBC e converte la stringa risultante da UTF-8 al CCSID del job.** _4_Input
Riceve in input la stringa criptata (covertita in esadecimale) e una chiave esadecimale di 32 caratteri
_4_Output
Restituisce in output la stringa in chiaro
###  BASE64       Base64 (stringa con conv.UTF-8)
**Decodifica la stringa da Base64 in chiaro e converte la stringa risultante da UTF-8****al CCSID del job.**
_4_Input
Riceve in input la stringa criptata in Base64
_4_Output
Restituisce in output la stringa in chiaro
###  BASE64_BIN   Base64 (binario)
**Decodifica la stringa da Base64 in chiaro senza eseguire nessuna conversione successiva sul** **risultato.**
_4_Input
Riceve in input la stringa criptata in Base64
_4_Output
Restituisce in output la stringa in chiaro

## HASH      Generazione HASH
Calcola l'hash, convertito in esadecimale, di una stringa ricevuta in input
###  MD5       MD5 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **MD5 e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro
_4_Output
Restituisce in output l'hash della stringa trasformato in esadecimale
###  SHA-1     SHA-1 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **SHA-1 e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro
_4_Output
Restituisce in output l'hash della stringa trasformato in esadecimale
###  SHA-256   SHA-256 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **SHA-256 e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro
_4_Output
Restituisce in output l'hash della stringa trasformato in esadecimale
###  SHA-384   SHA-384 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **SHA-384 e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro
_4_Output
Restituisce in output l'hash della stringa trasformato in esadecimale
###  SHA-512   SHA-512 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **SHA-512 e converte la stringa risultante in esadecimale.**
_4_Input
Riceve in input la stringa in chiaro
_4_Output
Restituisce in output l'hash della stringa trasformato in esadecimale

## CHKHASH   Controllo corrispondenza hash
Controlla la corrispondenza tra l'hash ricevuto in input e quello calcolato a partire dalla stringa in chiaro ricevuta
###  MD5       MD5 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **MD5 e converte la stringa risultante in esadecimale; quindi la confronta con l'hash in **esadecimale ricevuto.**
_4_Input
Riceve in input la stringa in chiaro e un hash in esadecimale da confrontare
_4_Output
Restituisce in output l'indicatore 35 acceso e il messaggio BAS1289 se l'hash non corrisponde alla stringa ricevuta.
###  SHA-1     SHA-1 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **SHA-1 e converte la stringa risultante in esadecimale; quindi la confronta con l'hash in **esadecimale ricevuto.**
_4_Input
Riceve in input la stringa in chiaro e un hash in esadecimale da confrontare
_4_Output
Restituisce in output l'indicatore 35 acceso e il messaggio BAS1289 se l'hash non corrisponde alla stringa ricevuta.
###  SHA-256   SHA-256 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **SHA-256 e converte la stringa risultante in esadecimale; quindi la confronta con l'hash in **esadecimale ricevuto.**
_4_Input
Riceve in input la stringa in chiaro e un hash in esadecimale da confrontare
_4_Output
Restituisce in output l'indicatore 35 acceso e il messaggio BAS1289 se l'hash non corrisponde alla stringa ricevuta.
###  SHA-384   SHA-384 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **SHA-384 e converte la stringa risultante in esadecimale; quindi la confronta con l'hash in **esadecimale ricevuto.**
_4_Input
Riceve in input la stringa in chiaro e un hash in esadecimale da confrontare
_4_Output
Restituisce in output l'indicatore 35 acceso e il messaggio BAS1289 se l'hash non corrisponde alla stringa ricevuta.
###  SHA-512   SHA-512 + HEX
**Converte la stringa in chiaro dal CCSID del job a UTF-8, calcola l'hash con algoritmo** **SHA-512 e converte la stringa risultante in esadecimale; quindi la confronta con l'hash in **esadecimale ricevuto.**
_4_Input
Riceve in input la stringa in chiaro e un hash in esadecimale da confrontare
_4_Output
Restituisce in output l'indicatore 35 acceso e il messaggio BAS1289 se l'hash non corrisponde alla stringa ricevuta.

# Prerequisiti
 :  : DEC T(MB) P(QILEGEN) K(£G02D)

# Oggetti collegati
 :  : DEC T(MB) P(QILEGEN) K(£K15)


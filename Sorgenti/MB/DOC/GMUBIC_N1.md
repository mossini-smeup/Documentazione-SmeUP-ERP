# Definizioni su situazione ubicazione
Un'ubicazione è bloccata se è stato inserito il flag in anagrafica.
Un'ubicazione è vuota se : 
 * la qtà attesa è = 0;
 * la giacenza è = 0;
 * non viene tenuta in considerazione la qtà allocata. Ad esempio se giacenza = 5 e qtà allocata = 5, l'ubicazione è impegnata :  sarà libera in futuro, ma al momento non lo si può assumere.

# Definizioni su GMQUAN
 * G§QTAL :  Qtà allocata; si impegna una qtà esistente
 * G§QTAT :  Qtà attesa; si destina una qtà futura

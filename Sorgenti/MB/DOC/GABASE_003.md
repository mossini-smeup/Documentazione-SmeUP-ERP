## Note implementazione
> Stati fissati nei programmi SME.up
   :  : DEC T(TA) P(B£WGA) K(10)
   :  : DEC T(TA) P(B£WGA) K(15)
   :  : DEC T(TA) P(B£WGA) K(16)
   :  : DEC T(TA) P(B£WGA) K(20)
   :  : DEC T(TA) P(B£WGA) K(50)
> Impostazioni Tabelle GA1/2
   :  : DEC T(TA) P(GA1) K(*)
   :  : DEC T(TA) P(GA2) K(*)
> Oggetti
   :  : DEC T(TA) P(*CNTT) K(RA)
> Note
   :  : DEC T(TA) P(NSC) K(GAR)
  :  : IF F1( :  : OAV T1(TA) P1(NSC) K1(GAR) OA(I/T$KYC1)) OP(<>)     F2(**) CM(_9_  Oggetto 1 di GAR deve essere "**")
  :  : IF F1( :  : OAV T1(TA) P1(NSC) K1(GAR) OA(I/T$KYC2)) OP(<>)     F2(**) CM(_9_  Oggetto 2 di GAR deve essere "**")

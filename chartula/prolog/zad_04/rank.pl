
:-op(140, fy, neg).
:-op(160, xfy, [and, or, imp, revimp, uparrow, downarrow, notimp, notrevimp]).

r(p,0):-!.
r(q,0):-!.
r(s,0):-!.
r(neg p,0):-!.
r(neg q,0):-!.
r(neg s,0):-!.
r(verum,0):-!.
r(falsum,0):-!.
r(neg verum,1):-!.
r(neg falsum,1):-!.

r(Z,R):-Z=neg neg X, r(X,R1), R is R1 +1.
r(Z,R):-Z=X and Y, r(X,R1), r(Y,R2), R is R1+R2+1.
r(Z,R):-Z=neg (X and Y), r(neg X,R1), r(neg Y,R2), R is R1+R2+1.
r(Z,R):-Z=X or Y, r(X,R1), r(Y,R2), R is R1+R2+1.
r(Z,R):-Z=neg(X or Y), r(neg X,R1), r(neg Y,R1), R is R1+R2+1.
r(Z,R):-Z=X imp Y, r(neg X,R1), r(Y,R2), R is R1+R2+1.
r(Z,R):-Z=neg(X imp Y), r(X,R1), r(neg Y,R2), R is R1+R2+1.
r(Z,R):-Z=X revimp Y, r(X,R1), r(neg Y,R2), R is R1+R2+1.
r(Z,R):-Z=neg(X revimp Y), r(neg X,R1), r(Y,R2), R is R1+R2+1.
r(Z,R):-Z=X uparrow Y, r(neg X,R1), r(neg Y,R2), R is R1+R2+1.
r(Z,R):-Z=X downarrow Y, r(neg X,R1), r(neg Y,R2), R is R1+R2+1.
r(Z,R):-Z=neg(X uparrow Y), r(X,R1), r(Y,R2), R is R1+R2+1.
r(Z,R):-Z=neg(X downarrow Y), r(X,R1), r(Y,R2), R is R1+R2+1.




:-op(140, fy, neg).
:-op(160, xfy, [and, or, imp, revimp, uparrow, downarrow, notimp, notrevimp]).

conjunctive(_ and _).
conjunctive(neg(_ or _)).
conjunctive(neg(_ imp _)).
conjunctive(neg(_ revimp _)).
conjunctive(neg(_ uparrow _)).
conjunctive(_ notimp _).
conjunctive(_ notrevimp _).
conjunctive(_ downarrow _).

disjunctive(neg(_ and _)).
disjunctive(_ or _).
disjunctive(_ imp _).
disjunctive(_ revimp _).
disjunctive(neg(_ notimp _)).
disjunctive(neg(_ notrevimp _)).
disjunctive(neg(_ downarrow _)).
disjunctive(_ uparrow _).

unary(neg neg _).
unary(neg true).
unary(neg false).

components(X and Y, X,Y).
components(neg(X and Y), neg X, neg Y).
components(X or Y, X, Y).
components(neg(X or Y), neg X, neg Y).
components(X imp Y, neg X, Y).
components(neg(X imp Y), X, neg Y).
components(X revimp Y, X, neg Y).
components(neg(X revimp Y), neg X, Y).
components(X uparrow Y, neg X, neg Y).
components(X downarrow Y, neg X, neg Y).
components(neg(X uparrow Y), X, Y).
components(neg(X downarrow Y), X, Y).


component(neg neg X,X).
component(neg true, false).
component(neg false, true).



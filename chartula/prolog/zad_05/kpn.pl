:-op(140, fy, neg).
:-op(160, xfy, [and, or, imp, revimp, uparrow, downarrow, notimp, notrevimp]).

remove(_,[],[]).
remove(X,[X|Tail],Newtail):-remove(X,Tail,Newtail).
remove(X,[Head|Tail],[Head|Newtail]):-remove(X,Tail,Newtail).

conjunctive(_ and _).
conjunctive(neg(_ or _)).
conjunctive(neg(_ imp _)).
conjunctive(neg(_ revimp _)).
conjunctive(neg(_ uparrow _)).
conjunctive(_ downarrow _).
conjunctive(_ notimp _).
conjunctive(_ notrevimp _).

disjunctive(neg(_ and _)).
disjunctive(_ or _).
disjunctive(_ imp _).
disjunctive(_ revimp _).
disjunctive(_ uparrow _).
disjunctive(neg(_ downarrow _)).
disjunctive(neg(_ notimp _)).
disjunctive(neg(_ notrevimp _)).

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
components(neg(X uparrow Y), X,Y).
components(X downarrow Y, neg X, neg Y).
components(neg(X downarrow Y), X, Y).
components(X notimp Y, X,neg Y).
components(neg(X notimp Y), neg X, Y).
components(X notrevimp Y, neg X, Y).
components(neg(X notrevimp Y), X, neg Y).

component(neg neg X,X).
component(neg true, false).
component(neg false, true).

/*zadanie wyslano na email mkolowsk@amu.edu.pl 
*
* Generalnie wystarczylo pozamieniac wszystkie Alpha na Beta, Beta na Alpha, Conjunction na Disjunction, etc. 
 * Dlaczego? Poniewaz algorytm wyprowadzania KPN rozni sie od algorytmu wyprowadzania DPN
 * regulami wlasnie w przypadku formul typu Alpha oraz Formul typu Beta.
 * Mamy tu do czynienia z pewnego rodzaju odwrotnoscia stad zamiania.
 *
 * Szczegoly jako komentarze w kodzie ponizej.
 * */


/* Singlestep dla formuł typu unarnego. Formula jest disjunkcja, formula typu unarnego.
 * W dalszych linijkach zachodzi zastepowanie na podstawie   
 * 
 * */
singlestep([Disjunction|Rest],New) :-
  member(Formula, Disjunction),
  unary(Formula),
  component(Formula, Newformula),
  remove(Formula, Disjunction, Temporary),
 Newdisjunction=[Newformula|Temporary],
 New=[Newdisjunction|Rest].

/* Singlestep dla formul typu Beta.
 * Bierze pod uwage komponenty Beta.
 * Komponenty zostaja w tej samej klauzuli
 *
 */
singlestep([Disjunction|Rest],New) :-
  member(Beta, Disjunction),
  disjunctive(Beta),
  components(Beta, Betaone, Betatwo),
  remove(Beta, Disjunction, Temporary),
 Newdis=[Betaone,Betatwo|Temporary],
 New=[Newdis|Rest].

/* Singlestep dal formul typu Alfa.
 * Tworzy dwie klauzule w ktorych znajduja sie odpowiednio 
 * komponenty alfa1 oraz alfa2
*
*/
singlestep([Disjunction|Rest],New) :-
  member(Alpha, Disjunction),
  conjunctive(Alpha),
  components(Alpha, Alphaone, Alphatwo),
  remove(Alpha, Disjunction, Temporary),
 Newdisone=[Alphaone|Temporary],
  Newdistwo=[Alphatwo|Temporary],
  New=[Newdisone, Newdistwo|Rest].

singlestep([Disjunction|Rest],[Disjunction|Newrest]) :-
  singlestep(Rest, Newrest).


expand(Dis,Newdis):-
        singlestep(Dis, Temp),
        expand(Temp, Newdis).
expand(Dis,Dis).

clauseform(X,Y):-expand([[X]],Y).






















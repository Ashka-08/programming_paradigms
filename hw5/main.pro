% https://swish.swi-prolog.org/

% Rules
sum([], 0).
sum([H|T], Sum) :-
    sum(T, Sum1),
    Sum is H + Sum1.

% Query
?- sum([1,5,10], Sum).

% Output
% Sum = 16
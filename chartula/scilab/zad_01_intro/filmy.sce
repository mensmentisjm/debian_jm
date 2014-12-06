licznik = 0;
czas=0;
[wier kol]=size(dane);
for i=1:1:wier
    if dane(i,1) == 1996
        licznik=licznik+1;
        czas=czas+dane(i,4);
    end
end
disp(czas/licznik)

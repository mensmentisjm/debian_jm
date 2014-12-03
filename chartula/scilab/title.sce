t=cell2mat(tytuly);
proporcja=dane(:,4)./dane(:,3);
bar(proporcja);
a=gca();
a.rotation_angles=[0,180]
a.x_ticks=tlist(["ticks","locations","labels"],(1:36)',t);

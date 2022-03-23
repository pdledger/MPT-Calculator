algebraic3d

solid sphout = sphere (0, 0, 0; 200);
solid sphin = sphere (0, 0, 0; 1) -maxh=0.1;
solid sphinsh = sphere (0, 0, 0; 0.75) -maxh=0.1;

solid shell = sphin and not sphinsh;

#solid rest = sphinsh or sphout and not sphin;
solid rest = sphout and not sphin;
#solid rest = sphout;

tlo rest -transparent -col=[0,0,1];#air
tlo shell -col=[1,0,0];#sphere -mur=1 -sig=6E+06
tlo sphinsh -transparent -co=[0,0,1]; #inner -mur=1 -sig=1

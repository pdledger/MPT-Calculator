algebraic3d

solid sphout = sphere (0, 0, 0; 200);
solid sphin = sphere (1.1, 0, 0; 1) -maxh=0.1;
solid sphin2 = sphere (-1.1, 0, 0; 1) -maxh=0.1;

solid rest = sphout and not sphin and not sphin2;

tlo rest -transparent -col=[0,0,1];#air
tlo sphin -col=[1,0,0];#sphere -mur=1 -sig=6E+06
tlo sphin2 -col=[1,0,0];#sphere -mur=1 -sig=6E+06

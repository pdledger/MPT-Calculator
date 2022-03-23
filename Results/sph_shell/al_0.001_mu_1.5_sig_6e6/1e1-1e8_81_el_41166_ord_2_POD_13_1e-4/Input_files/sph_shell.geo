algebraic3d

solid sphout = sphere (0, 0, 0; 2000);
solid sphin = sphere (0, 0, 0; 35) -maxh=3;
solid sphinsh = sphere (0, 0, 0; 25) -maxh=2;

solid shell = sphin and not sphinsh;

#solid rest = sphinsh or sphout and not sphin;
solid rest = sphout and not shell;
#solid rest = sphout;

tlo rest -transparent -col=[0,0,1];#air
tlo shell -col=[1,0,0];#sphere -mur=1.5 -sig=6E+06

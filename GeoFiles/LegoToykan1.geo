algebraic3d

solid rest = sphere (0, 0, 0; 100);
solid brick1 = orthobrick (0,0,0; 3.8,1.9,1) -maxh=0.2;
solid brick2 = orthobrick (0,1.9,0;1.9,8,1) -maxh=0.2;
solid brick3 = orthobrick (0,0,1;1.9,1.9,1.9) -maxh=0.2;


solid domain = rest and not brick1 and not brick2 and not brick3;

tlo domain -transparent -col=[0,0,1];#air
tlo brick1 -col=[1,0,0];#mat1 -mur=1 -sig=5.95E+07
tlo brick2 -col=[0,1,0];#mat2 -mur=1 -sig=5.95E+07
tlo brick3 -col=[0,1,0];#mat2 -mur=1 -sig=5.95E+07

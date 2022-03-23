algebraic3d

solid rest = sphere (0, 0, 0; 100);
solid brick1 = orthobrick (-2,-4,-0.5;2,4,0.5) -maxh=0.2;

solid cylin = cylinder ( 0, 2, -0.5; 0, 2, 0.5; 1.5 )
        and plane (0, 2, -0.5; 0, 0, -1)
        and plane (0, 2, 0.5; 0, 0, 1) -maxh=0.08;

solid brickhole = brick1 and not cylin;

solid domain = rest and not brickhole;

tlo domain -transparent -col=[0,0,1];#air
tlo brickhole -col=[1,0,0];#mat1 -mur=1 -sig=5.95E+07

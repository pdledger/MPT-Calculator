#
## A cone
#
algebraic3d

# Cone given by bottom circle and top circle
# and cut by planes:

solid boxout = orthobrick (-1000, -1000, -1000; 1000, 1000, 1000) -bco=1;

solid cutcone = cone ( 0, 0, 0; 7.5; 0, 0, 15; 1 )
        and plane (0, 0, 0; 0, 0, -1)
        and plane (0, 0, 15; 0, 0, 1);



solid rest = boxout and not cutcone;

solid object= cutcone  -maxh=0.5;

tlo rest -transparent -col=[0.56078434,0.68627453,0.56078434];#air
tlo object -col=[0,0,1];#mat1 -mur=1 -sig=1.39E+07

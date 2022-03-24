#This file contains the function for checking the validity of the eddy current model
#Functions -PODP

#Importing
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl
import scipy.linalg as slin
import multiprocessing_on_dill as multiprocessing
import netgen.meshing as ngmeshing
import sys
from ngsolve import *

sys.path.insert(0,"Functions")
sys.path.insert(0,"Settings")
from Settings import SolverParameters

def Centroid(Object,alpha,inorout,Stepmesh):
    Object = Object[:-4]+".vol"
    #Set order Ordercheck to be of low order to speed up computation.
    Ordercheck = 1
    #Accuracy is increased by increaing noutput, but at greater cost
    noutput=20

        #Loading the object file
    ngmesh = ngmeshing.Mesh(dim=3)
    ngmesh.Load("VolFiles/"+Object)

    #Creating the mesh and defining the element types
    mesh = Mesh("VolFiles/"+Object)
    if Stepmesh == False:
        mesh.Curve(5)#This can be used to refine the mesh

    #Set materials
    inout_coef = [inorout[mat] for mat in mesh.GetMaterials() ]
    inout = CoefficientFunction(inout_coef)

    # Compute volume of Object
    Vol=Integrate(inout,mesh)*(alpha**3)
    print("Volume of the object is",Vol)

    femfull = H1(mesh, order=1,dirichlet="default|outside")

    # Find Centroid
    xp=alpha**3*Integrate(inout*x,mesh)/Vol
    yp=alpha**3*Integrate(inout*y,mesh)/Vol
    zp=alpha**3*Integrate(inout*z,mesh)/Vol

    print("The centoid of the object is(",xp,",",yp,",",zp,")")
    print(dir(mesh))

    return

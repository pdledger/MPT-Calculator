#Importing
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

#This is required for when a copy of the file is sent to the results section
try:
    sys.path.insert(0,"1e1-1e8_81_el_62053_ord_0_POD_13_1e-4")
except:
    pass

from PlotterSettings import PlotterSettings
try:
    sys.path.insert(0,"1e1-1e8_81_el_62053_ord_0_POD_13_1e-4/Functions")
except:
    pass
from Plotters import *

#Frequency arrays
Frequencies = np.genfromtxt("1e1-1e8_81_el_62053_ord_0_POD_13_1e-4/Data/Frequencies.csv",delimiter=",")

#Eigenvalue arrays
EigenValues0 = np.genfromtxt("1e1-1e8_81_el_62053_ord_0_POD_13_1e-4/Data/Eigenvalues.csv",delimiter=",",dtype=complex)
EigenValues1 = np.genfromtxt("1e1-1e8_81_el_62053_ord_1_POD_13_1e-4/Data/Eigenvalues.csv",delimiter=",",dtype=complex)

EigenValues2 = np.genfromtxt("1e1-1e8_81_el_62053_ord_2_POD_13_1e-4/Data/Eigenvalues.csv",delimiter=",",dtype=complex)
EigenValues3 = np.genfromtxt("1e1-1e8_81_el_62053_ord_3_POD_13_1e-4/Data/Eigenvalues.csv",delimiter=",",dtype=complex)
EigenValues4 = np.genfromtxt("1e1-1e8_81_el_62053_ord_4_POD_13_1e-4/Data/Eigenvalues.csv",delimiter=",",dtype=complex)

pmax=5

#Retrieve the settings for the plot
Title, Show, ETP, _, MLS, MMS, SLS, SMS, _, _, ECL = PlotterSettings()
#Create a way to reference xkcd colours
PYCOL=['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b','#e377c2','#7f7f7f','#bcbd22','#17becf']
#Plot the real graph
fig, ax = plt.subplots()
#Plot the convergenc of eigenvalues 1:
for i in range(pmax):
    if i==0:
        lines = ax.plot(Frequencies,EigenValues0[:,0].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==1:
        lines += ax.plot(Frequencies,EigenValues1[:,0].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==2:
        lines += ax.plot(Frequencies,EigenValues2[:,0].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==3:
        lines += ax.plot(Frequencies,EigenValues3[:,0].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==4:
        lines += ax.plot(Frequencies,EigenValues4[:,0].real,MLS,markersize=MMS,color=PYCOL[i])


ymin, ymax = ax.get_ylim()

#Format the axes
plt.xscale('log')
plt.ylim(ymin, ymax)
ax.grid(True)
ax.yaxis.set_major_formatter(plt.FuncFormatter(TickFormatter))
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.15, bottom=0.1, right=0.94, top=0.90)

#Label the axes
plt.xlabel("Frequency (rad/s)")
plt.ylabel(r"$\lambda(\mathcal{N}^0+\mathcal{R})$")

#Title
if Title==True:
    plt.title(r"Eigenvalues of $\mathcal{N}^0+\mathcal{R}$")

#Create the legend
names = []
for i in range(pmax+1):
    names.append(r"$\lambda_1(\mathcal{N}^0+\mathcal{R})$ (POD), p ="+str(i)+"")


#Make the legend
ax.legend(lines,names)

#Save the graph
plt.savefig("RealEigenvalues1.pdf")
plt.show()

fig, ax = plt.subplots()

#Plot the convergenc of eigenvalue 2:
for i in range(pmax):
    if i==0:
        lines = ax.plot(Frequencies,EigenValues0[:,1].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==1:
        lines += ax.plot(Frequencies,EigenValues1[:,1].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==2:
        lines += ax.plot(Frequencies,EigenValues2[:,1].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==3:
        lines += ax.plot(Frequencies,EigenValues3[:,1].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==4:
        lines += ax.plot(Frequencies,EigenValues4[:,1].real,MLS,markersize=MMS,color=PYCOL[i])

ymin, ymax = ax.get_ylim()

#Format the axes
plt.xscale('log')
plt.ylim(ymin, ymax)
ax.grid(True)
ax.yaxis.set_major_formatter(plt.FuncFormatter(TickFormatter))
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.15, bottom=0.1, right=0.94, top=0.90)

#Label the axes
plt.xlabel("Frequency (rad/s)")
plt.ylabel(r"$\lambda(\mathcal{N}^0+\mathcal{R})$")

#Title
if Title==True:
    plt.title(r"Eigenvalues of $\mathcal{N}^0+\mathcal{R}$")

#Create the legend
names = []
for i in range(pmax+1):
    names.append(r"$\lambda_2(\mathcal{N}^0+\mathcal{R})$ (POD), p ="+str(i)+"")

#Make the legend
ax.legend(lines,names)

#Save the graph
plt.savefig("RealEigenvalues2.pdf")
plt.show()

fig, ax = plt.subplots()

#Plot the convergenc of eigenvalue 2:
for i in range(pmax):
    if i==0:
        lines = ax.plot(Frequencies,EigenValues0[:,2].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==1:
        lines += ax.plot(Frequencies,EigenValues1[:,2].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==2:
        lines += ax.plot(Frequencies,EigenValues2[:,2].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==3:
        lines += ax.plot(Frequencies,EigenValues3[:,2].real,MLS,markersize=MMS,color=PYCOL[i])
    elif i==4:
        lines += ax.plot(Frequencies,EigenValues4[:,2].real,MLS,markersize=MMS,color=PYCOL[i])

ymin, ymax = ax.get_ylim()

#Format the axes
plt.xscale('log')
plt.ylim(ymin, ymax)
ax.grid(True)
ax.yaxis.set_major_formatter(plt.FuncFormatter(TickFormatter))
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.15, bottom=0.1, right=0.94, top=0.90)

#Label the axes
plt.xlabel("Frequency (rad/s)")
plt.ylabel(r"$\lambda(\mathcal{N}^0+\mathcal{R})$")

#Title
if Title==True:
    plt.title(r"Eigenvalues of $\mathcal{N}^0+\mathcal{R}$")

#Create the legend
names = []
for i in range(pmax+1):
    names.append(r"$\lambda_3(\mathcal{N}^0+\mathcal{R})$ (POD), p ="+str(i)+"")

#Make the legend
ax.legend(lines,names)

#Save the graph
plt.savefig("RealEigenvalues3.pdf")
plt.show()

#Plot the real graph
fig, ax = plt.subplots()
#Plot the convergenc of eigenvalues 1:
for i in range(pmax):
    if i==0:
        lines = ax.plot(Frequencies,EigenValues0[:,0].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==1:
        lines += ax.plot(Frequencies,EigenValues1[:,0].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==2:
        lines += ax.plot(Frequencies,EigenValues2[:,0].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==3:
        lines += ax.plot(Frequencies,EigenValues3[:,0].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==4:
        lines += ax.plot(Frequencies,EigenValues4[:,0].imag,MLS,markersize=MMS,color=PYCOL[i])


ymin, ymax = ax.get_ylim()

#Format the axes
plt.xscale('log')
plt.ylim(ymin, ymax)
ax.grid(True)
ax.yaxis.set_major_formatter(plt.FuncFormatter(TickFormatter))
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.15, bottom=0.1, right=0.94, top=0.90)

#Label the axes
plt.xlabel("Frequency (rad/s)")
plt.ylabel(r"$\lambda(\mathcal{I})$")

#Title
if Title==True:
    plt.title(r"Eigenvalues of $\mathcal{I}$")

#Create the legend
names = []
for i in range(pmax+1):
    names.append(r"$\lambda_1(\mathcal{I})$ (POD), p ="+str(i)+"")


#Make the legend
ax.legend(lines,names)

#Save the graph
plt.savefig("ImagEigenvalues1.pdf")
plt.show()

fig, ax = plt.subplots()

#Plot the convergenc of eigenvalue 2:
for i in range(pmax):
    if i==0:
        lines = ax.plot(Frequencies,EigenValues0[:,1].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==1:
        lines += ax.plot(Frequencies,EigenValues1[:,1].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==2:
        lines += ax.plot(Frequencies,EigenValues2[:,1].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==3:
        lines += ax.plot(Frequencies,EigenValues3[:,1].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==4:
        lines += ax.plot(Frequencies,EigenValues4[:,1].imag,MLS,markersize=MMS,color=PYCOL[i])

ymin, ymax = ax.get_ylim()

#Format the axes
plt.xscale('log')
plt.ylim(ymin, ymax)
ax.grid(True)
ax.yaxis.set_major_formatter(plt.FuncFormatter(TickFormatter))
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.15, bottom=0.1, right=0.94, top=0.90)

#Label the axes
plt.xlabel("Frequency (rad/s)")
plt.ylabel(r"$\lambda(\mathcal{I})$")

#Title
if Title==True:
    plt.title(r"Eigenvalues of $\mathcal{I}$")

#Create the legend
names = []
for i in range(pmax+1):
    names.append(r"$\lambda_2(\mathcal{I})$ (POD), p ="+str(i)+"")

#Make the legend
ax.legend(lines,names)

#Save the graph
plt.savefig("ImagEigenvalues2.pdf")
plt.show()

fig, ax = plt.subplots()

#Plot the convergenc of eigenvalue 2:
for i in range(pmax):
    if i==0:
        lines = ax.plot(Frequencies,EigenValues0[:,2].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==1:
        lines += ax.plot(Frequencies,EigenValues1[:,2].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==2:
        lines += ax.plot(Frequencies,EigenValues2[:,2].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==3:
        lines += ax.plot(Frequencies,EigenValues3[:,2].imag,MLS,markersize=MMS,color=PYCOL[i])
    elif i==4:
        lines += ax.plot(Frequencies,EigenValues4[:,2].imag,MLS,markersize=MMS,color=PYCOL[i])

ymin, ymax = ax.get_ylim()

#Format the axes
plt.xscale('log')
plt.ylim(ymin, ymax)
ax.grid(True)
ax.yaxis.set_major_formatter(plt.FuncFormatter(TickFormatter))
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.15, bottom=0.1, right=0.94, top=0.90)

#Label the axes
plt.xlabel("Frequency (rad/s)")
plt.ylabel(r"$\lambda(\mathcal{I})$")

#Title
if Title==True:
    plt.title(r"Eigenvalues of $\mathcal{I}$")

#Create the legend
names = []
for i in range(pmax+1):
    names.append(r"$\lambda_3(\mathcal{I})$ (POD), p ="+str(i)+"")

#Make the legend
ax.legend(lines,names)

#Save the graph
plt.savefig("ImagEigenvalues3.pdf")
plt.show()

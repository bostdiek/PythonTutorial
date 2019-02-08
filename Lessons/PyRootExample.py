'''
Uses python 2
Author: Bryan Ostdiek
bostdiek@gmail.com
This file reads in a root LHEF file, finds the particles of interest, and
plots histograms
'''
import array
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import ROOT as rt
import sys

DEBUG = False  # comment to run through only first 1000 events

# Make the plots in the native python plotting look good
plt.rcParams.update({'font.family': 'cmr10',
                     'font.size': 13}
                    )
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.labelsize'] = 15


# Now define the functions that I want to use on my data
def get_inv_mass(fourm1, fourm2):
    '''
    The function takes in two lists, which should be four vectors
    in the form of (E, PX, PY, PZ)

    Returns: The invariant mass of the two vectors
    '''
    e1, px1, py1, pz1 = fourm1
    e2, px2, py2, pz2 = fourm2

    return np.sqrt((e1 + e2)**2 - (px1 + px2)**2 -
                   (py1 + py2)**2 - (pz1 + pz2)**2
                   )


def get_rap(four_momentum):
    '''Calculates the rapidity for a list which is a four vector'''
    e, px, py, pz = four_momentum
    return 0.5 * np.log((e + pz) / (e - pz))


# Lastly, define my analysis function which will be run on multiple files
def BasicAnalysis(fname, pid1, pid2):
    '''
Usage:
    For each event in a root file, find the two particles of interest and gets
    their four vectors (E, PX, PY, PZ). Additionally calculates their rapidities
    and transverse momentum. Lastly, it combines the four vectors and gives the
    invariant mass.

Inputs:
    fname = path to root file with 'LHEF' tree
    pid1 = interger denoting the particle ID to look for for particle 1
    pid2 = interger denoting the particle ID to look for for particle 2

Outputs:
    List with a header.
    '''
    Tfile = rt.TFile(fname)
    Events = Tfile.Get('LHEF')
    Particles = Events.GetBranch("Particle")
    totalentries = Events.GetEntriesFast()
    print 'Total number of events: {0}'.format(totalentries)

    update_proc = totalentries / 20

    outlist = [['e1', 'px1', 'py1', 'pz1', 'pt1', 'y1', 'e2', 'px2', 'py2', 'pz2', 'pt2', 'y2', 'yt', 'minv']]

    for i in xrange(totalentries):
        Events.GetEntry(i)
        if i > 1 and (i % update_proc == 0):
            print('Processed {0:8d} / {1:8d} events ({2}%)'.format(i,
                                                                   totalentries,
                                                                   float(100. * i / totalentries)
                                                                   )
                  )
            sys.stdout.flush()
            if DEBUG:
                print 'short run for debugging'
                break
    #             sys.exit("short run for debugging")

        PID = []
        EE = []
        PX = []
        PY = []
        PZ = []
        for i in range(int(Events.GetLeaf('Particle_size').GetValue())):
            PID.append(Events.GetLeaf('Particle.PID').GetValue(i))
            EE.append(Events.GetLeaf('Particle.E').GetValue(i))
            PX.append(Events.GetLeaf('Particle.Px').GetValue(i))
            PY.append(Events.GetLeaf('Particle.Py').GetValue(i))
            PZ.append(Events.GetLeaf('Particle.Pz').GetValue(i))

        pts = []
        for pid, e, px, py, pz in zip(PID, EE, PX, PY, PZ):
            if pid == pid1:
                particle = [e, px, py, pz,
                            np.sqrt(px**2 + py**2),
                            get_rap([e, px, py, pz])
                            ]
            if pid == pid2:
                antiparticle = [e, px, py, pz,
                                np.sqrt(px**2 + py**2),
                                get_rap([e, px, py, pz])
                                ]

        outlist.append(particle + antiparticle + [get_rap([x+y for x, y in zip(particle[:4], antiparticle[:4])]),
                                                  get_inv_mass(particle[:4],
                                                               antiparticle[:4])
                                                  ]
                       )
    return outlist


# Now the main part of the file
MyFile = '../Data/Photon_to_bb.root'
ppbar_A_bb = BasicAnalysis(MyFile,
                           5,  # b quark
                           -5  # anti b
                           )
# Convert the list to a data frame
ppbar_A_bb = pd.DataFrame(ppbar_A_bb[1:],
                          columns=ppbar_A_bb[0])

# Now make a histogram
plt.figure(figsize=(4, 4))
plt.hist(ppbar_A_bb['minv'], bins=50, histtype='step')
plt.xlabel(r'$m_{b\bar{b}}$ [GeV]')
plt.ylabel('Number of events')
plt.yscale('log')
plt.savefig('PlottingTest.pdf', bbox_inches='tight')

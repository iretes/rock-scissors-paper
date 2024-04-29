# PySCeS input file: https://stochpy.sourceforge.net/html/inputfile_doc.html#pysces-inputfile
# Stochastic Simulation Algorithm input format
# Rock Scissors Paper model

# R + S  --> 2R, Pr
# P + R --> 2P, Pp
# S + P --> 2S, Ps

R1:
    R + S > R + R
    R*S*Pr

R2: 
    P + R > P + P
    P*R*Pp

R3:
    S + P > S + S
    S*P*Ps

# Parameters
Pr = 0.2
Ps = 0.5
Pp = 0.3

# Init Values
R = 33
S = 33
P = 33
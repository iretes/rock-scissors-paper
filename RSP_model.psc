# PySCeS input file
# Stochastic Simulation Algorithm input format
# Rock Scissors Paper model

# R + S  --> S + 2R, Pr
# R + P --> P, Pp
# S + P --> P + 2S, Ps
# S + R --> R, Ps
# P + R --> R + 2P, Pr
# P + S --> S, Pr

R1:
    R + S > S + R + R
    R*S*Pr

R2: 
    R + P > P
    R*P*Pp

R3:
    S + P > P + S + S
    S*P*Ps

R4:
    S + R > R
    S*R*Ps

R5:
    P + R > R + P + P
    P*R*Pr

R6:
    P + S > S
    P*S*Pr

#InitPar
Pr = 0.2
Ps = 0.5
Pp = 0.3

#InitVar
R = 33
S = 33
P = 33
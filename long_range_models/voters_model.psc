# Rock Scissors Paper model

# R + S  --> 2R, Pr
# P + R --> 2P, Pp
# S + P --> 2S, Ps
# R -> P, Pt

R1:
    R + S > R + R
    R*S*Pr

R2:
    S + P > S + S
    S*P*Ps

R3: 
    P + R > P + P
    P*R*Pp

R4:
    P > R
    P*Pt

# Parameters
Pr = 0.2
Ps = 0.5
Pp = 0.3
Pt = 0.5

# Init Values
R = 5000
S = 3000
P = 2000

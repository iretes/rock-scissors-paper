# Rock Scissors Paper model

# R + S  --> 2R, Pr
# P + R --> 2P, Pp
# S + P --> 2S, Ps

R1:
    R + S > R + R
    R*S*Pr

R2:
    S + P > S + S
    S*P*Ps

R3: 
    P + R > P + P
    P*R*Pp

# Parameters
Pr = 0.2
Ps = 0.5
Pp = 0.3

# Init Values
R = 33
S = 33
P = 33

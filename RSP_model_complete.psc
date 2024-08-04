# Rock Scissors Paper model

# R + S  --> S + 2R, Pr
# R + P --> P, Pp
# S + P --> P + 2S, Ps
# S + R --> R, Pr
# P + R --> R + 2P, Pp
# P + S --> S, Ps

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
    S*R*Pr

R5:
    P + R > R + P + P
    P*R*Pp

R6:
    P + S > S
    P*S*Ps

# Parameters
Pr = 0.2
Ps = 0.5
Pp = 0.3

# Init Values
R = 33
S = 33
P = 33

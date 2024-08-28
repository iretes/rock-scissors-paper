# Negative feedback loop

# G1 --> RP1, G1 + P1
# G2 --> RP2, G2 + P2
# G3 --> RP2, G3 + P3
# P1 + G2, RU1 <--> RB1, P1G2
# P2 + G3, RU2 <--> RB2, P2G3
# P3 + G1, RU3 <--> RB3, P3G1
# P1 --> RD1,
# P2 --> RD2,
# P3 --> RD3,

R1:
    G1 > G1 + P1
    G1*RP1

R2:
    G2 > G2 + P2
    G2*RP2

R3:
    G3 > G3 + P3
    G3*RP3

R4:
    P1 + G2 > P1G2
    P1*G2*RB1

R5:
    P1G2 > P1 + G2
    P1G2*RU1

R6:
    P2 + G3 > P2G3
    P2*G3*RB2

R7:
    P2G3 > P2 + G3
    P2G3*RU2

R8:
    P3 + G1 > P3G1
    P3*G1*RB3

R9:
    P3G1 > P3 + G1
    P3G1*RU3

R10:
    P1 > $pool
    P1*RD1

R11:
    P2 > $pool
    P2*RD2

R12:
    P3 > $pool
    P3*RD3

# Parameters
RP1 = 10
RP2 = 10000
RP3 = 10
RB1 = 10
RU1 = 2
RB2 = 0.1
RU2 = 20
RB3 = 10
RU3 = 20
RD1 = 1
RD2 = 100
RD3 = 1

# Init Values
P1 = 0
P2 = 0
P3 = 0
G1 = 1
G2 = 1
G3 = 1
P1G2 = 0
P2G3 = 0
P3G1 = 0

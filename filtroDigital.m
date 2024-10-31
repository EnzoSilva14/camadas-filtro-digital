s = tf('s');

wc = 1500;
num = wc^2 ;
den = s^2 + 2*wc*s + wc^2;
G = tf(num/den);
bode (G);
grid;
T = 1/44100;
H = c2d(G,T)

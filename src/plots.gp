# wxt terminal
#set terminal wxt size 350,262 enhanced font 'Verdana,10' persist
# png
set terminal pngcairo size 1350,700 enhanced font 'Verdana,10'
set output 'multiplot1.png'
# svg
#set terminal svg size 350,262 fname 'Verdana, Helvetica, Arial, sans-serif' \
#fsize '10'
#set output 'multiplot1.svg'

# color definitions
# set style line  1 lc rgb '#0060ad' pt 5 ps 0.2 lt 1 lw 2    # blue

unset key

set xlabel 't [ps]'
set grid ytics lt 0 lw 1 lc rgb "#bbbbbb"
set grid xtics lt 0 lw 1 lc rgb "#bbbbbb"


file = 'state_output'

### Start multiplot (2x2 layout)
set multiplot layout 2,2 rowsfirst

# --- GRAPH Temperature
set ylabel 'T [K]'
set label 1 'T' at graph 0.92,0.9 font ',8'

T(x) = a1*x + b1            # define the function to be fit
a1 = 0.1; b1 = 1;            # initial guess for a1 and b1      
fit T(x) file using 1:2 via a1, b1

plot file using 1:2 with points, T(x)

# --- GRAPH Pressure ---
set ylabel 'P [atm]'
set label 1 'P' at graph 0.92,0.9 font ',8'

f2(x) = a2*x + b2            # define the function to be fit
a2 = 1e-7; b2 = 1;            # initial guess    
fit f2(x) file using 1:3 via a2, b2

plot file using 1:3 with points

# --- GRAPH Potential Energy
set ylabel 'V [kJ/mol]'
set label 1 'V' at graph 0.92,0.9 font ',8'

f3(x) = a3*x + b3            # define the function to be fit
a3 = 0.1; b3 = 1;            # initial guess    
fit f3(x) file using 1:4 via a3, b3

plot file using 1:4 with points, f3(x)
# --- GRAPH Total Energy
set ylabel 'E [kJ/mol]'
set label 1 'E' at graph 0.92,0.9 font ',8'

f4(x) = a4*x + b4           # define the function to be fit
a4 = 0.1; b4 = 1;            # initial guess    
fit f4(x) file using 1:5 via a4, b4

plot file using 1:5 with points, f4(x)

unset multiplot
### End multiplot

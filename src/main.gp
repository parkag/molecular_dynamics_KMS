set term gif animate delay 20 size 800, 800
set output "point.gif"
set size square
set view 15,30

particles = 5
N = particles ** 3
do for [n=0:200] {
	splot [-5:5][-5:5][-5:5] "simulation_output" using 1:2:3 every ::((n* N)+1)::((n+1)*N) title sprintf("n=%i", n)
}

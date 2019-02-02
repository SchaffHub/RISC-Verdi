vcs:
	vcs -top tb -full64 -sverilog -lca -kdb -debug_access+all -timescale=1ns/1ps -f files.f
	simv

clean:
	rm -f simv ucli.key *.vcd
	rm -rf simv.daidir
	rm -rf csrc

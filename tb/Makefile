#vcs:
#	vcs -top tb -full64 -sverilog -lca -kdb -debug_access+all -timescale=1ns/1ps -f files.f
#	simv
V_TOP           = tb

# VCS three step flow.
# Analyze (AN)
V_AN_CMD        = vlogan
V_AN_SWITCHES   = -full64 -sverilog -timescale=1ns/1ps
V_AN_DEFINES    =

# Elaborate (EL)
V_EL_CMD        = vcs
V_EL_SWITCHES   = -full64 -lca -kb -debug_access+all

# Simulate (SM)
V_SM_CMD        = ./simv

vcs:
	$(V_AN_CMD) $(V_AN_SWITCHES) $(V_AN_DEFINES) -f files.f
	$(V_EL_CMD) $(V_EL_SWITCHES) $(V_TOP)
	$(V_SM_CMD)

clean:
	rm -f simv ucli.key *.vcd
	rm -rf simv.daidir
	rm -rf csrc
	rm -rf AN.DB
	rm -f vc_hdrs.h
	rm -f trace_core_00_0.log

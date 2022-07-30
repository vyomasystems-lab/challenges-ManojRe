
# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)
 
# for design with no bug
#VERILOG_SOURCES = $(PWD)/seqdetea.v

# for design with bug
VERILOG_SOURCES = $(PWD)/seqdetea_buggy.v

TOPLEVEL := seqdetea       # design
MODULE   := test_seqdetea     # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 

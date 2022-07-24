# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection1 """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    
    # input driving 
    for i in range(2):
        dut.inp_bit.value = 1
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')

    for i in range(1):
        dut.inp_bit.value = 0
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')

    for i in range(2):
        dut.inp_bit.value = 1
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')
    
    await Timer(2, units='ns')
    dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')
    assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {int(dut.seq_seen.value)} != 1."

@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection2 """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    
    # input driving 
    for i in range(2):
        dut.inp_bit.value = 1
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')

    for i in range(1):
        dut.inp_bit.value = 0
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')

    for i in range(3):
        dut.inp_bit.value = 1
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')
    for i in range(1):
        dut.inp_bit.value = 0
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')

    for i in range(2):
        dut.inp_bit.value = 1
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')
    
    await Timer(2, units='ns')
    dut._log.info(f'Inp={dut.inp_bit.value} current_sta={dut.current_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.seq_seen.value}')
    assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {int(dut.seq_seen.value)} != 1."


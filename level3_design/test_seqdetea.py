
import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_seqdetea_bug(dut):
    """Test for seq detection1 """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset/clear
    dut.clr.value = 1
    await FallingEdge(dut.clk)  
    dut.clr.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test1 here! ######')
    
    # input driving 
    for i in range(2):
        dut.din.value = 1
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.din.value} present_sta={dut.present_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.dout.value}')

    for i in range(2):
        dut.din.value = 0
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.din.value} present_sta={dut.present_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.dout.value}')

    for i in range(3):
        dut.din.value = 1
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.din.value} present_sta={dut.present_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.dout.value}')
    for i in range(1):
        dut.din.value = 0
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.din.value} present_sta={dut.present_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.dout.value}')

    for i in range(1):
        dut.din.value = 1
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.din.value} present_sta={dut.present_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.dout.value}')
    for i in range(1):
        dut.din.value = 0
        await RisingEdge(dut.clk)
        dut._log.info(f'Inp={dut.din.value} present_sta={dut.present_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.dout.value}')


    #await Timer(2, units='ns')
    dut._log.info(f'Inp={dut.din.value} present_sta={dut.present_state.value} next_sta={dut.next_state.value} clk={int(dut.clk)} DUT={dut.dout.value}')
    assert dut.dout.value == 1, f"Seq detector is incorrect: {dut.dout.value} != 1."


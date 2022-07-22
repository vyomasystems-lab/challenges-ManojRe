# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    SEL = 5'b1101
    INP13 = 1
    # input driving
    dut.inp13.value = INP13
    dut.sel.value = SEL
    await Timer(2, units='ns')

    assert dut.sel.value == INP13, f"Multiplexer selection is incorrect: {dut.sel.value} != 1"

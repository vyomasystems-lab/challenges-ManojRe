# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    Not_inp13 = 0
    SEL = 13
    INP13 = 1
    # input driving
    dut.inp13.value = INP13
    dut.inp12.value = Not_inp13
    dut.sel.value = SEL
    await Timer(2, units='ns')
    dut._log.info(f'Sel={SEL:05} Inp13={INP13:05} Output={INP13:05} DUT={int(dut.out.value):05}')
    assert int(dut.out.value) == INP13, f"Multiplexer selection is incorrect: {int(dut.out.value)} != 1.\nThis Bug Ocurred Because in Verilog code, Mux Select Case for inp12 and inp13 is same which is 13 or b01101."


@cocotb.test()
async def test_mux2(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    SEL = 30
    INP30 = 1
    # input driving
    dut.inp30.value = INP30
    dut.sel.value = SEL
    await Timer(2, units='ns')
    dut._log.info(f'Sel={SEL:05} Inp30={INP30:05} Output={INP30:05} DUT={int(dut.out.value):05}')
    assert int(dut.out.value) == INP30, f"Multiplexer selection is incorrect: {int(dut.out.value)} != 1.\nThis Bug Ocurred Because in Verilog code, Mux Select Case for inp30 is not written, so output is 0 which is default \ncase."

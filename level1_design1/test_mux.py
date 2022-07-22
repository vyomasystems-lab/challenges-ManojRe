# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    Not_inp13 = 0
    SEL = 13
    INP13 = 1
    # input driving
    dut.inp13.value = INP13
    # dut.inp0.value = Not_inp13
    # dut.inp1.value = Not_inp13
    # dut.inp2.value = Not_inp13
    # dut.inp3.value = Not_inp13
    # dut.inp4.value = Not_inp13
    # dut.inp5.value = Not_inp13
    # dut.inp6.value = Not_inp13
    # dut.inp7.value = Not_inp13
    # dut.inp8.value = Not_inp13
    # dut.inp9.value = Not_inp13
    # dut.inp10.value = Not_inp13
    # dut.inp11.value = Not_inp13
    dut.inp12.value = Not_inp13
    # dut.inp14.value = Not_inp13
    # dut.inp15.value = Not_inp13
    # dut.inp16.value = Not_inp13
    # dut.inp17.value = Not_inp13
    # dut.inp18.value = Not_inp13
    # dut.inp19.value = Not_inp13
    # dut.inp20.value = Not_inp13
    # dut.inp21.value = Not_inp13
    # dut.inp22.value = Not_inp13
    # dut.inp23.value = Not_inp13
    # dut.inp24.value = Not_inp13
    # dut.inp25.value = Not_inp13
    # dut.inp26.value = Not_inp13
    # dut.inp27.value = Not_inp13
    # dut.inp28.value = Not_inp13
    # dut.inp29.value = Not_inp13
    #dut.inp30.value = Not_inp13
    dut.sel.value = SEL
    await Timer(2, units='ns')
    dut._log.info(f'Sel={SEL:05} Inp13={INP13:05} Output={INP13:05} DUT={int(dut.out.value):05}')
    assert int(dut.out.value) == INP13, f"Multiplexer selection is incorrect: {int(dut.out.value)} != 1. This Bug Ocurred Because in Verilog code of Mux Select Case for inp12 and inp13 is same which is 13 or b01101"

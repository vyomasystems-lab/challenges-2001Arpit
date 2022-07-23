# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""

    sel0 = 12
    sel1 = 13

    in0 = 1
    in1 = 3

    dut.inp12.value = in0;
    dut.inp13.value = in1;

    dut.sel.value = sel1;    #Output should have the value of inp13

    await Timer(2, units='ns')

    assert dut.out.value == in1, f"Multiplexer output is incorrect: {dut.out.value} != {dut.inp13.value}"

@cocotb.test()
async def test_mux2(dut):

    sel = 30

    inp = 3

    dut.inp30.value = inp
    dut.sel.value = sel

    await Timer(2, units='ns')

    assert dut.out.value == inp, f"Multiplexer output is incorrect: {dut.out.value} != {dut.inp30.value}"

    #cocotb.log.info('##### CTB: Develop your test here ########')

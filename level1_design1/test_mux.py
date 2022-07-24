# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""


    dut.inp0.value = random.randint(0,3)
    dut.inp1.value = random.randint(0,3)
    dut.inp2.value = random.randint(0,3)
    dut.inp3.value = random.randint(0,3)
    dut.inp4.value = random.randint(0,3)
    dut.inp5.value = random.randint(0,3)
    dut.inp6.value = random.randint(0,3)
    dut.inp7.value = random.randint(0,3)
    dut.inp8.value = random.randint(0,3)
    dut.inp9.value = random.randint(0,3)
    dut.inp10.value = random.randint(0,3)
    dut.inp11.value = random.randint(0,3)
    dut.inp12.value = random.randint(0,3)
    dut.inp13.value = random.randint(0,3)
    dut.inp14.value = random.randint(0,3)
    dut.inp15.value = random.randint(0,3)
    dut.inp16.value = random.randint(0,3)
    dut.inp17.value = random.randint(0,3)
    dut.inp18.value = random.randint(0,3)
    dut.inp19.value = random.randint(0,3)
    dut.inp20.value = random.randint(0,3)
    dut.inp21.value = random.randint(0,3)
    dut.inp22.value = random.randint(0,3)
    dut.inp23.value = random.randint(0,3)
    dut.inp24.value = random.randint(0,3)
    dut.inp26.value = random.randint(0,3)
    dut.inp27.value = random.randint(1,3)
    dut.inp28.value = random.randint(1,3)
    dut.inp29.value = random.randint(1,3)
    dut.inp30.value = random.randint(1,3)

    arr[31]=[dut.inp0.value,dut.inp1.value,dut.inp2.value,dut.inp3.value,dut.inp4.value,dut.inp5.value,dut.inp6.value,dut.inp7.value,dut.inp8.value,
    dut.inp9.value,dut.inp10.value,dut.inp11.value,dut.inp12.value,dut.inp13.value,dut.inp14.value,dut.inp15.value,dut.inp16.value,dut.inp17.value,
    dut.inp18.value,dut.inp19.value,dut.inp20.value,dut.inp21.value,dut.inp22.value,dut.inp23.value,dut.inp24.value,dut.inp25.value,dut.inp26.value,
    dut.inp27.value,dut.inp28.value,dut.inp29.value,dut.inp30.value]

    for i in range(31):
        


    dut.sel.value = i;    

    await Timer(2, units='ns')
   
    assert dut.out.value == dut.inp0.value, f"Multiplexer output is incorrect: {dut.out.value} != {arr[i]}"
    



@cocotb.test()
async def test_mux2(dut):

    sel = 30

    inp = 3

    dut.inp30.value = inp
    dut.sel.value = sel

    await Timer(2, units='ns')

    assert dut.out.value == inp, f"Multiplexer output is incorrect: {dut.out.value} != {dut.inp30.value}"

    #cocotb.log.info('##### CTB: Develop your test here ########')

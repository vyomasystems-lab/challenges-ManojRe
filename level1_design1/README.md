 # 31:1 MUX Design Verification
    There are two bugs in this MUX Design
 ![LVL1des1](https://user-images.githubusercontent.com/86054925/180403436-cdc9db7a-1bca-4769-b3da-4004df41adb8.png)
 ![LVL1des11](https://user-images.githubusercontent.com/86054925/180415773-40a3f824-9f0c-4550-9532-a0f63053d9f6.png)

## Verification Environment

The test drives inputs to the Design Under Test (mux module here) which takes in 5-bit input *sel* to select input from inp0 to inp 30 and gives 2-bit output *out*.

Case1: The values are assigned to the input port using 
```
dut.inp13.value = 1 
dut.inp12.value = 0
dut.sel.value = 13
```
Case2: The values are assigned to the input port using 
```
dut.inp30.value = 2
dut.sel.value = 30
```

The assert statement is used for comparing the MUX's output to the expected value.

The following error is seen:
```
assert int(dut.out.value) == INP13, f"Multiplexer selection is incorrect: {int(dut.out.value)} != 1."
                     AssertionError: Multiplexer selection is incorrect: 0 != 1.
                     This Bug Ocurred Because in Verilog code, Mux Select Case for inp12 and inp13 is same which is 13 or b01101.
```
```
assert int(dut.out.value) == INP30, f"Multiplexer selection is incorrect: {int(dut.out.value)} != 2."
                     AssertionError: Multiplexer selection is incorrect: 0 != 2.
                     This Bug Ocurred Because in Verilog code, Mux Select Case for inp30 is not written, so output is 0 which is default case.
                     
```
## Test Scenario **(Important)**
TEST1:
- Test Inputs: sel=13 inp12=0 inp13=1
- Expected Output: out=1
- Observed Output in the DUT dut.out=0
TEST2:
- Test Inputs: sel=30 inp30=2
- Expected Output: out=2
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(sel or inp0  or inp1 or  inp2 or inp3 or inp4 or inp5 or inp6 or
            inp7 or inp8 or inp9 or inp10 or inp11 or inp12 or inp13 or 
            inp14 or inp15 or inp16 or inp17 or inp18 or inp19 or inp20 or
            inp21 or inp22 or inp23 or inp24 or inp25 or inp26 or inp27 or 
            inp28 or inp29 or inp30 )

  begin
    case(sel)
      5'b00000: out = inp0;
      .
      .
      5'b01101: out = inp12; ====> BUG //here it should be 1100 for 12
      .
      .
      5'b11101: out = inp29;  ====> BUG // after this condition 31st i.e inp30 is not written
      default: out = 0;
    endcase             
  end
```
For the MUX design, the logic of select in case for inp12 should be ``5'b01100`` instead of ``5'b01101`` as in the design code.

For the MUX design, the logic of select in case for inp30 should be written as ``5'b11110: out = inp30;``.

## Design Fix
Updating the design and re-running the test makes the test pass.

![LVL1des1_bugfree](https://user-images.githubusercontent.com/86054925/180419974-239a53eb-cdcc-4618-99e8-10239ed3bcee.PNG)

The updated design is checked in as mux_bugfree.v

## Verification Strategy

The MUX design is simple so I directly started with checking Verilog Code and finding whether there is any design bug and gone through whole code from start to end each line, since the bug can be a minute bug. For Example in  
```
always @(sel or inp0 or ... )
```
there can be any parameter missing or instead of "or", "and" could be written, etc.,
While analyzing this I found bugs in the design and developed testbench according to it.

## Is the verification complete ?

Yes, to confirm it I tested it for some possible testcases and all testcases were passed.
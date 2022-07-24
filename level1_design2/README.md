 # 1011_Sequence Detector  Design Verification
    There are Four bugs in this Sequence Detector Design

## Verification Environment

The test drives inputs to the Design Under Test (seq_detect_1011 module here) which takes series of 1-bit input *inp_bit* and gives 1-bit output *seq_seen* whether "1011" sequence detected or not.

The values are assigned to the input port using 
```
for i in range(2):
        dut.inp_bit.value = 1
        await RisingEdge(dut.clk)
```
and sequence of input passed like 110101..., etc.,

The assert statement is used for comparing the Sequence Detector output to the expected value.

The following error is seen:
Bug1:
```
assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {dut.seq_seen.value} != 1..."
                     AssertionError: Seq detector is incorrect: 0 != 1.
                     This Bug Ocurred Because in Verilog code, Seq_detect Select Case of SEQ_1 'if' part should be SEQ_1 itself not IDEL, Because here we consider overlapping i.e. for I/P 11011.
```
Bug2:
```
assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {dut.seq_seen.value} != 1..."
                     AssertionError: Seq detector is incorrect: 0 != 1.
                     This Bug Ocurred Because in Verilog code, Seq detect Select Case of SEQ_101 'else' part should be SEQ_10 not IDEL, Because here we consider overlapping i.e. for I/P 101011.
                     
```
Bug3:
```
assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {dut.seq_seen.value} != 1..."
                     AssertionError: Seq detector is incorrect: 0 != 1.
                     This Bug Ocurred Because in Verilog code, Seq_detect Select Case of SEQ_1011 should be SEQ_1 not IDEL, Because here we consider overlapping i.e. for I/P 10111011.
```
Bug4:
```
assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {dut.seq_seen.value} != 1..."
                     AssertionError: Seq detector is incorrect: 0 != 1.
                     This Bug Ocurred Because in Verilog code, Seq_detect Select Case of SEQ_1011 should have 'if and else' case and if i/p is '1' then next_state is SEQ_1 else next_state is SEQ_10, Because here we consider overlapping 
                     i.e. for I/P 1011011.
```

## Test Scenario **(Important)**
- Test Inputs: sel=13 inp12=0 inp13=1
- Expected Output: out=1
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
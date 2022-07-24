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
                     This Bug Ocurred Because in Verilog code, Seq_detect Select Case of SEQ_1 'if' part should be SEQ_1 itself not IDLE, Because here we consider overlapping i.e. for I/P 11011.
```
Bug2:
```
assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {dut.seq_seen.value} != 1..."
                     AssertionError: Seq detector is incorrect: 0 != 1.
                     This Bug Ocurred Because in Verilog code, Seq detect Select Case of SEQ_101 'else' part should be SEQ_10 not IDLE, Because here we consider overlapping i.e. for I/P 101011.
                     
```
Bug3:
```
assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {dut.seq_seen.value} != 1..."
                     AssertionError: Seq detector is incorrect: 0 != 1.
                     This Bug Ocurred Because in Verilog code, Seq_detect Select Case of SEQ_1011 should be SEQ_1 not IDLE, Because here we consider overlapping i.e. for I/P 10111011.
```
Bug4:
```
assert dut.seq_seen.value == 1, f"Seq detector is incorrect: {dut.seq_seen.value} != 1..."
                     AssertionError: Seq detector is incorrect: 0 != 1.
                     This Bug Ocurred Because in Verilog code, Seq_detect Select Case of SEQ_1011 should have 'if and else' case and if i/p is '1' then next_state is SEQ_1 else next_state is SEQ_10, Because here we consider overlapping 
                     i.e. for I/P 1011011.
```

## Test Scenario **(Important)**
TEST1:
- Test Inputs: inp_bit = 11011
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

TEST2:
- Test Inputs: inp_bit = 1101011
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

TEST3:
- Test Inputs: inp_bit = 110111011
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

TEST4:
- Test Inputs: inp_bit = 11011011
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

Expected Output is not seen for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(inp_bit or current_state)
  begin
    case(current_state)
      IDLE:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = IDLE;
      end
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;   ====> BUG //next_state should be SEQ_1
      .
      .
      .
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE; ====> BUG //next_state should be SEQ_10
      end
      SEQ_1011:
      begin
        next_state = IDLE; ====> BUG //if inp_bit = 1, then next_state should be SEQ_1, else SEQ_10
      end
    endcase
  end
```
For the Sequence Detector design:

The logic of SEQ_1 in case for inp_bit = 1, next_state should be ``SEQ_1`` instead of ``IDLE`` as in the design code.
The logic of SEQ_101 in case for inp_bit=0, i.e. else part next_state should be ``SEQ_10`` instead of ``IDLE``
The logic of SEQ_1011 in case if inp_bit=1, next_state should be ``SEQ_1`` else ``SEQ_10``.

## Design Fix
Updating the design and re-running the test makes the test pass.


The updated design is checked in as seq_detect_1011_bugfree.v

## Verification Strategy

The MUX design is simple so I directly started with checking Verilog Code and finding whether there is any design bug and gone through whole code from start to end each line, since the bug can be a minute bug. For Example in  
```
always @(sel or inp0 or ... )
```
there can be any parameter missing or instead of "or", "and" could be written, etc.,
While analyzing this I found bugs in the design and developed testbench according to it.

## Is the verification complete ?

Yes, to confirm it I tested it for some possible testcases and all testcases were passed.
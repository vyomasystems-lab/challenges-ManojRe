 # 1011_Sequence Detector  Design Verification
    There are Four bugs in this Sequence Detector Design
   ![LvL1_Des2_1](https://user-images.githubusercontent.com/86054925/180816206-bd3b23b9-63cb-4cdb-b6b5-5eb190397335.PNG)
   ![LvL1_Des2_2](https://user-images.githubusercontent.com/86054925/180816229-7a834a42-2e27-4f8c-829c-d586d4b64998.PNG)
   ![LvL1_Des2_3](https://user-images.githubusercontent.com/86054925/180816274-d787b03b-133a-49a5-a9b4-5b31d7c29d8b.PNG)


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
Updating the design One-by-One and re-running the test makes the test pass.

After Fixing SEQ_1 Bug: 
![LvL1_Des2_P1](https://user-images.githubusercontent.com/86054925/180838438-72da21d1-1ae0-4681-91ec-421ac1f99a13.PNG)

After Fixing SEQ_101 Bug: 
![LvL1_Des2_P2](https://user-images.githubusercontent.com/86054925/180838455-10205acc-e9bd-4501-99df-9de3f45b7145.PNG)

After Fixing SEQ_1011 Bug Part_1: 
![LvL1_Des2_P3](https://user-images.githubusercontent.com/86054925/180838466-ffc57df3-ec82-4aee-81bb-109157262593.PNG)

After Fixing SEQ_1011 Bug Part_2: 
![LvL1_Des2_P4](https://user-images.githubusercontent.com/86054925/180838476-27751eda-7ea5-4582-ad08-35c5e015e719.PNG)


The fully updated design is checked in as seq_detect_1011_bugfree.v

## Verification Strategy

The Seq_detect_1011 design is clock based so first i started with checking Verilog Code and finding whether there is any design bug and gone through whole code from start to end, while making test cases I got problems when I wanted to give input as ``11011`` in testbench code, i got some different Input like ``11001``, so i started checking it and understood that the time and trigger I have given were wrong caz of some internal time difference in this systen. And finally gave different combinations of input with this I got total 4 bugs and tried to solve all 4 bugs and saved in ``seq_detect_1011_bugfree.v`` file.

## Is the verification complete ?

Yes, after giving different input combinations for testing and running all 4 testcases with corrected code they all passed.

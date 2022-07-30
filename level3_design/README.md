 # 11010_Sequence Detector  Design Verification
    The Design is selected with no bugs present in this Sequence Detector Design
   ![LvL3_Des](https://user-images.githubusercontent.com/110245741/181879931-b3f77454-9e9f-4734-b596-a0ff07ab14d6.PNG)


## Verification Environment

The test drives inputs to the Design Under Test (seqdetea module here) which takes series of 1-bit input *din* and gives 1-bit output *dout* whether "11010" sequence detected or not.

The values are assigned to the input port using 
```
for i in range(2):
        dut.din.value = 1
        await RisingEdge(dut.clk)
```
and sequence of input passed like 11010..., etc.,

The assert statement is used for comparing the Sequence Detector output to the expected value.
And here we used non-buggy design, so expected value is equal to Seq. Detector design value

## Adding Bug to the Design
Sequence Detector can easily get buggy for complex design, the states gets mismatched easily cause of complexity it tends to happen.
```
S2 : if (din == 0)
                  next_state <= S3;
              else 
                  next_state <= S1;
```
here I introduced bug in the else part of S2, ``next_state`` assigned ``S1`` instead of ``S0`` state value.

## Test Scenario **(Important)**
TEST1:
- Test Inputs: din = 1100111010
- Expected Output: dout=1
- Observed Output in the DUT dut.dout=0

Expected Output is not seen for the above inputs, since we introduced bug in the design.

## Buggy Design
here after passing input of TEST1 case from above, we can see in the screenshot expected output is not equal to 1. 
![LvL3_Des_bug](https://user-images.githubusercontent.com/110245741/181880816-a47a1fbf-49e9-4e20-87ef-5de28287c1a3.PNG)

## Design Solution 
This Design can be easily solved by testing with different type of input such that it goes else part of each states i.e. from S0 to S4. With this we get in which part bug is and correct them accordingly.

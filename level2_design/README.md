 # Bitmanip Co-processor Design Verification
    There is a bugs in this Bitmanip Co-processor Design
   ![LvL2_Des](https://user-images.githubusercontent.com/110245741/182029805-96d0c881-d100-495f-8039-dca25b5c14b7.PNG)

## Verification Environment

The test drives inputs to the Design Under Test (mkbitmanip module here) which takes 4 inputs namely *mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2 and mav_putvalue_src3* each of 32-bit input and gives 33-bit output *mav_putvalue*.

The values are assigned to the input port using 
```
for i in range(5):

        mav_putvalue_src1 = random.randint(0, 4294967295)
        mav_putvalue_src2 = random.randint(0, 4294967295)
        mav_putvalue_src3 = random.randint(0, 4294967295)
        ....
```
and running 5 different inputs for all type of operation like ANDN, ORN, etc., 

The assert statement is used for comparing the Bitmanip Co-processor output to the expected value from *model_mkbitmanip.py*.
The following error is seen:
```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x101818e41 does not match MODEL = 0x844201a3
```

## Test Scenario **(Important)**
TEST1:
- Test Inputs: mav_putvalue_src1=0xc2e1c7f1, mav_putvalue_src2=0x9ccac72a, mav_putvalue_instr=0x40007033, EN_mav_putvalue=1.
- Expected Output: expected_mav_putvalue==0x844201a3
- Observed Output in the DUT mav_putvalue=0x101818e41

All *.._src* inputs are randomly generated with all possible value i.e. from 0x0 to 0xffffffff.
Expected Output is not seen for the above random inputs, proving that there is a design bug.

## Design Bug
Based on the above test input and analysing the design, we see the following

```
...
assign field1__h109 =
	     (mav_putvalue_instr[31:25] == 7'b0100000 &&
	      x__h254 == 10'b1110110011) ?
	       x__h39889 :
...
assign field1__h2958 = x__h39889 | y__h39890 ;
...
assign y__h39890 = mav_putvalue_src3 & y__h39891 ;
assign y__h39891 = ~mav_putvalue_src2 ;
...
```
While going through the verilog code the above code has involvement *mav_putvalue_src3*, but ``ANDN`` function is independent of *mav_putvalue_src3*, so the design bug is seen here.

## Verification Strategy
Since this design is complicated so normal understanding of whole verilog code wont be possible, so running all function with different combination input and trying to understand verilog code and comparing with *model_mkbitmanip.py* is what I did. With this I found bug in ``ANDN`` function.

## Is the verification complete ?
Yes, I tested for all possible function with the help of *model_mkbitmanip.py* file and used possible different random values as input, with this I verified the Bitmanip Co-processor Design.

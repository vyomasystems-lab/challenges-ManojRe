 # 31:1 MUX Design Verification

 ![LVL1des1](https://user-images.githubusercontent.com/86054925/180403436-cdc9db7a-1bca-4769-b3da-4004df41adb8.png)
 ![LVL1des11](https://user-images.githubusercontent.com/86054925/180406982-3e33830c-cb53-4ea4-8c30-bf1c50b07dec.png)

## Verification Environment

The test drives inputs to the Design Under Test (mux module here) which takes in 5-bit input *sel* to select input from inp0 to inp 30 and gives 2-bit output *out*.

The values are assigned to the input port using 
```
dut.inp13.value = 1 
dut.inp12.value = 0
dut.sel.value = 13
```


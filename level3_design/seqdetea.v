
module seqdetea(clk, clr, din, dout);

  output dout;
  input din;
  input clr;
  input clk;
  
  reg [2:0] present_state, next_state;
  parameter S0 = 3'b000, S1 = 3'b001, S2 = 3'b10,  S3 = 3'b011, S4 = 3'b100;

  assign dout = present_state == S4 ? 1 : 0;

  always @(posedge clk or posedge clr) begin
      if (clr == 1)
          present_state <= S0;
      else
          present_state <= next_state;
  end

  always @(*) begin
      case (present_state)
          S0 : if (din == 1)
                  next_state <= S1;
              else 
                  next_state <= S0;
          S1 : if (din == 1)
                  next_state <= S2;
              else 
                  next_state <= S0;
          S2 : if (din == 0)
                  next_state <= S3;
              else 
                  next_state <= S2;
          S3 : if (din == 1)
                  next_state <= S4;
              else 
                  next_state <= S0;
          S4 : if (din == 0)
                  next_state <= S0;
              else 
                  next_state <= S2;           
          default : next_state <= S0;
      endcase
  end
    
  endmodule

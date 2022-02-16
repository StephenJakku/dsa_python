from stack import Stack

def convert_int_to_bin(dec_num):
  s=Stack()
  ans=""
  while dec_num>0:
    s.push(dec_num%2)
    dec_num=dec_num//2
  while not s.isEmpty():
    ans+=str(s.pop())
  return ans

def main():
    input=242
    result=convert_int_to_bin(input)
    print(f"Decimal:{input}\nBinary:{result}")

main()
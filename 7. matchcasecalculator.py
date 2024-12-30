input1=int(input("ENTER THE FIRST NUMBER:"))
input2=int(input("ENTER THE SECOND NUMBER:"))

op=input("ENTER THE OPERATOR(*,/,+,-):")
match op:
    case "+":
        print(input1+input2)
    case "-":
        print(input1-input2)
    case "*":
        print(input1*input2)
    case "/":
        if input2==0:
            print("ERROR")
        else:
            print(input1/input2)
         



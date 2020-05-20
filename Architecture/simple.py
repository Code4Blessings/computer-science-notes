import sys
#DIV

PRINT_BEEJ = 1
HALT       = 2
PRINT_NUM =  3

memory = [
    PRINT_BEEJ,
    PRINT_NUM, #Opcode
    3, #argument
    PRINT_NUM,
    12,
    PRINT_BEEJ,
    PRINT_NUM,
    37,
    HALT
]

pc = 0 #program counter
running = True

while running:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")

    elif command == HALT:
        running = False
    
    elif command == PRINT_NUM:
        num = memory[pc + 1]
    
    else:
        print("Unknown instruction: {command}")
        sys.exit(1)

    pc +=1


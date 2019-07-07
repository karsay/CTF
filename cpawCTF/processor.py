tape = raw_input("plaintext: ")    
tape = list(tape)

for i in range(len(tape)):
    tape[i] = format(ord(tape[i]),"b")
    while len(tape[i]) != 8:
        tape[i] = "0" + tape[i]
tape = "".join(tape)
tape = list(tape)

ans = []

q = 0
for i in range(len(tape)):
    if q == 0:
        if tape[i] == "0":
            q = 0
            ans.append(str(q))
        elif tape[i] == "1":
            q = 1
            ans.append(str(q))
    elif q == 1:
        if tape[i] == "1":
            q = 1
            ans.append(str(q))
        elif tape[i] == "0":
            q = 0
            ans.append(str(q))

print "".join(ans)

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

result = {int(s.split(':')[0]): s.split(':')[1] for s in s.split()}
print(result)

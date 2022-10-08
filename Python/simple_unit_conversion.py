bits = int(input("Input a number of bits: "))
megabytes = bits//(8*1024*1024)
remaining_bits = bits % (8*1024*1024)
kilobytes = remaining_bits//(8*1024)
remaining_bits = remaining_bits % (8*1024)
bytes = remaining_bits//8
remaining_bits = remaining_bits % 8

print(bits, "b =", megabytes, "MB", kilobytes, "KB", bytes, "B", remaining_bits, "b" )
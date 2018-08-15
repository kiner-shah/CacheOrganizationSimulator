from Direct_Mapping_Cache_Organization import MainMemory

memory = MainMemory()
print "Initializing memory..."
memory.initialize_main_memory()
while True:
	try:
		value = int(raw_input("Enter the memory address to be accessed [0 - 16777215]: "))
		if value < 0 or value > 16777215:
			print "Value out of range entered"
			continue
		memory.search(value)
		x = raw_input("Continue (yes / no): ")
		if x == "no" or x == "n" or x == "NO" or x == "No":
			break
	except ValueError:
		print "Illegal value entered"

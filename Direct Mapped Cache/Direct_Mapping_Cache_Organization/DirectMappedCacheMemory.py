#from MainMemory import MainMemory
class DirectMappedCacheMemory:
	'''
	Assume,
	word address size = 24
	line address size = 14
	tag size = 8 (bits)
	word reference size = 2
	line size = 2^2 = 4 (words)
	no. of lines = 2^14
	total no. of words = 2^14 * 4 = 2^16

	Memory address of format:
	|---8----|--------14------|-2-|
	| tag    |    line        | w |
	'''
	LINE_SIZE = 4
	TAG_SIZE = 8
	TOT_NO_OF_LINES = 16384
	TOT_NO_OF_WORDS = 65536

	def __init__(self, memory):
		self.__words = [None] * self.TOT_NO_OF_WORDS
		self.__tags = [None] * self.TOT_NO_OF_LINES
		self.__main_memory = memory

	def __fill_cache_when_miss(self, tag_no, line_no):
		# print "tag = " + str(tag_no) + " line_no = " + str(line_no)
		start = ((tag_no << 14) | line_no) * self.LINE_SIZE
		end = ((tag_no << 14) | line_no) * self.LINE_SIZE + self.LINE_SIZE
		# print "start = " + str(start) + " end = " + str(end)
		self.__words[line_no * self.LINE_SIZE : (line_no + 1) * self.LINE_SIZE] = self.__main_memory.get_words_in_range(start, end)
		self.__tags[line_no] = tag_no
		# print self.__words[line_no * self.LINE_SIZE : (line_no + 1) * self.LINE_SIZE]

	def search_cache(self, addr):
		# relative word position = (n >> 0) & ((1 << 2) - 1)
		if addr >= self.__main_memory.TOT_NO_OF_WORDS:
			return
		relative_word_pos = addr & 3
		line_no = (addr >> 2) & ((1 << 14) - 1)
		tag_val = addr >> 16
		# print tag_val, line_no, bin(line_no), relative_word_pos
		if self.__tags[line_no] == None or self.__tags[line_no] != tag_val:
			print "Block not present in cache (Cache miss)"
			self.__fill_cache_when_miss(tag_val, line_no)
			print "Present in main memory: " + self.__main_memory.get_word(addr)
		elif self.__tags[line_no] == tag_val:
			print "Present in cache (Cache hit): " + self.__words[line_no * self.LINE_SIZE + relative_word_pos]
'''
memory = MainMemory()
memory.initialize_main_memory()
cache = DirectMappedCacheMemory(memory)
if cache.search_cache(10000000000000) == -1:
	pass
else:
	print "Illegal memory access attempt"
'''

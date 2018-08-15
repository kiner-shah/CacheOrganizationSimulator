from DirectMappedCacheMemory import DirectMappedCacheMemory
class MainMemory:
	'''
	Assume,
	word address size = 24
	no. of words = 2^24
	block size = 2^2 = 4
	no. of blocks = 2^24 / 2^2 = 2^22

	Memory address of format:
	|---8----|--------14------|-2-|
	| tag    |    line        | w |
	'''
	WORD_ADDR_SIZE = 24
	BLOCK_SIZE = 4
	TOT_NO_OF_WORDS = 16777216
	TOT_NO_OF_BLOCKS = 4194304

	def __init__(self):
		self.__words = [None] * self.TOT_NO_OF_WORDS

	def initialize_main_memory(self):
		self.__words = ["Word = " + str(i) for i in range(self.TOT_NO_OF_WORDS)]
		self.__cache = DirectMappedCacheMemory(self)
		# print "initialized " + str(i) + "th memory location with value " + self.__words[i]

	def get_word(self, addr):
		return self.__words[addr]

	def get_words_in_range(self, start, end):
		return self.__words[start : end]

	def search(self, addr):
		self.__cache.search_cache(addr)

'''
# for testing
memory = MainMemory()
import time
start = time.time()
memory.initialize_main_memory()
end = time.time()
print end - start
print memory.get_word(296), type(memory.get_word(296))
'''

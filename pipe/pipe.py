import os, sys, itertools, math

class Pipe:
	def __init__(self, function):
		self.function = function
	def __call__(self, *args, **kwargs):
		@Pipe
		def piped(argument):
			return self.function(argument, *args, **kwargs)
		return piped
	def __ror__(self, other):
		return self.function(other)

@Pipe
def reverse(iterable):
	return iterable[::-1]

@Pipe
def identity(object):
	return object

@Pipe
def sort(iterable):
	return (''.join if type(iterable) == str else identity.function)(sorted(iterable))

@Pipe
def as_list(iterable):
	return list(iterable)

@Pipe
def as_tuple(iterable):
	return tuple(iterable)

@Pipe
def as_set(iterable):
	return set(iterable)

@Pipe
def set(iterable):
	return {entry for entry in iterable}

@Pipe
def generator(iterable):
	return (entry for entry in iterable)

@Pipe
def string(object):
	return str(object)

@Pipe
def foreach(iterable, function):
	return list(map(function, iterable))

@Pipe
def join(iterable, joiner = ', '):
	return joiner.join(map(str, iterable))

@Pipe
def evaluate(object):
	return eval(str(object))

@Pipe
def flatten(iterable):
	array = []
	for entry in iterable:
		if hasattr(entry, '__iter__'):
			array.extend(flatten.function(entry))
		else:
			array.append(entry)
	return array

@Pipe
def stdout(object):
	sys.stdout.write(str(object))

@Pipe
def lineout(object):
	sys.stdout.write(str(object) + os.linesep)

@Pipe
def stdin(object = ''):
	return input(str(object))

@Pipe
def sum(iterable):
	if iterable:
		entry = type(iterable[0])()
		for item in iterable:
			entry += item
		return entry
	else:
		return 0

add = Pipe(lambda a, b: a + b)
mul = Pipe(lambda a, b: a * b)
div = Pipe(lambda a, b: a / b)
sub = Pipe(lambda a, b: a - b)

floor = Pipe(int)
ceil = Pipe(math.ceil)

floordiv = Pipe(lambda x, y: x // y)

@Pipe
def take_while(iterable, predicate):
	return list(itertools.takewhile(predicate, iterable))

@Pipe
def increments(iterable):
	return [iterable[index] - iterable[index - 1] for index in range(1, len(iterable))]

@Pipe
def filter(iterable, predicate):
	return [entry for entry in iterable if predicate(entry)]

@Pipe
def filter_out(iterable, predicate):
	return [entry for entry in iterable if not predicate(entry)]

@Pipe
def all(iterable, predicate = identity.function):
	for entry in iterable:
		if not predicate(entry):
			return False
	return True

@Pipe
def any(iterable, predicate = identity.function):
	for entry in iterable:
		if predicate(entry):
			return True
	return False

@Pipe
def thousand(number):
	return number * 1000

@Pipe
def million(number):
	return number * 1000 * 1000

@Pipe
def billion(number):
	return number * 1000 * 1000 * 1000

@Pipe
def trillion(number):
	return number * 1000 * 1000 * 1000 * 1000

@Pipe
def quadrillion(number):
	return number * 1000 * 1000 * 1000 * 1000 * 1000

@Pipe
def invert(boolean):
	return not boolean

def lessthan(number):
	return lambda x: x < number

def morethan(number):
	return lambda x: x > number

def fib():
	x = 0
	y = 1
	while True:
		yield y
		x, y = y, x + y

def pows(base = 2):
	x = 1
	while True:
		yield x
		x *= base

if __name__ == '__main__':
	2 | add(2) | mul(4) | lineout

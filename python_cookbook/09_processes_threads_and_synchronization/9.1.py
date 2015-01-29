#!/usr/bin/python

def wrap_callable(any_callable, before, after):
	'''wrap any callable with before/after calls'''
	def _wrapped(*a, **kw):
		before()
		try:
			return any_callable(*a, **kw)
		finally:
			after()
	return _wrapped
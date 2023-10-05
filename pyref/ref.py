from typing import Self


class Ref[T]:
	value: T

	def __init__(self, value: T) -> None:
		self.value = value

		for attr in dir(value):
			if attr == '__class__':
				continue
			method = getattr(value, attr)
			if callable(method):
				def f(*args, **kwargs):
					args = [arg.value if isinstance(arg, Ref) else arg for arg in args]
					kwargs = {k: v.value if isinstance(v, Ref) else v for k, v in kwargs.items()}
					return method(*args, **kwargs)
				setattr(self, attr, f)

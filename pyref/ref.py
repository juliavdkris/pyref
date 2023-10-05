from typing import Self


class Ref[T]:
	value: T

	def __init__(self, value: T) -> None:
		self.value = value

		for attr in dir(value):
			if attr == '__class__':
				continue
			setattr(self, attr, lambda *args: getattr(self.value, attr)(*args))

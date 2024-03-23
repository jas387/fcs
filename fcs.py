import flet

class Storage:
	__PAGE: flet.Page = None
	__NAME = 'com.example.app'
	
	@classmethod
	def set_page(cls, page: flet.Page):
		cls.__PAGE = page

	@classmethod
	def set_name(cls, name: str):
		cls.__NAME = name

	@classmethod
	def _check_page(cls):
		if cls.__PAGE is None:
			raise ValueError('Storage.set __PAGE is None!')

	@classmethod
	def set(cls, key:str, value: object):
		cls._check_page()
		return cls.__PAGE.client_storage.set(f'{cls.__NAME}.{key}',value)

	@classmethod
	def get(cls, key: str):
		cls._check_page()
		return cls.__PAGE.client_storage.get(f'{cls.__NAME}.{key}')

	@classmethod
	def contains_key(cls, key: str):
		cls._check_page()
		return cls.__PAGE.client_storage.contains_key(f'{cls.__NAME}.{key}')

	@classmethod
	def get_keys(cls, prefix: str):
		cls._check_page()
		return cls.__PAGE.client_storage.get_keys(f'{cls.__NAME}.{prefix}')

	@classmethod
	def remove(cls, key: str):
		cls._check_page()
		return cls.__PAGE.client_storage.remove(f'{cls.__NAME}.{key}')

	@classmethod
	def keys(cls):
		cls._check_page()
		return cls.__PAGE.client_storage.get_keys(f'{cls.__NAME}.')

	@classmethod
	def values(cls):
		return [cls.__PAGE.client_storage.get(key) for key in cls.keys()]

	@classmethod
	def clear(cls):
		keys = cls.keys()
		for key in keys:
			cls.__PAGE.client_storage.remove(key)



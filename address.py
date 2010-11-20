from zillow import zEstimate

class Address():
	def __init__(self, address, citystatezip):
		self.address = address
		self.citystatezip = citystatezip
		self.assessedValue = self.assessedValue()


	def assessedValue(self):
		return zEstimate(self)

#!/usr/bin/python3

#
# M3TIOR 2018
#

# NOTE:
#	All universal misc. functions for use by the minetestdb server shall be
#	hosted here.
#

def dynamic_sort(post, objects, fields):
	"""
		post	: dictionary containing post data
		objects	: return value of model.objects.all() (what we're sorting)
		fields	: array of datatypes

		This function sorts our objects by the post flags contained in fields
	"""
	# IDEA:
	#	Perhaps, for our explicit sort options, we could add a radio
	#	button that would act as the single flag for our range of
	#	explicit sort options. It would be very easy to implement.
	#
	for flag in post:
		if flag == 'csrfmiddlewaretoken':
			pass # empty block so my brain doesn't hate me (skip for now)
		for field in fields:
			# XXX: Never thought I'd be saying this, or making something hacky.
			#	THIS IS A DANGEROUS HACK... PLEASE BE AWARE OF THIS FOR FUTURE
			#	USE OF THE "dynamic_sort" METHOD. AS THIS IS USED WITHIN IT.
			#
			#	JK, it's actually not that bad considering I was going to use
			#	the dreaded EVAL!!! before I found this...
			#
			#	Really though, at this point this function's just a sacrifice
			#	for code readability
			#
			#	Ok, ok... so after an hour of thinking I ended up adding an
			#	objattr attribute to all inherited models to deal with this issue
			if flag.find(str(field.objattr)) == 0:
				# The issue starts here, at object sorting.
				objects = objects.filter(**{
					# the objects.filter method takes said models attributes as
					# keyword arguments and parses them through python's
					# keyword syntax, which means the only way to assign them
					# is to use pythons keyword syntax.
					str(field.objattr):int(flag.lstrip(str(field.objattr)))
					# I managed to find a way to assign keyword names via
					# dictionary syntax, however, I still can't figure out
					# an efficient means of getting the assigned
					# "field" attribute with only a class name and the class
					# that uses it.
					#
					# So for now, this is as efficient as things get if we want
					# to keep code readable and simple.
					#
					# We could directly add each different sort option or model
					# manually, and it would be a faster. However, at least
					# while we're still thinking about what we want, a modular
					# approach to things that is extendable without extra
					# hastle is going to be way easier on everyone involved
				})
	return objects

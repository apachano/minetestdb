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
	for flag in post:
		if flag == 'csrfmiddlewaretoken':
			pass # empty block so my brain doesn't hate me (skip for now)
		elif ("Tags" in fields) and tag.find("Tags") == 0:
			objects = objects.filter(tags=int(flag.lstrip("Tags")))
		elif ("Minetest Versions" in fields) and tag.find("Minetest Versions") == 0:
			objects = objects.filter(mt_version=int(flag.lstrip("Minetest Versions")))

		# IDEA:
		#	Perhaps, for our explicit sort options, we could add a radio button
		#	that would act as the single flag for our range of explicit sort
		#


def calculate_brightness(img):
	# Write your code here
	if not img or not img[0]:
		return -1
	total = 0
	count = 0
	for row in img:
		if len(row) != len(img[0]):
			return -1
		for pixel in row:
			if pixel < 0 or pixel >255:
				return -1
			total += pixel
			count += 1
	avg = total / count
	return avg

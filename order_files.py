import os
import sys
import string
import os
import collections

result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(".") for f in filenames if os.path.splitext(f)[1] == '.md']

# TODO: Wont work with 2 nested levels of posts

def check_duplicated_link(all_files):
	all_links = []
	for infile in all_files:
		a_file = open(infile, 'r')
		lines = a_file.readlines()

		order_line = -1
		for idx, line in enumerate(lines):
			if "permalink:" in line:
				link = lines[idx].split("permalink:")[1].split()[0]
				#print("Post name", link)
				all_links.append(link)
				break

	duplicates = [item for item, count in collections.Counter(all_links).items() if count > 1]
	print("Found the following duplicates", duplicates)
	if duplicates != []:
		raise Exception("There are duplicates posts", duplicates)
	else:
		print("Duplicates check. ok")

def order_posts(all_files):
	counter = 1
	letter_counter0 = 0
	letter_counter1 = 0

	alphabet_string = string.ascii_lowercase
	alphabet = list(alphabet_string)
	for infile in sorted(all_files):
		if infile not in ["./index.md", "./template.md", "./README.md"]:
			a_file = open(infile, 'r')
			lines = a_file.readlines()

			order_line = -1
			for idx, line in enumerate(lines):
				if "order:" in line and "nav_order" not in line:
					order_line = idx
					break

			nav_order_line = -1
			for idx, line in enumerate(lines):
				if "nav_order" in line:
					nav_order_line = idx
					break

			if order_line == -1 or nav_order_line == -1:
				raise Exception("error")

			if "00_" in infile:
				lines[nav_order_line] = f"nav_order: {alphabet[letter_counter0]}\n"
				print(infile, alphabet[letter_counter0])
				letter_counter0 += 1
				letter_counter1 = 0
			else:
				lines[nav_order_line] = f"nav_order: {alphabet[letter_counter1]}\n"
				print(infile, alphabet[letter_counter1])
				letter_counter1 += 1

			lines[order_line] = f"order: {str(counter)}\n"
			print(infile, counter)

			a_file = open(infile, "w")
			a_file.writelines(lines)
			a_file.close()
			counter += 1

order_posts(result)
check_duplicated_link(result)
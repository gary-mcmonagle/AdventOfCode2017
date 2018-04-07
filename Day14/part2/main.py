from disk import disk
import json

my_disk = disk(json.load(open("input.json")))
my_disk.convert_binary_to_grid_squares()
my_disk.create_groups()

print(my_disk.get_group_count())
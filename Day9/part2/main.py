from stream_parser import stream_parser
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
stream = stream_parser(content[0])
print(stream.get_garbage_count())

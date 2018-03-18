from stream_parser import stream_parser
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
stream = stream_parser(content[0])
total = 0
bracket_value = 0
for idx, char in enumerate(stream.get_stream()):
    if(char == "{"):
        bracket_value += 1
    if(char == "}"):
        total += bracket_value
        bracket_value -= 1
print(total)

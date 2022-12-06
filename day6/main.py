
with open('input.txt') as file: 
    message = file.readline().strip()

#message = "bvwbjplbgvbhsrlpgdmjqwftvncz"
message_marker_length = 14
for i in range(len(message)-4): 
    message_chunk = message[i:i+4]
    print(message_chunk)
    if (len(set(message_chunk)) == len(message_chunk)):
        for j in range(len(message[i:])-message_marker_length):
            mchunk = message[i+j:i+j+message_marker_length]
            if len(set(mchunk))==len(mchunk):
                print(mchunk)
                break
        break
        
print(i+4, i+j+message_marker_length)
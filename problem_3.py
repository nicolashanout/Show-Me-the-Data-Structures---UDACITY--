import sys
import time

class Node(object):
    def __init__(self, count, ch = None):
        self.child_0 = None
        self.child_1 = None
        self.count = count 
        self.ch = ch

    def __str__(self):
        return "(char: {}, count: {})".format(self.ch, self.count)


# ENCODING
def huffman_encoding(data):

    # count frequencies
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char,0) +1
    
    if len(frequency)<2:
        if data == "":
            return "0", Node(1,"")
        else:
            return encode(data, generate_huffman_code(Node(1,data[0]))), Node(1,data[0])

    # make nodes with counts and associated chars
    nodes = {}
    for char in frequency:
        nodes[char] = Node(frequency[char], char)

    # generate Tree
    priority = 1
    node_0 = None
    node_1 = None
    parent_node = None
    while len(nodes)>1:
        change_priority = True
        min_priority = None
        for char in nodes:            
            if nodes[char].count == priority:
                if not node_0:
                    node_0 = nodes[char]
                elif not node_1: 
                    node_1 = nodes[char]
            elif not min_priority or nodes[char].count< min_priority:
                min_priority = nodes[char].count
            
            if node_0 and node_1:
                parent_node = Node(node_0.count + node_1.count,
                                   node_0.ch + node_1.ch)
                parent_node.child_0 = node_0
                parent_node.child_1 = node_1
                nodes[parent_node.ch] = parent_node
                nodes.pop(node_0.ch)
                nodes.pop(node_1.ch)
                node_0 = None
                node_1 = None
                change_priority = False
                break

        if change_priority:
            priority = min_priority
    tree = parent_node

    # generate encoding
    encoding = generate_huffman_code(tree)

    encoded_data = encode(data, encoding)

    return encoded_data, tree

def generate_huffman_code(node , code = ""):
    encoding = {}
    if node:
        if not (node.child_0 or node.child_1):
            if code == "": # case of only one letter
                encoding.update({node.ch: "0"})
            else:
                encoding.update({node.ch: code})
        encoding.update(generate_huffman_code(node.child_0, code + "0"))
        encoding.update(generate_huffman_code(node.child_1, code + "1"))
    return encoding

def encode(data , encoding):
    encoded_data = data
    for char in encoding:
        encoded_data = encoded_data.replace(char, encoding[char])
    return encoded_data
    

# DECODING
def huffman_decoding(data, tree):
    
    encoding = generate_huffman_reverse_code(tree)
    decoded_message = ""
    code = ""
    for c in data:
        code += c
        if code in encoding:
            decoded_message += encoding[code]
            code = ""
    
    return decoded_message

def generate_huffman_reverse_code(node , code = ""):
    encoding = {}
    if node:
        if not (node.child_0 or node.child_1):
            if code == "": # case of only one letter
                encoding.update({"0": node.ch})
            else:
                encoding.update({code: node.ch})
        encoding.update(generate_huffman_reverse_code(node.child_0, code + "0"))
        encoding.update(generate_huffman_reverse_code(node.child_1, code + "1"))
    return encoding



# TEST
if __name__ == "__main__":
    codes = {}

    print('TEST 1:')
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))


    
    print('\n\n------------------------------------------------')
    print('TEST 2:')
    a_great_sentence = "short"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))

    
    print('\n\n------------------------------------------------')
    print('TEST 3:')
    a_great_sentence = "This is a very long sentence that will benefit more from the encoding because it probably has many repeating letters that appear again and again and again and again and and again and and again and and again and and again and and again and and again and and again and and again and and again and and again again and again and again and again and and again and and again and and again and and again and and again and and again and and again and and again and and again and and again again and again and again and again and and again and and again and and again and and again and and again and and again and and again and and again and and again and and again"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))




    print('\n\n------------------------------------------------')
    print('TEST 4:')
    a_great_sentence = "a"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))


    
    print('\n\n------------------------------------------------')
    print('TEST 5:')
    a_great_sentence = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))


    
    print('\n\n------------------------------------------------')
    print('TEST 6:')
    a_great_sentence = "aaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaa"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))

     
    print('\n\n------------------------------------------------')
    print('TEST 7:')
    a_great_sentence = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the dencoded data is: {}\n".format(decoded_data))
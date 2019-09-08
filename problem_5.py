import hashlib
import datetime

class Block(object):

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.data).encode('utf-8')+
                    str(self.previous_hash).encode('utf-8')+
                    str(self.timestamp).encode('utf-8'))
        sha.update(hash_str)
        return sha.hexdigest()

    def __str__(self):
        return '\nBlockHash: {}\n Timestamp: {}\n Data: {}\n Previous Hash: {}\n'.format(self.hash, self.timestamp, self.data, self.previous_hash)

class Node(object):
    def __init__(self, data, previous_hash):
        self.block = Block(datetime.datetime.utcnow(), data, previous_hash)
        self.next = None
        self.tail = None

class BlockChain(object):
    def __init__(self):
        self.head = None

    def append(self, data = None):
        if data == None:
            print("can't store empty block")
            return

        if not self.head:
            self.head = Node(data, None)
            self.tail = self.head

        else:
            self.tail.next = Node(data, self.tail.block.hash)
            self.tail = self.tail.next

    def __str__(self):
        if self.head == None:
            return "Block Chain is empty"
        current_node = self.head
        output = ""
        while current_node:
            output += str(current_node.block)
            current_node = current_node.next
        return output


print('\n------------------------------\n')
block_chain = BlockChain()
block_chain.append("Some Information")
block_chain.append("new Information")
block_chain.append("3rd Block")


current_block = block_chain.head
print(block_chain)
#expected output: prints the 3 blocks

print(current_block.block)
#outputs the first blocks data

current_block = current_block.next
print(current_block.block)
#outputs the second blocks data

current_block = current_block.next
print(current_block.block)
#outputs the last blocks data


print('\n------------------------------\n')
block_chain = BlockChain()

print(block_chain)
#expected output: Block Chain is empty



print('\n------------------------------\n')
block_chain = BlockChain()

block_chain.append()
block_chain.append("only this block should be there")
block_chain.append()

print(block_chain)
#expected output: prints 1 block only
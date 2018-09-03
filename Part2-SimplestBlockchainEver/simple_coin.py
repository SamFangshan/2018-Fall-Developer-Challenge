from blockchain import Blockchain

#Initiates blockchain

def generate_blocks(number_of_blocks):
    """
    input: number_of_blocks: int
    output: hash of final block: str

    Given a number of blocks return the output after x amount of block as a string. Input blocks are EMPTY
    """
    

    ### YOUR CODE HERE
    blkchn = Blockchain()
    blkchn.genesis()
    for x in range(number_of_blocks - 1):
        blk = blkchn.get_current_block()
        blkchn.mine(blk)
        
    return blkchn.get_current_block().hash_self()

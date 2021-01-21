from hashlib import sha256
import time

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(blockNumber, transactions, previousHash, difficulty):
    prefix = '0'*difficulty
    NONCE = 1
    while True:
        text = str(blockNumber) + transactions + previousHash + str(NONCE)
        NEW_HASH = SHA256(text)
        if NEW_HASH.startswith(prefix):
            print(f"Successfully mined bitcoins with nonce value: {NONCE}")
            return NEW_HASH
        NONCE += 1

if __name__=='__main__':
    # Example transactions.
    transactions='''
    bc1q9w4xxqjrr2awkedhcd7p4dj9cdwyru5fq986dt->bc1q9w4xxqjrr2awkedhcd7p4dj9cdwyru5fq986dt->0.68659010,
    bc1q9w4xxqjrr2awkedhcd7p4dj9cdwyru5fq986dt->33kAvZX39EGj9uHJZecqFAKmHKdfeQFk9R->0.05248186
    '''
    # Set Difficulty
    difficulty=20
    startTime = time.time()
    print("Start mining...")
    NEW_HASH = mine(666893, transactions, '0000000000000000000af3f0149d86aea807789e455b62b52eda02567a3a0ae9', difficulty)
    totalTime = str((time.time() - startTime))
    print(f"End mining. Mining took: {totalTime} seconds.")
    print(NEW_HASH)
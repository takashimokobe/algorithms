# A Hashtable is an object
# that contains a built in python list
# in every index of that list, there is another built in python list
# that list could be either empty or contain another built in python list
class HashTable:
    def __init__(self, val=8):
        self.val = val
        self.size = 0
        self.collisions = 0
        self.list = [[] for idx in range(val)]

    def __eq__(self, other):
        return ((type(other) == HashTable
                 and self.val == other.val and self.list == other.list and self.collisions == other.collisions))

    def __repr__(self):
        return ("HashTable({!r})".format(self.list))


# no parameters -> HashTable
# function returns an empty HashTable
def empty_hash_table():
    return HashTable()


# HashTable, int, str/int
# function inserts a list into the hashtable depending on its key
def insert(hashtable, key, item):
    hassh = hash(key) % (hashtable.val)

    for idx in range(len(hashtable.list[hassh])):
        if hashtable.list[hassh][idx][0] == key:
            hashtable.list[hassh][idx] = [key, item]
            hashtable.collisions += 1
            return hashtable

    if hashtable.list[hassh] != []:
        hashtable.collisions += 1

    hashtable.list[hassh].append([key, item])
    hashtable.size += 1

    if (hashtable.size / hashtable.val) > 1.5:

        hashtable.collisions = 0
        hashtable.val *= 2
        newlst = [[] for idx in range(hashtable.val)]

        for lst in range(len(hashtable.list)):
            for sublst in hashtable.list[lst]:

                hassh = hash(sublst[0]) % (hashtable.val)

                if newlst[hassh] != []:
                    hashtable.collisions += 1

                newlst[hassh].append(sublst)

        hashtable.list = newlst
        return hashtable

    return hashtable


# HashTable, int -> string
# function returns the item associated with the key
def get(hashtable, key):
    hassh = hash(key) % (hashtable.val)

    for idx in range(len(hashtable.list[hassh])):
        if hashtable.list[hassh][idx][0] == key:
            return hashtable.list[hassh][idx][1]

    raise LookupError()


# HashTable, int -> HashTable
# function removes a list in the HashTable
# and returns the new HashTable
def remove(hashtable, key):
    hassh = hash(key) % (hashtable.val)

    for idx in range(len(hashtable.list[hassh])):
        if hashtable.list[hassh][idx][0] == key:
            hashtable.list[hassh].pop(idx)
            hashtable.size -= 1
            return hashtable
    raise LookupError()


# HashTable -> int
# function returns the number of items in a HashTable
def size(hashtable):
    return hashtable.size


# HashTable -> int
# function returns the load factor of the table
def load_factor(hashtable):
    return hashtable.size / hashtable.val


# HashTable -> int
# function returns the number of collisions in a table
def collisions(hashtable):
    return hashtable.collisions
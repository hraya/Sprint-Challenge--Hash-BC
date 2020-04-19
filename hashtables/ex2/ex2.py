#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(length):
        tix_source = tickets[i].source
        tix_dest = tickets[i].destination
        hash_table_insert(hashtable, tix_source, tix_dest)
    #  first flight
    route[0] = (hash_table_retrieve(hashtable, "NONE"))

    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
        
    
    return route

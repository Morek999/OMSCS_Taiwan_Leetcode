/*
All right, I have to admit, I don't know wtf this question is talking about in the very beginning, so I directly look for the answer...
So there are three moves that you want to do with LRU cache:

1. Get the key / Check if the key exists

2. Put the key

3. Delete the first added key (least recently used item)

Since we want O(1) time complexity, hash table must be used for quick look up. And the trick that I can't come up with is to use double linked list
to store the key and value. That way we can quickly move the recent used element to the beginning of the list in O(1)

The hash table will store the key and the pointer to the component in the double linked list
The linked list will just store the key and the value

In get, we will first check if the value is already in hash table. If it is not in the hash table, just return -1
if it is in the hash table, then we need to move this key and value to the beginning of the double linked list and return its value

In put, we first search if this key is in the hash table. If it is, then we need to move this key and value to the beginning of the double linked list
and update the value.
If not, then we need to first check if the list reached its capacity. If it reached, just pop out the end of the linked list.
After checking the capacity, we can guarantee there's enough space to insert the value
We just simply insert the value to the beginning of the double linked list.
I think I will need to revisit this problem again and again since this one is actually not that straight forward. 
Time complexity: O(1) for the required operation
Space complexity: O(1) since we need a hash map and double linked list to store no more than the capacity
Reference: https://www.youtube.com/watch?v=q1Njd3NWvlY&
*/

class LRUCache {
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        const auto it = m.find(key);
        if(it == m.end()){
            return -1; // not found
        }
        // move this set to the beginning of the double linked list
        // note it-> second is the pointer to the location of key in linked list
        cache.splice(cache.begin(),cache,it->second); 
        return it->second->second; // return the value corresponding to the key location
    }
    
    void put(int key, int value) {
        const auto it = m.find(key);
        if(it != m.end()){ // the key is already existent  
            // update the value
            it->second->second = value;
            // move it to the front of the list
            cache.splice(cache.begin(),cache,it->second);
            return;
        }
        // if the key is not existent, then we need to check the capacity first
        if(cache.size() == cap){ 
            // reach the capacity and then pop out the last set in the double linked list
            // note we also need to modify the hash table
            const auto node = cache.back();
            m.erase(node.first); // erase the key in the hash table
            cache.pop_back();
        }
        // Now we guarantee there's space to insert new element in the double linked list
        cache.emplace_front(key,value); // insert the set to the front of the double linked list
        m[key] = cache.begin(); // store the key to the hash table
    }
private:
    int cap; 
    list<pair<int,int>> cache;
    unordered_map<int, list<pair<int,int>>::iterator> m;
};
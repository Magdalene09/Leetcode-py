import heapq as H

class HeapItem :

    def __init__(self, word, freq) :
        self.word = word
        self.freq = freq

    def __lt__(self, compareWord) :

        if self.freq == compareWord.freq :
            return self.word > compareWord.word

        return self.freq < compareWord.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        hmap = Counter(words)

        pq = []
        result = []

        for key, val in hmap.items() :
            item = HeapItem(key, val)

            if k > len(pq) :
                H.heappush(pq, item)

            else :
                if item > pq[0] :
                    H.heappop(pq)
                    H.heappush(pq, item)

        while pq :

            item = H.heappop(pq)
            result.append(item.word)

        result.reverse()
        return result

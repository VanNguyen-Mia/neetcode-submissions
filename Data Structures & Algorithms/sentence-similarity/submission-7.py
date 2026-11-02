class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        wordToSimilarWords = defaultdict(set)

        for word1, word2 in similarPairs:
            wordToSimilarWords[word1].add(word2)
            wordToSimilarWords[word2].add(word1)

        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in wordToSimilarWords[sentence1[i]]:
                continue
            return False

        return True
        # if len(sentence1) != len(sentence2):
        #     return False

        # sim_dict = {}
        # for pair in similarPairs:
        #     if pair[0] not in sim_dict:
        #         sim_dict[pair[0]] = (pair[1],)
        #     else:
        #         sim_dict[pair[0]] += (pair[1],) 

        # for i in range(len(sentence1)):
        #     if sentence1[i] == sentence2[i]:
        #         res = True
        #     elif sentence1[i] in sim_dict.keys() and sentence2[i] in sim_dict[sentence1[i]]:
        #         res = True
        #     elif sentence2[i] in sim_dict.keys() and sentence1[i] in sim_dict[sentence2[i]]:
        #         res = True
        #     else:
        #         res = False
        #         break

        # return res
            


        



        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary_ = {}
        # for i in strs:
        #     string = ''.join(sorted(i))
        #     if string not in dictionary_.keys():
        #         dictionary_[string] = [i]
        #     else:
        #         dictionary_[string].append(i)
        # return dictionary_.values()
        d = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s not in d.keys():
                d[s] = [i]
            else:
                d[s].append(i)
        return list(d.values())
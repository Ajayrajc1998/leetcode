class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        model=""
        for i in key:
            if i!=" " and i not in model:
                model+=i
        print(model)
        d={model[i]:chr(i+97) for i in range(len(model))}
        print(d)
        result=""
        for i in message:
            if i!=" ":
                result+=d[i]
            else:
                result+=" "
        return result
        
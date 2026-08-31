def decodeIp(s, result, string, idx, length, part):

    if part == 4:
        if idx == length:
            result.append(string)
        return

    for i in range(idx, min(idx + 3, length)):

        cur = s[idx:i + 1]

        if len(cur) > 1 and cur[0] == '0':
            return

        if int(cur) < 256:

            if part == 0:
                decodeIp(s, result, string + cur,
                         i + 1, length, part + 1)
            else:
                decodeIp(s, result, string + '.' + cur,
                         i + 1, length, part + 1)

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)
        result = []

        decodeIp(s, result, "", 0, n, 0)
        return result

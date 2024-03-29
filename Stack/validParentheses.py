class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        for c in s:
            #print(c)
            if c in {'(', '{', '['}:
                #print(f'{c} is in an opening bracket')
                q.append(c)
            elif c in {')', '}', ']'}:
                if len(q) == 0:
                    #print(q)
                    return False
                _ = q.pop()
                #print(_)
                match c:
                    case ')':
                        if not _ == '(':
                            return False
                    case ']':
                        if not _ == '[':
                            return False
                    case '}':
                        if not _ == '{':
                            return False
            #print(q, '\n')
        if len(q) == 0:
            return True
        else:
            return False
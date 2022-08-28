from math import log, inf

def count_sigfigs(num):
    sigfigs = 0
    for n in num.strip('0'):
        sigfigs += 1 if n != '.' else 0

    if '.' in num:
        sigfigs += len(num) - len(num.rstrip('0'))
    return sigfigs

class Val:
    def __init__(self, num, sigfigs=None):
        self.val = float(num)
        if isinstance(num, float):
            self.sig_figs = sigfigs
            return
        if num.startswith('-'):
            num = num[1:]
        if 'E' in num:
            num = num.split('E')[0]
        elif 'e' in num:
            num = num.split('e')[0]

        self.sig_figs = count_sigfigs(num)

    def __repr__(self):
        s = str(abs(self.val))
        s = s.replace(".", "").lstrip('0')

        if len(s) > self.sig_figs:
            s = s[:self.sig_figs+1]

        if len(s) > 1:
            s = s[0] + '.' + s[1:]
        else:
            s = s[0] + '.'

        n = float(s)
        if count_sigfigs(s) > self.sig_figs:
            n = float(s)
            n = round(n, self.sig_figs-1)
            s = str(n)

        sigfigs = count_sigfigs(s) 
        if sigfigs < self.sig_figs:
            s += '0' * (self.sig_figs - sigfigs) 
        while count_sigfigs(s) > self.sig_figs:
            s = s[:-1]

        s += 'E' + str(int(round(log(abs(self.val) / n, 10), 0)))
        s = '-' + s if self.val < 0 else '' + s

        return s

    def __str__(self):
        return f"<Val val={self.val} sigfigs={self.sig_figs}>"

    def __add__(self, other):
        if isinstance(other, type(self)):
            return Val(self.val + other.val, min(self.sig_figs, other.sig_figs))
        else:
            return Val(self.val + other, inf)
    def __sub__(self, other):
        if isinstance(other, type(self)):
            return Val(self.val - other.val, min(self.sig_figs, other.sig_figs))
        else:
            return Val(self.val - other, inf)
    def __mul__(self, other):
        if isinstance(other, type(self)):
            return Val(self.val * other.val, min(self.sig_figs, other.sig_figs))
        else:
            return Val(self.val * other, inf)
    def __truediv__(self, other):
        if isinstance(other, type(self)):
            return Val(self.val / other.val, min(self.sig_figs, other.sig_figs))
        else:
            return Val(self.val / other, inf)
    def __floordiv__(self, other):
        if isinstance(other, type(self)):
            return Val(self.val // other.val, min(self.sig_figs, other.sig_figs))
        else:
            return Val(self.val // other, inf)
    def __pow__(self, other):
        if isinstance(other, type(self)):
            return Val(self.val ** other.val, min(self.sig_figs, other.sig_figs))
        else:
            return Val(self.val ** other, inf)

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.val < other.val
        else:
            return self.val < other
    def __le__(self, other):
        if isinstance(other, type(self)):
            return self.val <= other.val
        else:
            return self.val <= other
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.val == other.val
        else:
            return self.val == other
    def __ne__(self, other):
        if isinstance(other, type(self)):
            return self.val != other.val
        else:
            return self.val != other
    def __ge__(self, other):
        if isinstance(other, type(self)):
            return self.val >= other.val
        else:
            return self.val >= other
    def __gt__(self, other):
        if isinstance(other, type(self)):
            return self.val > other.val
        else:
            return self.val > other
    def __index__(self):
        return int(self.val)
    def __float__(self):
        return self.val
    def __int__(self):
        return int(self.val)


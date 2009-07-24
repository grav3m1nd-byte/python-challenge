def trans_char(char) :
        import string
        shift = 2
        l = string.ascii_lowercase
        index = l.find(char)
        if -1 == index :
                return char
        new_index = index + shift
        if new_index > len(l)-1 :
                new_index -= len(l)
        new_char = l[new_index]
        return new_char
def trans_string(string) :
        result = ''
        for char in string :
                result += trans_char(char)
        return result

#print trans_string('wxyz')
#print trans_string('g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. ')
print trans_string('map')

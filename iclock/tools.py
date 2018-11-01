def getSQL_insert(table, **kwargs):
    """ \xe7\x94\x9f\xe6\x88\x90 insert SQL \xe8\xaf\xad\xe5\x8f\xa5
    """
    ks = ''
    vs = ''
    for k, v in kwargs.items():
        ks += k + ','
        if isNumber(v) or v == 'null':
            vs += str(v) + ','
        else:
            vs += "'" + v + "',"

    return 'INSERT INTO %s (%s) VALUES (%s)' % (table, ks[:-1], vs[:-1])


def getSQL_update(table, **kwargs):
    """ \xe7\x94\x9f\xe6\x88\x90 update SQL \xe8\xaf\xad\xe5\x8f\xa5
    """
    kvs = ''
    kvs_where = ''
    for k, v in kwargs.items():
        if k.startswith('where'):
            kvs_where += k[5:] + '='
            if isNumber(v) or v == 'null':
                kvs_where += str(v) + ' and '
            else:
                kvs_where += "'" + v + "' and "
        else:
            if not v:
                continue
            if isNumber(v) or v == 'null':
                kvs += k + '=' + str(v) + ','
            else:
                kvs += k + "='" + v + "',"

    if kvs_where == '':
        return 'UPDATE %s SET %s' % (table, kvs[:-1])
    return 'UPDATE %s SET %s WHERE %s' % (table, kvs[:-1], kvs_where[:-4])


def getSQL_update_ex(table, dict):
    """ \xe7\x94\x9f\xe6\x88\x90 update SQL \xe8\xaf\xad\xe5\x8f\xa5
    """
    kvs = ''
    kvs_where = ''
    for k, v in dict.items():
        if k.startswith('where'):
            kvs_where += k[5:] + '='
            if isNumber(v) or v == 'null':
                kvs_where += str(v) + ' and '
            else:
                kvs_where += "'" + v + "' and "
        else:
            if not v:
                continue
            if isNumber(v) or v == 'null':
                kvs += k + '=' + str(v) + ','
            else:
                kvs += k + "='" + v + "',"

    if kvs_where == '':
        return 'UPDATE %s SET %s' % (table, kvs[:-1])
    return 'UPDATE %s SET %s WHERE %s' % (table, kvs[:-1], kvs_where[:-4])


def isNumber(num):
    """ \xe5\x88\xa4\xe6\x96\xad\xe6\x98\xaf\xe5\x90\xa6\xe6\x95\xb0\xe5\xad\x97 (int float long)
    """
    try:
        abs(num)
        return True
    except:
        return False


def getStr_c(s):
    """ \xe8\x8e\xb7\xe5\x8f\x96 C\xe8\xaf\xad\xe8\xa8\x80\xe7\xb3\xbb\xe7\xbb\x9f \xe4\xbc\xa0\xe8\xbe\x93\xe8\xbf\x87\xe6\x9d\xa5\xe7\x9a\x84\xe6\x95\xb0\xe6\x8d\xae\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2
    """
    try:
        return s[:s.index('\x00')]
    except:
        return s


def getFptemp_c(s):
    """ \xe8\x8e\xb7\xe5\x8f\x96 C\xe8\xaf\xad\xe8\xa8\x80\xe7\xb3\xbb\xe7\xbb\x9f \xe4\xbc\xa0\xe8\xbe\x93\xe8\xbf\x87\xe6\x9d\xa5\xe7\x9a\x84\xe6\x8c\x87\xe7\xba\xb9\xe6\xa8\xa1\xe7\x89\x88\xef\xbc\x88\xe5\x90\x8e\xe9\x9d\xa2\xe5\xa1\xab\xe5\x85\x85\xe7\x9a\x84"\x00"\xef\xbc\x89
    """
    i = len(s) - 1
    while i > 0 and s[i] == '\x00':
        i -= 1

    return s[:i]


def getStr_c_decode(s):
    """ \xe8\x8e\xb7\xe5\x8f\x96 C\xe8\xaf\xad\xe8\xa8\x80\xe7\xb3\xbb\xe7\xbb\x9f \xe4\xbc\xa0\xe8\xbe\x93\xe8\xbf\x87\xe6\x9d\xa5\xe7\x9a\x84\xe6\x95\xb0\xe6\x8d\xae\xe7\x9a\x84\xe5\xad\x97\xe7\xac\xa6\xe4\xb8\xb2\xef\xbc\x8c\xe5\xb9\xb6\xe6\x8c\x89 gb18030 \xe8\xa7\xa3\xe7\xa0\x81
    """
    try:
        return unicode(s[:s.index('\x00')].decode('gb18030'))
    except:
        return unicode(s.decode('gb18030'))


def getSQL_insert_ex(table, dict):
    """ \xe7\x94\x9f\xe6\x88\x90 insert SQL \xe8\xaf\xad\xe5\x8f\xa5
    """
    ks = ''
    vs = ''
    for k, v in dict.items():
        ks += k + ','
        if v == None:
            v = 'null'
        if isNumber(v) or v == 'null':
            vs += str(v) + ','
        elif str(type(v)) == "<type 'datetime.datetime'>":
            vs += "'" + v.strftime('%Y-%m-%d %H:%M:%S') + "',"
        elif str(type(v)) == "<type 'datetime.time'>":
            vs += "'" + v.strftime('%H:%M:%S') + "',"
        else:
            vs += "'" + v + "',"

    return 'INSERT INTO %s (%s) VALUES (%s)' % (table, ks[:-1], vs[:-1])

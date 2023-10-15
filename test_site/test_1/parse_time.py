from dateutil.parser import parse


class ParseTime():

    def parse(now, last):

        last = parse(last)
        result = str(now - last)
        if result.find('day') != -1:
            return 1
        else:
            result = result.split(':')
            if result[0] != '0':
                return 1
            else:
                if int(result[1]) >= 30:
                    return 1
                else:
                    return 0

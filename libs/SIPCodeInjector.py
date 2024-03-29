#replacement of SIP codes text


#some codes for SIP
import copy

__codes = {
    100 : "Trying",
    180 : "Ringing",
    182 : "Queued",

    200 : "OK",
    202 : "Accepted",
    204 : "No Notification",

    480 : "Temporarily Unavailable",
    486 : "Busy Here",

    603: "Decline"
}


__reCodes = copy.deepcopy(__codes)

def replaceCode(code : int, text : str):
    if text in __codes.values() or not code in __codes.keys(): return
    __reCodes[code] = text


def reformatRequest(text : list) -> list:
    header = text[:]
    codeLine = header[0].split(" ")[:2]
    code = int(codeLine[1])
    if code not in  __codes:
        return text
    codeLine.append(__reCodes[code])
    header[0] = " ".join(codeLine)
    return header

def getCode(code: int) -> str:
    if not code in __reCodes: return None
    return __reCodes[code]

    
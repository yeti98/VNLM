import re


END_OF_SENTENCES_CHARS = '.?!'

CHAR1 ='AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXYaăâbcdđeêghiklmnoôơpqrstuưvxy'
CHAR2 = 'áạàảãăắặằẳẵâấậầẩẫđéẹèẻẽêếệềểễíịìỉĩóọòỏõôốộồổỗơớợờởỡúụùủũưứựừửữýỵỳỷỹÁẠÀẢÃĂẮẶẰẲẴÂẤẬẦẨẪĐÉẸÈẺẼÊẾỆỀỂỄÍỊÌỈĨÓỌÒỎÕÔỐỘỒỔỖƠỚỢỜỞỠÚỤÙỦŨƯỨỰỪỬỮÝỴỲỶỸ'
PATTERN = r'\.[{}][{}]'.format(CHAR2+CHAR1, CHAR2+CHAR1)


def reduce_spaces(text):
    return re.sub(r'\s+', ' ', text)


def endline_after_sentence(text):
    for ch in END_OF_SENTENCES_CHARS:
        text = text.replace(ch+' ', ch+'\n')
    return text

def doc2sentences(text):
    text = reduce_spaces(text)
    while re.search(PATTERN, text):
        x = re.search(PATTERN, text)
        # print(x)
        text = text[:x.start() + 1] + ' ' + text[x.start() + 1:]
    text = endline_after_sentence(text)
    return [x.strip() for x in text.split('\n')]
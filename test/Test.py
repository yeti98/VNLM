import re

from src.run.utils import doc2sentences

CHAR1 ='AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXYaăâbcdđeêghiklmnoôơpqrstuưvxy'
CHAR2 = 'áạàảãăắặằẳẵâấậầẩẫđéẹèẻẽêếệềểễíịìỉĩóọòỏõôốộồổỗơớợờởỡúụùủũưứựừửữýỵỳỷỹÁẠÀẢÃĂẮẶẰẲẴÂẤẬẦẨẪĐÉẸÈẺẼÊẾỆỀỂỄÍỊÌỈĨÓỌÒỎÕÔỐỘỒỔỖƠỚỢỜỞỠÚỤÙỦŨƯỨỰỪỬỮÝỴỲỶỸ'
PATTERN = r'\.[{}][{}]'.format(CHAR2+CHAR1, CHAR2+CHAR1)
a = '''Họ thấy Giả mẫu mệt nhọc nên đều ra về.Riêng Tiết
phu Nhân từ biệt Giả mẫu rồi đến bên nhà Bảo Thoa nói: abc, v.v...Riêng Tiết
phu Nhân từ biệtw Giả mẫu rồi đến bên nhà Bảo Thoa nói:'''

a='''Nếu lão Hagrid mà không chỉ thì Harry
cũng không nhận ra được là nó nằm ở đó.Người ta vôi vã đi ngang qua mà không hề
liếc tới nó một cái.Ánh mắt của họ trượt từ tiệm sách lớn bên này sang tiệm băng đĩa
nhạc bên kia như thể họ không hề thấy tiệm rượu Leaky Cauldron.'''


a='''Trong lịch sử văn học Trung Quốc. Hồng Lâu Mộng có một vị trí đặc biệt. Người Trung Hoa say
mê đọc nó, bình luận về nó(1), sáng tác về nó đến nỗi nói: “Khai đàm bất thuyết Hồng Lâu
Mộng, Độc tận thi thư diệc uổng nhiên!”'''
# print(re.search(
#     r'\.[AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXYaăâbcdđeêghiklmnoôơpqrstuưvxy][AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXYaăâbcdđeêghiklmnoôơpqrstuưvxy]',
#     a))
# print(PATTERN)

# while re.search(PATTERN,a):
#     x = re.search(PATTERN,a)
#     # print(x)
#     a = a[:x.start()+1]+' '+a[x.start()+1:]

# print(a)
print(doc2sentences(a))
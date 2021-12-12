def delSpace():
    s =input('moi ban nhap chuoi vao:')
    z =s.split()
    print(z)
    c = "".join(z) #xoa khoang trang
    print(c)
    c = "_".join(z) #thay the dau gạch dưới
    print(c)
delSpace()


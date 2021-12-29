from abc import ABC, abstractmethod
#tính trừu tượng
class Person(ABC):
     # tính đóng gói các phương thức dưới là protected
     _hoten = ''
     _gioitinh = ''
     _tuoi = 0
     def __init__(self, *para): #khởi tạo
         if len(para) == 0:
             pass           #thoát
         else:
            self._hoten = para[0] #lưu
            self._gioitinh = para[1]
            self._tuoi = para[2]

     @abstractmethod
     def getInfo(self):
         print("Ho ten: {0}".format(self._hoten))
         print("Gioi tinh: {0}".format(self._gioitinh))
         print("Tuoi: {0}".format(self._tuoi))

     def Nhap(self):
         print("Nhap ho ten: ", end ='');
         self._hoten = input()
         print("Nhap gioi tinh: ", end ='');
         self._gioitinh = input();
         print("Tuoi: ", end ='');
         self._tuoi = int(input());


class Vemaybay:
     # tính đóng gói các phương thức dưới là private
     __tenchuyen = ''
     __ngaybay = ''
     __giave = 0
     # phuong thuc khoi tao
     def __init__(self, *para):
         if len(para) == 0:
             pass
         else:
            self.__tenchuyen = para[0]
            self.__ngaybay = para[1]
            self.__giave = para[2]
     # xuat
     def getInfo(self):
         print("Ten chuyen bay: {0}".format(self.__tenchuyen))
         print("Ngay bay: {0}".format(self.__ngaybay))
         print("Gia ve: {0}".format(self.__giave))
         print();

     # getgiave
     def getgiave(self):
         return self.__giave

     def Nhap(self):
         print("Nhap ten chuyen bay: ", end ='');
         self.__tenchuyen = input();
         print("Nhap ngay bay (yyyy,mm,dd): ", end ='');
         self.__ngaybay = input();
         print("Gia ve: ", end ='');
         self.__giave = int(input());

# tính kế thừa hành khách kế thừa từ lớp person
class Hanhkhach(Person):
    #private tính đóng gói
     __soluong = 0
     def __init__(self, *para):
         if len(para) == 0:
             self.__ve = [];
             pass
         else:
            super().__init__(para[0], para[1], para[2]) #khởi tạo
            self.__ve = [];
            self.__soluong = para[3]
            for i in range(self.__soluong):
                self.__ve.append(Vemaybay('','',0)) 
    #tính đa hình overiding lại hàm Nhap từ class person
     def Nhap(self):
         super().Nhap();
         self.__ve.clear();
         print("Nhap so luong ve: ", end = '');
         self.__soluong = int(input());
         for i in range (self.__soluong):
             tmp = Vemaybay();
             tmp.Nhap();
             self.__ve.append(tmp)
    #tính đa hình overiding lại hàm getInfo từ class person
     def getInfo(self):
         super().getInfo()
         for i in range(self.__soluong): #in thong tin
             print("Thong tin ve thu " + str(i + 1))
             self.__ve[i].getInfo()

     def tongtien(self):
         tong = 0
         for v in self.__ve:
             tong += v.getgiave()
         if self.__soluong > 3:
             print('Discount 10% khi mua tren 3 ve!')
             return (tong - tong * 0.1)
         return tong;

choose = 1;
a = []
n = 0;

def compare(e):
    return e.tongtien()




while(choose != 0):
    print("----------------------Menu------------------------");
    print("  1. Khoi tao danh sach khach hang!" );
    print("  2. Xuat thong tin khach hang!" );
    print("  3. Xuat tong tien phai tra cho tung khach hang!" );
    print("  4. Sap xep theo thu tu tong tien tang dan!" );
    print("  5. Sap xep theo thu tu tong tien giam dan!" );
    print("  6. Sua thong tin khach hang!" );
    print("  7. Xoa thong tin khach hang!" );
    print("  0. Thoat" );
    print("--------------------------------------------------");
    choose = int(input('Moi ban chon chuc nang: '));
    if choose == 1:
        print('Nhap so luong khach hang: ', end = '')
        n = int(input());
        for i in range(n):
            tmp = Hanhkhach();
            tmp.Nhap();
            a.append(tmp);
    elif choose == 2:
        for i in a:
            i.getInfo();
    elif choose == 3:
        for i in range(n):
            print('Tong tien cua khach hang thu {0} phai tra la: {1} '.format(str(i+1),int(a[i].tongtien())))
    elif choose == 4:
        a.sort(reverse = False,key=compare)
        print('Sap xep thanh cong! Hay quay lai chuc nang 2 de kiem tra')
    elif choose == 5:
        a.sort(reverse = True,key=compare)
        print('Sap xep thanh cong! Hay quay lai chuc nang 2 de kiem tra')
    elif choose == 6:
        num = -1
        print("Nhap so thu tu của khach hang can chinh sua: ", end = '');
        num = int(input())
        if num > len(a) or num == 0:
            print('So thu tu khong hop le')
        else:
            a[num - 1].Nhap();
    elif choose == 7:
        num = -1
        print("Nhap so thu tu của khach hang can xoa: ", end = '');
        num = int(input())
        if num > len(a) or num == 0:
            print('So thu tu khong hop le')
        else:
            a.pop(num - 1);
            print('Xoa thanh cong! Hay quay lai chuc nang 2 de kiem tra')
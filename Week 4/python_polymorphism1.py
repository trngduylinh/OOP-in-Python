class Hoa:
    def gioi_thieu (self):
        print("Đây là bông hoa")
    def mau_sac (self):
        print("Đa dạng màu sắc")
class Hoa_Hong(Hoa):
    def mau_sac (self):
        print("Màu đỏ")
class Hoa_Lan(Hoa):
    def mau_sac (self):
        print("Màu trắng")
flo = Hoa ()
rose = Hoa_Hong()
orc = Hoa_Lan()

flo.gioi_thieu()
flo.mau_sac()

rose.gioi_thieu()
rose.mau_sac()

orc.gioi_thieu()
orc.mau_sac()

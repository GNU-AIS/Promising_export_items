class ExportItem:
    """ 품목별 국가별 수출입실적 API를 통해 각각의 데이터를 받을 때 클래스 단위로 저장하기 위한 수출 아이템 클래스 """
    def __init__(self, year:str, statCdCntnKor1:str, statCd:str, statKor:str, hsCd:str, expWgt:int, expDlr:int, impWgt:int, impDlr:int, balPayments:int):
        """
        :param year: (str) 기간 ex.. 2016.1
        :param statCdCntnKor1: (str) 국가명 ex.. 미국
        :param statCd: (str) 국가코드 ex.. US
        :param statKor: (str) 품목명 ex.. 쇠고기(냉동한 것으로 한정한다)
        :param hsCd: (str) hs 코드 ex.. 0202
        :param expWgt: (int) 수출중량 ex.. 18003
        :param expDlr: (int) 수출금액 ex.. 150822
        :param impWgt: (int) 수입중량 ex.. 14809834
        :param impDlr: (int) 수입금액 ex.. 93754113
        :param balPayments: (int) 무역수지 ex.. -93603291
        """
        self.year = year
        self.statCdCntnKor1 = statCdCntnKor1
        self.statCd = statCd
        self.statKor = statKor
        self.hsCd = hsCd
        self.expWgt = expWgt
        self.expDlr = expDlr
        self.impWgt = impWgt
        self.impDlr = impDlr
        self.balPayments = balPayments

    def __repr__(self):
        return (f"ExportItem(year={self.year}, statCdCntnKor1={self.statCdCntnKor1}, statCd={self.statCd}, "
                f"statKor={self.statKor}, hsCd={self.hsCd}, expWgt={self.expWgt}, expDlr={self.expDlr}, "
                f"impWgt={self.impWgt}, impDlr={self.impDlr}, balPayments={self.balPayments})")






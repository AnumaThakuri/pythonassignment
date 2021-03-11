class date:
    count=0
    def __init__(self,d,m,y):
        self.__day=d
        self.__month=m
        self.__year=y
        date.datecount()
    def datecount():
        date.count=date.count+1
        print(date.count)
    def showdate(self):
        print('{}/{}/{}'.format(self.__day,self.__month,self.__year))
def main():
    d1=date(12,1,1998)
    d1.showdate()
    date.datecount()
    date.datecount()
    print('month=',d1.__year )

if __name__=='__main__':
    main()
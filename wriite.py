import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("fff.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # 초기 로그인 화면
        self.stackedWidget.setCurrentIndex(1)
        # 로그인 버튼 클릭시 loginaction 메서드로감
        self.login.clicked.connect(self.loginaction)
        # 회원가입 버튼 클릭시 넥스트 스택으로감 index[0]
        self.join.clicked.connect(self.next_stack)
        # 비밀번호 가입표시
        self.password.setEchoMode(QLineEdit.Password)
        # 가입완료 버튼클릭 시 five메서드로감
        self.confirmjoin.clicked.connect(self.five)
        self.previous_btn.clicked.connect(self.previous_stack)

    # 로그인 스택
    def previous_stack(self):
        self.stackedWidget.setCurrentIndex(1)

    def next_stack(self):
        # 회원가입 창
        self.stackedWidget.setCurrentIndex(0)

    # 가입완료 버튼 클릭 시 도달하는 메서드
    def five(self):
        # 회원가입창에서 쓰는 lineedit 이름 id_2
        id_2=self.id_2.text()
        # 회원가입창에서 쓰는 lineedit 이름 password_2
        password_2=self.password_2.text()
        confirm=self.confirm.text()
        call=self.call.text()
        address=self.address.text()
        # idread 리턴값인 아이디 리스트를 불러옴
        g=self.idread()
        # 5가지 요소 충족 확인
        if self.id_2.text()!='' and self.password_2.text()!='' and self.confirm.text()!='' and self.call.text()!='' and self.address.text()!='':
            QMessageBox.information(self,  '요건충족', 'dsadsa')
            # 입력받은 id_2가 id데이터베이스 g에 있을떄
            if id_2 in g:
                QMessageBox.information(self, '중복 오류 아이디', '오류 아이디')
            else:
                # id_2가 id텍스트에 없을때 다음 단계로 진행하기 위함
                QMessageBox.information(self, '올바른 아이디', '사용가능 아이디')
                # password_2가 비밀번호 확인과 다를때는 오류
                if self.password_2.text() != self.confirm.text():
                    QMessageBox.information(self, '비밀번호 오류', '오류 비밀번호')
                else:
                    # password_2가 비밀번호 확인과 같을 때 id,ps를 텍스트에 쓰고 id와 ps를 읽음
                    QMessageBox.information(self, '비밀번호가 맞습니다', '맞음 비밀번호')
                    self.idwrite(id_2)

                    self.pswrite(password_2)
                    self.idread()
                    self.psread()
                    self.id_2.clear()
                    self.password_2.clear()
                    self.confirm.clear()
                    self.call.clear()
                    self.address.clear()
        # 5가지 요소 충족이 안될떄 메시지박스 뜨게함
        else:
            QMessageBox.information(self,  '필수요소', 'sdasdsa')



    # id_2가 써있는 텍스트파일 설정
    def idwrite(self,id_2):
        # ID를 텍스트에 저장할 때 개행으로 저장하게함
        with open('ID.txt', 'a', encoding='utf8') as f:
            id=f'{id_2}\n'
            # 텍스트에 id_2값을 쓰게함
            f.write(id)
        f.close()
    # password_2 가입화면에 쓴 텍스트 파일 생성
    def pswrite(self,password_2):
        with open('PS.txt', 'a', encoding='utf8') as f:
            ps=f'{password_2}\n'
            f.write(ps)
        f.close()
    # idread 메서드를 호출시 읽은 아이디 텍스트를 리스트에 저장후 리스트를 리턴함
    def idread(self):
        f = open("ID.txt")
        # 메서드 내에서 쓰는 리스트 선언
        ist=[]
        # 텍스트를 읽음
        while True:
            line = f.readline()
            if not line: break
            # 텍스트에 개행과 공백이 있어 제거했음
            line = line.replace('\n', '')
            # 개행과 공백이 제거된 텍스트 라인을 ist리스트에 저장
            ist.append(line)
        f.close()
        # 저장된 리스트를 사용하기 위해 리턴값으로 리스트를 받음
        return ist
    def psread(self):
        f = open("PS.txt")
        pst = []
        while True:
            line = f.readline()
            if not line: break
            line = line.replace('\n', '')
            pst.append(line)

        f.close()
        return pst
    # 로그인 버튼을 눌렀을때 실행하는 메서드
    def loginaction(self):


        # 로그인 창에서 입력받는 값은 id,password임
        id=self.id.text()
        password=self.password.text()
        # b와 c라는 변수를 만들어 id리스트와 ps리스트를 받기위함
        b= self.idread()
        c=self.psread()
        # e라는 리스트를 만들어 [id,ps],[id,ps] 식으로 만들기 위함
        e=[]
        # id, ps 저장된 리스트를 e에 담음
        for i in range(0,len(b)):
            d=[b[i],c[i]]
            e.append(d)
        # 봄이라는 리스트를 만들어 로그인창에서 입력받는 리스트를 만듬
        bom=[id,password]

        # 봄이라는 입력받은 id 값과 ps 값이 저장된 id,ps 리스트인 e리스트 안에 있을때
        if bom in e:
            QMessageBox.information(self, '성공 로그인', '축하')
            # bom[0]은 id값 메인페이지에 로그인 성공한 id값을 넘기기 위함
            return bom[0]

        else:
            QMessageBox.information(self, '실패 로그인', '실패')
            self.id.clear()
            self.password.clear()


    def clear_id(self):
        self.id.clear()
        self.password.clear()




if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

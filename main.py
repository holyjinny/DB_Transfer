import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from TransferUI import (
    Ui_MainWindow,
)  # Qt Designer를 통해 작업한 UI 파일.py의 경로 설정


# PyQt6의 QMainWindow와 Ui_MainWindow를 상속받는 MainWindow 클래스 정의
class MainWindow(QMainWindow, Ui_MainWindow):
    # __init__ 생성자: MainWindow 인스턴스를 초기화하는 부분
    def __init__(self, *args, **kwargs) -> None:
        # 부모 클래스(QMainWindow)의 __init__ 메서드를 호출하여 기본 초기화 작업을 수행
        super().__init__(*args, **kwargs)

        # Ui_MainWindow의 UI를 현재 MainWindow 인스턴스(self)에 설정
        self.setupUi(self)


# QApplication 인스턴스를 생성. PyQt6 애플리케이션을 시작하려면 QApplication 객체가 필요함
app = QApplication(sys.argv)  # sys.argv를 사용해 커맨드라인 인자도 처리 가능

# MainWindow 인스턴스를 생성
window = MainWindow()

# MainWindow 인스턴스를 화면에 표시
window.show()

# 애플리케이션의 이벤트 루프를 실행하여 프로그램이 종료될 때까지 이벤트를 처리하도록 함
app.exec()

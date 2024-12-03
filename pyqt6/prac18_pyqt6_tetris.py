import random
import sys

from PyQt6.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QFrame, QApplication

class Tetris(QMainWindow):
    """테트리스 메인 윈도우 클래스"""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """애플리케이션 UI 초기화"""

        self.tboard = Board(self)  # 게임 보드 생성
        self.setCentralWidget(self.tboard)  # 보드를 중앙 위젯으로 설정

        self.statusbar = self.statusBar()  # 상태 표시줄 생성
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)  # 보드의 메시지를 상태 표시줄에 표시

        self.tboard.start()  # 게임 시작

        self.resize(180, 380)  # 창 크기 설정
        self.center()  # 창 중앙 정렬
        self.setWindowTitle('Tetris')  # 창 제목 설정
        self.show()  # 창 표시

    def center(self):
        """창을 화면 중앙에 배치"""
        qr = self.frameGeometry()  # 창의 현재 위치와 크기 정보 가져오기
        cp = self.screen().availableGeometry().center()  # 화면 중앙 계산

        qr.moveCenter(cp)  # 창 위치를 중앙으로 이동
        self.move(qr.topLeft())  # 창 이동


class Board(QFrame):
    """테트리스 게임 보드 클래스"""
    msg2Statusbar = pyqtSignal(str)  # 상태 표시줄에 메시지를 보내기 위한 신호

    BoardWidth = 10  # 보드 가로 크기
    BoardHeight = 22  # 보드 세로 크기
    Speed = 300  # 게임 속도 (ms)

    def __init__(self, parent):
        super().__init__(parent)
        self.initBoard()

    def initBoard(self):
        """보드 초기화"""

        self.timer = QBasicTimer()  # 타이머 생성
        self.isWaitingAfterLine = False  # 라인 제거 대기 상태

        self.curX = 0  # 현재 블록의 x 좌표
        self.curY = 0  # 현재 블록의 y 좌표
        self.numLinesRemoved = 0  # 제거된 라인 수
        self.board = []  # 보드 상태 저장

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)  # 키 입력 포커스 설정
        self.isStarted = False  # 게임 시작 상태
        self.isPaused = False  # 게임 일시정지 상태
        self.clearBoard()  # 보드 초기화

    def shapeAt(self, x, y):
        """보드의 특정 위치에 있는 블록 모양 반환"""
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        """보드의 특정 위치에 블록 모양 설정"""
        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self):
        """한 칸의 너비 반환"""
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        """한 칸의 높이 반환"""
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        """게임 시작"""
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()  # 보드 초기화

        self.msg2Statusbar.emit(str(self.numLinesRemoved))  # 상태 표시줄에 초기 라인 수 표시
        self.newPiece()  # 새로운 블록 생성
        self.timer.start(Board.Speed, self)  # 타이머 시작

    def pause(self):
        """게임 일시정지"""
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()  # 타이머 중지
            self.msg2Statusbar.emit("paused")  # 상태 표시줄에 "paused" 메시지 표시
        else:
            self.timer.start(Board.Speed, self)  # 타이머 재개
            self.msg2Statusbar.emit(str(self.numLinesRemoved))  # 상태 표시줄에 라인 수 표시

        self.update()  # 화면 갱신

    def paintEvent(self, event):
        """보드와 블록을 그림"""
        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        # 보드에 있는 블록 그리기
        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter, rect.left() + j * self.squareWidth(),
                                    boardTop + i * self.squareHeight(), shape)

        # 현재 블록 그리기
        if self.curPiece.shape() != Tetrominoe.NoShape:
            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                                self.curPiece.shape())


    def keyPressEvent(self, event):
        """키 입력 처리"""

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            # 게임이 시작되지 않았거나 현재 블록이 없는 경우 기본 동작 처리
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key.Key_P:
            self.pause()  # 'P' 키로 게임 일시정지
            return

        if self.isPaused:
            return  # 게임이 일시정지 상태일 때 키 입력 무시

        # 방향키 및 동작 키 처리
        elif key == Qt.Key.Key_Left.value:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)  # 왼쪽 이동

        elif key == Qt.Key.Key_Right.value:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)  # 오른쪽 이동

        elif key == Qt.Key.Key_Down.value:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)  # 블록 시계 방향 회전

        elif key == Qt.Key.Key_Up.value:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)  # 블록 반시계 방향 회전

        elif key == Qt.Key.Key_Space.value:
            self.dropDown()  # 스페이스 키로 블록 빠르게 내리기

        elif key == Qt.Key.Key_D:
            self.oneLineDown()  # 'D' 키로 한 줄 아래로 이동

        else:
            super(Board, self).keyPressEvent(event)  # 그 외 키는 기본 처리


    def timerEvent(self, event):
        """타이머 이벤트 처리"""

        if event.timerId() == self.timer.timerId():
            # 라인 제거 대기 상태면 새 블록 생성
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()  # 한 줄 아래로 이동

        else:
            super(Board, self).timerEvent(event)

    def clearBoard(self):
        """보드를 초기화하여 빈 상태로 만듦"""
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

    def dropDown(self):
        """블록을 가능한 가장 아래로 내림"""
        newY = self.curY

        while newY > 0:
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
            newY -= 1

        self.pieceDropped()


    def oneLineDown(self):
        """블록을 한 줄 아래로 이동"""
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()


    def pieceDropped(self):
        """블록을 내린 후 라인을 제거하고 새 블록 생성"""
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()


    def removeFullLines(self):
        """완성된 라인을 제거"""
        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n += 1

            if n == Board.BoardWidth:
                rowsToRemove.append(i)

        rowsToRemove.reverse()

        for m in rowsToRemove:
            for k in range(m, Board.BoardHeight - 1):
                for l in range(Board.BoardWidth):
                    self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines += len(rowsToRemove)

        if numFullLines > 0:
            self.numLinesRemoved += numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))  # 제거된 라인 수 갱신

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()


    def newPiece(self):
        """새로운 블록 생성"""
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            # 블록이 이동할 수 없으면 게임 종료
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")


    def tryMove(self, newPiece, newX, newY):
        """블록을 새로운 위치로 이동 가능 여부 확인"""
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True


    def drawSquare(self, painter, x, y, shape):
        """블록의 사각형을 그림"""
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
                         x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
                         y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe:
    """테트리스 블록 모양을 정의하는 클래스"""
    # 블록 모양을 나타내는 상수
    NoShape = 0  # 블록 없음
    ZShape = 1   # Z 모양 블록
    SShape = 2   # S 모양 블록
    LineShape = 3  # 일자 블록
    TShape = 4   # T 모양 블록
    SquareShape = 5  # 정사각형 블록
    LShape = 6   # L 모양 블록
    MirroredLShape = 7  # 반전된 L 모양 블록


class Shape:
    """테트리스 블록의 모양과 동작을 정의하는 클래스"""
    # 블록 모양에 대한 좌표 테이블
    # 각 모양에 대한 상대 좌표로 구성된 튜플
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),  # NoShape
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),  # ZShape
        ((0, -1), (0, 0), (1, 0), (1, 1)),   # SShape
        ((0, -1), (0, 0), (0, 1), (0, 2)),   # LineShape
        ((-1, 0), (0, 0), (1, 0), (0, 1)),   # TShape
        ((0, 0), (1, 0), (0, 1), (1, 1)),    # SquareShape
        ((-1, -1), (0, -1), (0, 0), (0, 1)),  # LShape
        ((1, -1), (0, -1), (0, 0), (0, 1))    # MirroredLShape
    )

    def __init__(self):
        """Shape 객체를 초기화"""
        self.coords = [[0, 0] for _ in range(4)]  # 블록의 좌표 (4개)
        self.pieceShape = Tetrominoe.NoShape  # 초기 모양은 NoShape로 설정
        self.setShape(Tetrominoe.NoShape)  # 기본 모양 설정

    def shape(self):
        """현재 블록의 모양 반환"""
        return self.pieceShape

    def setShape(self, shape):
        """블록 모양 설정"""
        table = Shape.coordsTable[shape]  # 지정된 모양의 좌표 테이블 가져오기
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]  # 각 블록의 좌표를 설정
        self.pieceShape = shape  # 블록 모양 업데이트

    def setRandomShape(self):
        """무작위로 블록 모양 설정"""
        self.setShape(random.randint(1, 7))  # 1에서 7까지의 모양 중 하나를 랜덤 선택


    def x(self, index):
        """지정된 블록의 x 좌표 반환"""
        return self.coords[index][0]

    def y(self, index):
        """지정된 블록의 y 좌표 반환"""
        return self.coords[index][1]

    def setX(self, index, x):
        """지정된 블록의 x 좌표 설정"""
        self.coords[index][0] = x

    def setY(self, index, y):
        """지정된 블록의 y 좌표 설정"""
        self.coords[index][1] = y

    def minX(self):
        """블록의 가장 작은 x 좌표 반환"""
        return min(self.coords[i][0] for i in range(4))

    def maxX(self):
        """블록의 가장 큰 x 좌표 반환"""
        return max(self.coords[i][0] for i in range(4))

    def minY(self):
        """블록의 가장 작은 y 좌표 반환"""
        return min(self.coords[i][1] for i in range(4))

    def maxY(self):
        """블록의 가장 큰 y 좌표 반환"""
        return max(self.coords[i][1] for i in range(4))

    def rotateLeft(self):
        """블록을 왼쪽으로 회전"""
        if self.pieceShape == Tetrominoe.SquareShape:
            return self  # 정사각형 블록은 회전하지 않음

        result = Shape()
        result.pieceShape = self.pieceShape  # 회전 후에도 동일한 모양 유지

        for i in range(4):
            result.setX(i, self.y(i))  # y 좌표를 x 좌표로 설정
            result.setY(i, -self.x(i))  # x 좌표를 반전하여 y 좌표로 설정

        return result

    def rotateRight(self):
        """블록을 오른쪽으로 회전"""
        if self.pieceShape == Tetrominoe.SquareShape:
            return self  # 정사각형 블록은 회전하지 않음

        result = Shape()
        result.pieceShape = self.pieceShape  # 회전 후에도 동일한 모양 유지

        for i in range(4):
            result.setX(i, -self.y(i))  # y 좌표를 반전하여 x 좌표로 설정
            result.setY(i, self.x(i))  # x 좌표를 y 좌표로 설정

        return result

def main():
    """애플리케이션 실행을 위한 메인 함수"""
    app = QApplication([])  # PyQt6 애플리케이션 객체 생성
    tetris = Tetris()       # Tetris 클래스의 인스턴스 생성 (메인 윈도우)
    sys.exit(app.exec())    # 이벤트 루프 실행 및 애플리케이션 종료 처리

# 애플리케이션 실행
if __name__ == '__main__':
    main()  # main 함수 호출
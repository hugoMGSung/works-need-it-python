## 파이썬 응용예제

### PyQt6

- 모듈 설치

```shell
pip install PyQt6
```

#### 기본 예제
1. prac01_pyqt6.py

    ```python
    import sys
    from PyQt6.QtWidgets import QApplication, QWidget

    # 애플리케이션 클래스 초기화
    app = QApplication(sys.argv)
    # QWidget 클래스에서 기본 창 생성
    window = QWidget()
    # 창 크기 설정
    window.setWindowTitle("PyQt6 MainWindow")
    window.setGeometry(100, 100, 400, 300)  # (x, y, width, height)
    # 창 표시
    window.show()
    # 애플리케이션 이벤트 루프 시작
    sys.exit(app.exec())
    ```


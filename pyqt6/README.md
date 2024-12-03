## 파이썬 응용예제

### PyQt6

- 모듈 설치

```shell
pip install PyQt6
```

- PySide6 도 같이 설치할 것
    - QtDesigner 설치됨(가장 간편!)

#### 버전 테스트
1. prac00_pyqt6_version.py

#### 기본 예제
1. prac01_pyqt6_basic.py

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

    <img src="https://raw.githubusercontent.com/hugoMGSung/works-need-it-python/refs/heads/main/images/tot0001.png" width="500">


#### 영화플레이어 클로닝
- 우선 가져오기 - 제대로 동작 안하네? ^^

#### Tutorial
- https://zetcode.com/pyqt6/layout/ 참조
- 다이얼로그, 드래그 앤 드랍, Custom Widgets 등 생략
## 파이썬 MCP Agent 만들기

### Cursor IDE에서 해야함

### MCP (Model Context Protocol) 소개
- AI가 외부 데이터의 도구(Tools)에 효과적으로 연결할 수 있는 표준화된 방식
- 특히 다양한 도구의 표준화된 연결로 많이 활용되고 있음
    - MCP Server: 사용할 수 있는 도구(tool)를 정의하고 제공하는 역할
    - MCP Client: 정의된 도구를 불러와 사용 (Claude Desktop, Cursor, OpenAI Agents SDK)

### 셋팅
- OpenAI 키 발급
- Youtube Data API Key 발급
- .env에 키값 저장
- 가상환경 설정
- 관련 모듈 설치
    ```shell
    > pip install mcp openai-agents streamlit youtube-transcript-api python-dotenv requests
    ```
- MCP 연동 테스트 - [소스](./mcp01_server_test.ipynb)

- mcp.json에 Python경로 및 MCP서버 경로 저장

- Cursor IDE에서 해야하는 지 다시 확인할 것
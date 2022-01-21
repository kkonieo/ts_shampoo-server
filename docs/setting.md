

## poetry shell ( vscode 연동)

```bash
$ poetry shell
. /home/.../.cache/pypoetry/virtualenvs/ts-shampoo-server-0UDTPI6N-py3.8/bin/activate
# /home/nyh/.cache/pypoetry/virtualenvs/ts-shampoo-server-0UDTPI6N-py3.8/bin/python <  이걸 interpreter path 에 입력해준다.
```

`poetry shell` 명령어를 입력했을 떄 뜨는 경로 bin 까지 복사해서 `/python`을 덧붙여준다.
`enter interpreter path` 버튼을 눌러 위 경로를 입력해준다.


커맨드 팔레트 열기 ( ctrl + shift + p ) ->
select interpreter


## vscode 셋팅 ( lint, format )

ctrl+shift+p 
-> workspace settings (JSON) 열어서 아래 코드를 입력한다

```json
// .vscode/settings.json
{
  // 린팅 활성화
  "python.linting.enabled": true,
  // flake8 사용
  "python.linting.flake8Enabled": true,

  // 별도로 .flake8 config 파일을 생성하여 관리한다면 아래 내용은 불필요
  "python.linting.flake8Args": [
    // black의 기본 max line length 값은 88 이므로 맞춰준다.
    // https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length
    "--max-line-length=88",
    // 무시 할 에러코드
    // 에러 코드 확인 -> https://flake8.pycqa.org/en/latest/user/error-codes.html
    "--ignore=F401,E402"
  ],

  // black formatter 사용
  "python.formatting.provider": "black",

  "[python]": {
    // 코드를 저장할 떄 마다 실행
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      // isort 사용 설정
      "source.organizeImports": true,
      "python.sortImports": true
    }
  }
}
```
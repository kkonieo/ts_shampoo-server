## 프로젝트 생성

## 1. Poetry 설정

```
1. pip install poetry => poetry 설치

2. poetry install 
    - 처음에만 설정 
    - enter를 쳐서 넘어간다.

3. poetry shell
    - poetry 가상환경에 접근한다.

4. poetry add <package 명>
    - 사용할 패키지들을 추가한다.
    - 자동으로 의존성 파일에 해당 목록이 업데이트 된다.
    - `--dev` 옵션을 통해 개발 환경에만 사용할 옵션을 설정할 수 있다.
    - ex) poetry add flake8 --dev
    
5. poetry remove <package 명>
    - 패키지들을 삭제한다
    - 자동으로 의존성 파일에서 해당 목록이 삭제된다.

6. exit
    - poetry 가상환경을 종료한다.
```

## 2. 프로젝트 구조 설정

```
1. django-admin startproject config .
    - root 위치에서 설정
    - 프로젝트의 config 설정 폴더

2. django-admin startapp <app파일명>
    - root/apps 위치에서 설정
    - 페이지 api 기능 설정 폴더

```

## 3. Django migrations Workflow

```
1. 등록할 ORM의 name을 설정
    => ex) "apps.user"

2. config/settings/base.py
    - ORM 모델 등록할 app 등록
    - INSTALLED_APPS
    => ex) "apps.user"

3. python manage.py makemigrations 
    - 새로운 ORM 모델 생성 시

3. python manage.py migrate
    - ORM 모델 migrations
```

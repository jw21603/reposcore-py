import re
import requests
import logging

def validate_repo_format(repo: str) -> bool:
    pattern = r'^[\w\-]+/[\w\-]+$'
    if re.fullmatch(pattern, repo):
        return True
    else:
        print("저장소 형식이 올바르지 않습니다. 'owner/repo' 형식으로 입력해주세요.")
        return False

def check_github_repo_exists(repo: str) -> bool:
    """
    GitHub 저장소 존재 여부를 확인하는 함수.
    
    API 요청을 통해 저장소가 실제로 존재하는지 확인합니다.
    """
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    elif response.status_code == 403:
        logging.warning("⚠️ GitHub API 요청 실패: 403 (요청 횟수 초과 또는 인증 오류)")
        logging.info("ℹ️ 해결 방법: --token 옵션 또는 GITHUB_TOKEN 환경 변수 사용")
    elif response.status_code == 404:
        logging.warning(f"⚠️ 저장소 '{repo}'가 존재하지 않습니다.")
    else:
        logging.warning(f"⚠️ 요청 실패: HTTP 상태 코드 {response.status_code}")

    return False

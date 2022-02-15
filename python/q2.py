import re


def solution(new_id: str):
    """_summary_
    - 아이디의 길이는 3자 이상 15자 이하여야 합니다.
    - 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
    - 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

    1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

    제약조건

    - new_id는 길이 1 이상 1,000 이하인 문자열입니다.
    - new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
    - new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.
    """

    answer = ""
    # Step 1
    answer = new_id.lower()
    # Step 2
    answer = re.sub("[^a-z0-9\-_.]", "", answer)
    # Step 3
    answer = re.sub("\.[.]*", ".", answer)
    # Step 4
    answer = re.sub("^[.]", "", answer)
    answer = re.sub("[.]$", "", answer)
    # Step 5
    if answer == "":
        answer = "a"
    # Step 6
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[-1:] == ".":
            answer = answer[0:-1]
    # Step 7
    while len(answer) <= 2:
        answer = answer + answer[-1:]

    return answer


if __name__ == "__main__":
    solution("abcdefghijklmn.p")

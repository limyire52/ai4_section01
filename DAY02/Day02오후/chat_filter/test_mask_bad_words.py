"""실행 방법: python test_mask_bad_words.py (Python 3.9 이상)."""

from mask_bad_words import mask_bad_words


def run_tests() -> None:
    # 기본 동작과 여러 금지어를 확인합니다.
    assert mask_bad_words("너는 바보야", ["바보"]) == "너는 **야"
    assert mask_bad_words("바보 멍청이", ["바보", "멍청이"]) == "** ***"
    assert mask_bad_words("BAD, Bad, bad!", ["bad"]) == "***, ***, ***!"

    # 빈 입력, 빈 목록, 빈 금지어, 중복 금지어를 확인합니다.
    assert mask_bad_words("안녕하세요!", ["바보"]) == "안녕하세요!"
    assert mask_bad_words("", ["바보"]) == ""
    assert mask_bad_words("그대로 유지", []) == "그대로 유지"
    assert mask_bad_words("빈 단어 무시", [""]) == "빈 단어 무시"
    assert mask_bad_words("BAD", ["", "bad", "bad"]) == "***"

    # 특수문자와 겹치는 금지어를 확인합니다.
    assert mask_bad_words("a.b a+b [x]", ["a.b", "a+b", "[x]"]) == "*** *** ***"
    assert mask_bad_words("aXb", ["a.b"]) == "aXb"
    assert mask_bad_words("ababa", ["aba"]) == "*****"
    assert mask_bad_words("abc", ["ab", "bc"]) == "***"
    assert mask_bad_words("abc", ["bc", "ab"]) == "***"

    # 부분 일치, 전체 일치, 메시지보다 긴 금지어를 확인합니다.
    assert mask_bad_words("badly", ["bad"]) == "***ly"
    assert mask_bad_words("bad", ["badword"]) == "bad"
    assert mask_bad_words("게임", ["게임"]) == "**"

    # 공백, 줄바꿈, 문장부호, 이모지가 보존되는지 확인합니다.
    assert (
        mask_bad_words("안녕\tBAD\n바보! 😀", ["bad", "바보"])
        == "안녕\t***\n**! 😀"
    )

    # 결과 길이와 원본 입력이 보존되는지 확인합니다.
    words = ["bad", "바보"]
    message = "BAD 바보"
    assert len(mask_bad_words(message, words)) == len(message)
    assert words == ["bad", "바보"] and message == "BAD 바보"

    print("19개 assert 테스트 모두 통과")


if __name__ == "__main__":
    run_tests()

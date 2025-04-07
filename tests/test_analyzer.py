from reposcore.analyzer import RepoAnalyzer

def test_example_calculate_scores():
    analyzer = RepoAnalyzer("oss2025hnu/reposcore-py")
    analyzer.participants = {
        "test_user1": {
            "p_enhancement": 2,
            "p_bug": 1,
            "p_documentation": 3,
            "i_enhancement": 2,
            "i_bug": 2,
            "i_documentation": 2,
        },
        "test_user2": {
            "p_enhancement": 0,
            "p_bug": 0,
            "p_documentation": 10,
            "i_enhancement": 0,
            "i_bug": 0,
            "i_documentation": 10,
        },
        "test_user3": {
            "p_enhancement": 3,
            "p_bug": 3,
            "p_documentation": 20,
            "i_enhancement": 5,
            "i_bug": 5,
            "i_documentation": 5,
        },
        "test_user4": {
            "p_enhancement": 1,
            "p_bug": 1,
            "p_documentation": 1,
            "i_enhancement": 0,
            "i_bug": 0,
            "i_documentation": 0,
        },
        "test_user5": {
            "p_enhancement": 2,
            "p_bug": 0,
            "p_documentation": 0,
            "i_enhancement": 0,
            "i_bug": 0,
            "i_documentation": 0,
        },
        "test_user6": {
            "p_enhancement": 0,
            "p_bug": 0,
            "p_documentation": 0,
            "i_enhancement": 3,
            "i_bug": 3,
            "i_documentation": 6,
        },
        "test_user7": {
            "p_enhancement": 2,
            "p_bug": 2,
            "p_documentation": 12,
            "i_enhancement": 4,
            "i_bug": 4,
            "i_documentation": 20,
        },
        "test_user8": {
            "p_enhancement": 0,
            "p_bug": 2,
            "p_documentation": 6,
            "i_enhancement": 1,
            "i_bug": 1,
            "i_documentation": 3,
        },
        "test_user9": {
            "p_enhancement": 0,
            "p_bug": 2,
            "p_documentation": 5,
            "i_enhancement": 2,
            "i_bug": 0,
            "i_documentation": 1,
        },
        "test_user10": {
            "p_enhancement": 3,
            "p_bug": 0,
            "p_documentation": 3,
            "i_enhancement": 3,
            "i_bug": 0,
            "i_documentation": 3,
        },
    }

    scores = analyzer.calculate_scores()
    assert scores["test_user1"] == 25, "test_user1 결과값이 일치하지 않습니다."
    assert scores["test_user2"] == 0, "test_user2 결과값이 일치하지 않습니다."
    assert scores["test_user3"] == 79, "test_user3 결과값이 일치하지 않습니다."
    assert scores["test_user4"] == 8, "test_user4 결과값이 일치하지 않습니다."
    assert scores["test_user5"] == 6, "test_user5 결과값이 일치하지 않습니다."
    assert scores["test_user6"] == 0, "test_user6 결과값이 일치하지 않습니다."
    assert scores["test_user7"] == 72, "test_user7 결과값이 일치하지 않습니다."
    assert scores["test_user8"] == 25, "test_user8 결과값이 일치하지 않습니다."
    assert scores["test_user9"] == 21, "test_user9 결과값이 일치하지 않습니다."
    assert scores["test_user10"] == 24, "test_user10 결과값이 일치하지 않습니다."
from survey import AnonymousSurvey
import pytest

@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的AnonymousSurvey实例"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_language_survey(language_survey):
    """测试单个答案会被妥善存储"""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
    
def test_three_language_survey(language_survey):
    """测试三个答案会被妥善存储"""
    languages = ['Chinese', 'English', 'Japines']
    for language in languages:
        language_survey.store_response(language)
        
    for language in languages:
        assert language in language_survey.responses
from survey import AnonymousSurvey
            
question = "What language did you first leran to speak?"
language_survey = AnonymousSurvey(question)

# 显示问题并存储答案
language_survey.show_result()
print("Enter 'q' at any time to quit.\n")
while True:
    language = input(language_survey.question)
    if language != 'q':
        language_survey.store_response(language)
    else:
        break
    
print("\nThank you to everyone who participated in the survey!")
language_survey.show_result()
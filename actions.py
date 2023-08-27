from typing import Any, Text, Dict, List
import openai
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# openai.api_key = ""

# def chatgpt_rasa(prompt):
#     try: 
#         response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt= prompt,
#         temperature=1,
#         max_tokens=800,
#         top_p=1,
#         frequency_penalty=0.2,
#         presence_penalty=0.2,
#         )
#         anwer = response.choices[0].text
#     except: anwer = "Hiện giờ hệ thống đang bảo trì"
#     print(anwer)
#     return anwer
openai.api_key = "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"

def chatgpt_rasa(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= prompt,
    temperature=1,
    max_tokens=800,
    top_p=1,
    frequency_penalty=0.6,
    presence_penalty=0.6,
    )
    print(response.choices[0].text)
    return response.choices[0].text


class ActionGreet(Action):
    def name(self):
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và chatbot giáo dục Uniberty. Hãy trả lời câu "+ str(textex) +", đồng thời hỏi tên người đó và không nói tiếp bất cứ gì hết."
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_greet",text =  json)
        return []
class ActionGoodbye(Action):
    def name(self):
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với dự định tạm biệt (goodbye). Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_goodbye",text =  json)
        return []
    
class ActionThank(Action):
    def name(self):
        return "action_thank"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với dự định cảm ơn người dùng. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_thank",text =  json)
        return [] 

class ActionConsultation(Action):
    def name(self):
        return "action_consultation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với dự định tư vấn nghề nghiệp cho người dùng để định hướng rõ về nghề nghiệp. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_consultation",text =  json)
        return [] 
    
class ActionAskName(Action):
    def name(self):
        return "action_ask_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là cuộc hội thoại giữa người và Chatbot tư vấn tuyển sinh Uniberty. Nếu là câu chào thì chào lại và đặt câu hỏi hỏi tên người dùng, ngược lại thì trả lời ngắn gọn không đặt câu hỏi. Trả lời câu" + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_ask_name",text =  json)
        return [] 
    
class ActionHelp(Action):
    def name(self):
        return "action_help"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với chức năng hỗ trợ người dùng định hướng nghề nghiệp và trả lời các câu liên quan tới tuyển sinh. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_help",text =  json)
        return [] 
    
    
class ActionBenchmark(Action):
    def name(self):
        return "action_benchmark"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        major=tracker.get_slot("majors")
        university=tracker.get_slot("university")
        text = f"Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Cho biết điểm chuẩn ngành {major}, {university}  là 26.3 . Hãy trả lời câu " + textex +" một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_benchmark",text =  json)
        return [] 
    
    
    
class ActionTuition(Action):
    def name(self):
        return "action_tuition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với học phí đại trà là 17 triệu. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_tuition",text =  json)
        return [] 
    
    
class ActionCurriculum(Action):
    def name(self):
        return "action_curriculum"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Hãy trả lời câu " + textex + " một cách ngắn gọn có kèm theo link trường để học sinh tham khảo"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_curriculum",text =  json)
        return [] 

class ActionCriterias(Action):
    def name(self):
        return "action_criterias"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với chỉ tiêu chung là 60 người/ngành. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_criterias",text =  json)
        return [] 

class ActionReview(Action):
    def name(self):
        return "action_review"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với dự định giới thiệu về trường. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_review",text =  json)
        return [] 


class ActionProfile(Action):
    def name(self):
        return "action_profile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với dự định cho đường link nộp hồ sơ cho trường đại học. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_profile",text =  json)
        return [] 
    
class ActionFacilities(Action):
    def name(self):
        return "action_facilities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với dự định giới thiệu cơ sở vật chất. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_facilities",text =  json)
        return [] 
    
class ActionDormitory(Action):
    def name(self):
        return "action_dormitory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Với dự định giới thiệu kiến túc xá. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_dormitory",text =  json)
        return [] 

class ActionCareerOpportunities(Action):
    def name(self):
        return "action_career_opportunities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Ý định là về cơ hội nghề nghiệp và học tập. Hãy trả lời câu " + textex + " một cách ngắn gọn"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        # json  = {"0":{"intent": intent, 
        #          "entity":[name,majors,university],
        #          "answer":answer,
        #          },}
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_career_opportunities",text =  json)
        return [] 
    
class ActionDefaultFallback(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Hãy trả lời câu " + textex + " một cách ngắn gọn mang tính giáo dục"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_default_fallback",text =  json)
        return [] 
class ActionDefaultFallback(Action):
    def name(self):
        return "action_comparison_school"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        textex=tracker.latest_message['text']
        text = "Đây là một cuộc trò chuyện giữa người và AI chatbot tư vấn giáo dục Uniberty. Dự định so sánh các trường. Hãy trả lời câu " + textex + " một cách ngắn gọn mang tính giáo dục"
        answer=chatgpt_rasa(text)
        name = tracker.get_slot("name")
        majors =tracker.get_slot("majors")
        university =tracker.get_slot("university")
        school1 = tracker.get_slot("school1")
        school2 =tracker.get_slot("school2")
        
        intent = tracker.latest_message.get('intent', {})
        json = f"""{{\"intent\": {intent}, 
                  \"entity\":[{name},{majors},{university},{school1},{school2}],
                  \"answer\":{answer},
                }}"""
        dispatcher.utter_message(template="utter_comparison_school",text =  json)
        return [] 
import g4f
import g4f.Provider
from g4f.Provider.Bing import Tones
def create_start_of_story(cookies):
    messages = [{"role" : "system", "content" : "Do you know DungeonAI? You are a copy of Dungeon AI please write ONLY story in your response (5 sentences)"}]
    messages.append({"role": "user", "content" : "can you create a start of story, theme-'cyberpank' player role-'cop' language:'ukrainian', you must TALK story with player to player with name 'Ярослав' think of a place where the story begins"})
    print(messages)
    try:
        response = g4f.ChatCompletion.create(
            # model="gpt-4-turbo",
            # provider=g4f.Provider.Bing,
            model=g4f.models.command_r_plus,
            provider=g4f.Provider.HuggingChat,
            messages=messages,
            stream=True,
            cookies=cookies,
            # tone=Tones.creative,
        )
        
    except Exception as e:
        print(f"first error {e}")
        response = g4f.ChatCompletion.create(
            # model="gpt-4-turbo",
            # provider=g4f.Provider.Bing,
            model=g4f.models.command_r_plus,
            provider=g4f.Provider.HuggingChat,
            messages=messages,
            stream=True,
            cookies=cookies,
            # tone=Tones.creative,
        )
    text = ""
    for i in response:
        text+=i
        print(text)
    return text
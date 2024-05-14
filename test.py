import g4f
import g4f.Provider
from g4f.Provider.Bing import Tones
import time
import requests
import os
cookies = {
    "__stripe_mid" : "e10d408c-737a-438c-b0d0-242a95ad1dd50f5ef4",
    "__stripe_sid" : "f31e6026-af4f-4c5e-8203-6a62c03eea25d3d0f0",
    "aws-waf-token" : "4cf763d4-9ec2-4c5b-b266-36dd08520032:DQoAvexMExQJAAAA:WG37pMJ2VsCFucBa95ATgTb2DtJS/GRH5yoPnAaJQZkhZV5DhQBVuK9UzWl2jLWdE4cWgm2+0OSx4VYP7ZQrzV/GJm2WQko1kL9QUNvcA7UD5wtJX4ckMo0a8KVBoIIPP6wclmodniCzSX9+eis/gwFG5Huu+NeAE0EeT116U7FFCyHCmjequGtt/L7ZjUNvZlERYpc7MhkQoqxLHY+Rq62wqv7x2znVKfYwudD7wnzrnTQqg1BGYEV0bY4z67oLAwRj5LI=",
    "token" : "zxrnCzSdWdheKwXsvXKYujPvajXhnEfEKHupaQMZTphqMMzmsjNyAsiUXpDpcwwcURBEraFNlbxjQAmyNGpFihpCKcSXENQxhQdOYebjCgAGddpUzvJJJdgFoxrkbdee",
    "token" : "zxrnCzSdWdheKwXsvXKYujPvajXhnEfEKHupaQMZTphqMMzmsjNyAsiUXpDpcwwcURBEraFNlbxjQAmyNGpFihpCKcSXENQxhQdOYebjCgAGddpUzvJJJdgFoxrkbdee"
}
time1 = time.time()
# response = g4f.ChatCompletion.create(
#     model = g4f.models.default,
#     provider = g4f.Provider.Bing,
#     stream=True,
#     messages=[{"role" : "user", "content" : "Hi, who are you?(3 sentenses)"}],
#     tone=Tones.creative,
# )

# response = requests.post(url="https://api.deepinfra.com/v1/inference/mistralai/Mixtral-8x22B-Instruct-v0.1", data={"input": {'role' : 'user', 'content' : 'Hi!'}, "stream": 'False'})
messages = []
messages.append({"role" : "assistant", "content" : """
Звичайно, я можу допомогти розділити кожну тему на підпункти, щоб краще відповідати формату презентації тривалістю 15 хвилин. Ось оновлена версія тексту презентації:

**Вступ:**

"Доброго дня всім! Сьогодні я хочу розповісти вам про надзвичайно важливу зірку, без якої життя на Землі було б неможливим – Сонце. У цій презентації ми розглянемо три основні аспекти впливу Сонця на нашу планету: біологічний, географічний та фізичний. Кожен з цих аспектів демонструє, наскільки тісно наше існування пов'язане з цією яскравою зіркою."

**Перша частина: Біологічний вплив:**

1. "По-перше, Сонце відіграє ключову роль у фотосинтезі. Рослини, які є основою харчового ланцюга, залежать від сонячного світла, щоб перетворювати вуглекислий газ і воду на кисень і глюкозу, забезпечуючи нас їжею."

2. "Сонячне світло також впливає на наші біологічні ритми. Воно допомагає регулювати наші цикли сну та активності, що має вирішальне значення для здоров'я і добробуту."

3. "Крім того, сонячне світло сприяє виробленню вітаміну D в нашому організмі. Вітамін D необхідний для здоров'я кісток і сильної імунної системи."

**Друга частина: Географічний вплив:**

1. "Сонячна енергія є основним фактором, що визначає клімат на Землі. Регіони, які отримують більше прямого сонячного світла, як правило, мають тепліший клімат, тоді як регіони з меншою кількістю сонячного світла мають холодніший клімат."

2. "Сонячне світло також впливає на формування рельєфу. Наприклад, вітрова ерозія, спричинена нагріванням сонцем, формує піщані дюни в пустелях."

3. "Танення снігів і льодів під впливом сонячного тепла живить річки та водоспади, забезпечуючи водою численні екосистеми."

**Третя частина: Фізичний вплив:**

1. "Сонце є основним джерелом енергії для Землі. Завдяки сонячному світлу і теплу відбувається рух повітряних мас, утворення вітрів і океанічних течій."

2. "Ми також можемо безпосередньо використовувати сонячну енергію для виробництва електроенергії за допомогою сонячних панелей і теплових електростанцій."

3. "Сонячна активність, така як спалахи і корональні викиди маси, впливає на магнітне поле Землі, створюючи полярні сяйва і потенційно впливаючи на наші технології, такі як супутники і електричні мережі."

**Заключення:**

"Підсумовуючи, хочу наголосити, що Сонце відіграє життєво важливу роль у підтримці життя на Землі. Воно впливає на біологічні, географічні та фізичні процеси, забезпечуючи енергією, формуючи клімат і рельєф, а також підтримуючи здоров'я і добробут живих істот. Сподіваюся, ця презентація допомогла вам по-новому оцінити значення Сонця в нашому житті. Дякую за увагу!"

Ця структура забезпечує більш детальний огляд кожної теми, при цьому зберігаючи чіткий фокус і відповідність до 15-хвилинного формату презентації.
"""})
while True:
    time1 = time.time()
    inp = input("Input: ")
    messages.append({"role" : 'user', "content" : inp})
    response = g4f.ChatCompletion.create(
        model = g4f.models.command_r_plus,
        provider = g4f.Provider.HuggingChat,
        stream=True,
        messages=messages,
    )

    # print(response.text)
    text = ''
    for i in response:
        try :
            text += i
        except:
            pass
        os.system("clear")
        print(text)
    time2 = time.time()
    time_all = time2 - time1
    print(time_all)
    messages.append({"role" : "assistant", "content" : text})
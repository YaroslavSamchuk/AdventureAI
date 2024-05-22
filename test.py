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
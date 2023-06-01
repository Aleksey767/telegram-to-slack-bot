# Examples of work

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/8748b55e-aa67-4637-8b86-a9b0b880fee9)

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/a2e0fdd7-05e1-46fd-9a67-53a48306fec7)

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/820db0e1-7fb9-487a-811e-adac73951d11)



# How to use
### Step 1
Change the variables:

You need to find this variables in every project file and change value.Use your personal values. How to find or create them you can find on the Internet

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/e680d517-0cf3-4cdc-900d-121f52ab6f41)

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/0dddd7d8-8817-4057-bf75-8af266f44c96)

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/b094528f-1237-489a-a6c5-6a6e0cc3c5cd)

### Step 2
Run main.py script in your console:
Move to the root of the project and type - python main.py 

Or just press the button in your IDE 

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/7f9d4cc1-d429-4b12-905e-02ac4bc2547e)

You should see: 

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/7b7e621c-a20a-4507-8c25-21de0efdcc92)

After entering the phone number, if you entered correctly variables api_hash,api_id and phone you can enter the code. After that you should see:

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/08e558ce-7ffe-418a-b0b3-1cc7655fd252)

### Step 3

Close your terminal and run Dockerfile
If you use Linux, you need to change that(from 'python', to 'python3'):

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/2428f0bc-191c-47fa-b064-eb1b2029d8a0)

Сuz in my case i I got an error.If you use Windows without docker container - don't change anything. Let it be - 'python'
Also you need to configure port. In my case i have custom proxy-server and my port is 80. But you can use something else, for example - ngrok and 8080.

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/43ad61e4-ec23-4fd8-a448-2c8fb4b59272)

Now,when your pycash and session file was create, you can create docker image, use:

#### docker build -t tgbot:v.1 . 

#### docker run -d -p 80:80 --name tgbot tgbot:v.1

That is all, you can start this bot at docker container, or at IDE (main.py) like python script. Also you need to clear MySQL database and use your telegram channel. You can do this With your own hands in python or use slack-commands(don't forget configure "Interactivity & Shortcuts". Use your parameters):

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/d2ac3a1e-0365-4cf7-a740-a7591b4e1364)

![image](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/fd6009b4-44b9-4876-a0f1-5cc8e8ba5010)









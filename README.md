# Examples of work

![1](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/3c757ae9-271e-40f2-abc1-e09d12df8007)

![2](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/bebe31aa-7445-44d6-a134-7b013cb449c0)

![3](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/9622f40a-faa5-4c85-bb1a-4501d593f669)



# How to use
### Step 1
Change the variables:

You need to find this variables in every project file and change value.Use your personal values. How to find or create them you can find on the Internet

![4](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/26cabcfb-7a8b-4109-a935-29949f2f338e)

![5](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/74136d48-6b15-4d40-a3d8-92fbd25eb838)

![6](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/3850601c-063f-475f-bd0d-02a87be18fad)


### Step 2
Run main.py script in your console:
Move to the root of the project and type - python main.py 

Or just press the button in your IDE 

![7](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/169e1290-063a-407c-93a6-2cdc0e7a12f7)


You should see: 

![8](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/e402b10f-f85e-4b75-aebc-1ed2729ef72a)


After entering the phone number, if you entered correctly variables api_hash,api_id and phone you can enter the code. After that you should see:

![9](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/ab1fa88a-2cf7-4391-be1a-4da516aa255c)


### Step 3

Close your terminal and run Dockerfile
If you use Linux, you need to change that(from 'python', to 'python3'):

![10](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/ba4c4634-cbf4-4aa4-8824-8c16875c4c44)


Сuz in my case i I got an error.If you use Windows without docker container - don't change anything. Let it be - 'python'
Also you need to configure port. In my case i have custom proxy-server and my port is 80. But you can use something else, for example - ngrok and 8080.

![11](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/b2c305ec-56ca-4c82-baed-bf1a94d40109)


Now,when your pycash and session file was create, you can create docker image, use:

#### docker build -t tgbot:v.1 . 

#### docker run -d -p 80:80 --name tgbot tgbot:v.1

That is all, you can start this bot at docker container, or at IDE (main.py) like python script. Also you need to clear MySQL database and use your telegram channel. You can do this With your own hands in python or use slack-commands(don't forget configure "Interactivity & Shortcuts". Use your parameters):

![12](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/249560b5-8068-42ad-aab8-d6e4ffc5c56c)


![13](https://github.com/Aleksey767/telegram-to-slack-bot/assets/98593351/7d336b83-99b5-48f3-860d-109953ea9077)










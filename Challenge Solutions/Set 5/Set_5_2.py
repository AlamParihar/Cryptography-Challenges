from multiprocessing import Process
import time
import Set_5_2_bot
import Set_5_2_middle
import Set_5_2_user

#run bot, mitm and client scripts in parallel

if __name__== '__main__':

    b=Process(target=Set_5_2_bot.main, name='bot', args=())
    b.start()
    time.sleep(1)
    m=Process(target=Set_5_2_middle.main, name='middle', args=())
    m.start()
    time.sleep(1)
    u=Process(target=Set_5_2_user.main, name='user', args=())
    u.start()

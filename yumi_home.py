'''
工作室名字:玉米开花
根据地用户:个人使用、只有几个人知道的秘密基地、分享后所有人可见..
根据地用途:工具分享、数据收集、兴趣推荐、经历分享、综合主站.....
最喜欢的现有模块:兴趣推荐、图片处理工具、智慧词典、留言区
现有模块改进灵感:。。。
原创模块:。。
原创模块一句话功能介绍:。。
'''
import streamlit as st
from PIL import Image

page=st.sidebar.radio('玉米首页',['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

def page_1():
    st.write('工作室名字:玉米开花')
    st.image('slogan.png')
    st.text('''
工作室名字:玉米开花
根据地用户:个人使用、只有几个人知道的秘密基地、分享后所有人可见..
根据地用途:工具分享、数据收集、兴趣推荐、经历分享、综合主站.....
最喜欢的现有模块:兴趣推荐、图片处理工具、智慧词典、留言区
现有模块改进灵感:。。。
原创模块:。。
原创模块一句话功能介绍:。。
''')
    with open ('霞光.mp3','rb')as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3',start_time=10)
    st.write('我的电影推荐')
    st.write('-----------------------------')
    st.write('我的游戏推荐')
    st.write('-----------------------------')
    st.write('我的书籍推荐')
    st.write('-----------------------------')
    st.write('我的习题集推荐')
    st.write('-----------------------------')
    

def page_2():
    st.write(':heart_eyes:图片换色小程序:sunglasses:')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:   
            st.image(img_change(img,0,2,1))
        with tab3:   
            st.image(img_change(img,1,2,0))
        with tab4:   
            st.image(img_change(img,1,0,2))

def page_3():
    st.write(':blue[智能词典]')
    with open('words_space.txt','r',encoding='utf-8') as f:
        word_list=f.read().split('\n')
    for i in range(len(word_list)):
        word_list[i]=word_list[i].split("#")
    words_dict={}
    for i in word_list:
        words_dict[i[1]]=[int(i[0]),i[2]]#单词：[编号，中文意思]

    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])#编号：次数

    word=st.text_input("请输入要查询的单词：")
    if word in words_dict:
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in times_dict.items():
                message += str(k)+"#"+str(v)+'\n'
            message = message[:-1]
            f.write(message)
            
        st.write(words_dict[word])
        st.write('此单词被查询次数：',times_dict[n])
        if word == 'python' or word == 'C++' or word == 'java':
            st.code('''
                    #恭喜你触发了彩蛋，这是一行编程代码：
                    print('hello world!')
                    ''')
        if word == 'balloon' or word == 'birthday':
            st.balloons()
        if word == 'winter' or word == 'snow':
            st.snow()
        if word == 'yumi':
            st.write('作者邀请你喝奶茶！')     

def page_4():
    st.write("聊天室")
    with open("leave_messages.txt",'r',encoding='utf-8') as f:
        msg_list = f.read().split('\n')
    for i in range(len(msg_list)):
        msg_list[i] = msg_list[i].split("#")
    for i in msg_list:
        if i[1] == '阿短':
            with st.chat_message('🌽'):
                st.write(i[1],"：",i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🌈'):
                st.write(i[1],"：",i[2])
        elif i[1] == '制作组':
            with st.chat_message('🧑‍🔬'):
                st.header(i[1],"：",i[2])
        elif i[1] == '匿名用户1':
            with st.chat_message('🧨'):
                st.write(i[1],"：",i[2])
        elif i[1] == '匿名用户2':
            with st.chat_message('🧧'):
                st.write(i[1],"：",i[2])
        elif i[1] == '匿名用户3':
            with st.chat_message('🧧'):
                st.write(i[1],"：",i[2])
    name = st.selectbox("你的名字是：",['阿短','编程猫','制作组','匿名用户1','匿名用户2','匿名用户3'])
    new_msg = st.text_input("冒个泡吧：")
    if st.button('发送'):
        msg_list.append([str(int(msg_list[-1][0])+1),name,new_msg])
        with open("leave_messages.txt",'w',encoding='utf-8') as f:
            msg=''
            for i in msg_list:
                msg += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            msg = msg[:-1]
            f.write(msg)
    # st.write('我的留言区')
    # with open('leave_messages.txt','r',encoding='utf-8') as f:
    #     messages_list=f.read().split('\n')
    # for i in range(len(messages_list)):
    #     messages_list[i]=messages_list[i].split("#")
    # for i in messages_list:
    #     if i[1]=='阿短':
    #         with st.chat_message('🌴'):
    #             st.text(i[1]+':'+i[2])
    #     elif i[1]=='编程猫':
    #         with st.chat_message('🐱'):
    #             st.write(i[1],':',i[2])
    # name=st.selectbox('我是.....',['阿短','编程猫'])
    # new_message= st.text_input('我想要说的话.....')
    # if st.button('确认留言'):
    #     messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
    #     with open('leave_messages.txt','w',encoding='utf-8')as f:
    #         message=''
    #         for i in messages_list:
    #             message += i[0]+'#'+i[1]+'#'+i[2]+'\n'
    #         message=message[:-1]
    #         f.write(message)
            
def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array =  img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img
    
if page=='我的兴趣推荐':
    page_1()
elif page=='我的图片处理工具':
    page_2() 
elif page=='我的智能词典':
    page_3()
elif page=='我的留言区':
    page_4()

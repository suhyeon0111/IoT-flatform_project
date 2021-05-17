from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("restaurant pos")
root.geometry("800x420+0+20")
root.resizable(False, False)
root.configure(bg='skyblue')

# 새로운 창 만들기
# top = Toplevel(root)
# top.title("결제창")

# 테이블 1번
def b1event():
    if(b1['text'] == 'table1'):
         b1['text'] = '주문 목록'
        # b1['fg']='red'
        # b1['bg'] = 'yellow'
    elif ( b1['text'] == '주문 목록'):
            Mbox=messagebox.askquestion("카드결제", "결제가 정상적으로 처리되었습니까?")
            # 메시지 박스에서 yes를 누르면 table1로 초기화 시키기
            if( Mbox == 'yes'):
                 b1['text'] = 'table1'
            #메시지 박스에서 no를 누르면 뒤로 가라는 알림창 생성
            else:
                messagebox.showinfo('결제창','back')
  
b1=Button(root, text="table1", command = b1event,  width=20, height=7, overrelief="solid")
b1.pack()
b1.place(x=40, y=30)  

# 테이블 2번
def b2event():
    if(b2['text'] == 'table2'):
        b2['text'] = '주문 목록'
        #b2['fg']='red'
        #b2['bg'] = 'yellow'
    elif (b2['text'] == '주문 목록'):
            Mbox2=messagebox.askquestion("카드결제", "결제가 정상적으로 처리되었습니까?")
            # 메시지 박스에서 yes를 누르면 table1로 초기화 시키기
            if( Mbox2 == 'yes'):
                b2['text'] = 'table2'
            #메시지 박스에서 no를 누르면 뒤로 가라는 알림창 생성
            else:
                messagebox.showinfo('결제창','back')
  
b2=Button(root, text="table2", command = b2event,width=20, height=7, overrelief="solid")
b2.pack()
b2.place(x=300, y=30)

#  테이블 3번
def b3event():
    if(b3['text'] == 'table3'):
        b3['text'] = '주문 목록'
        #b3['fg']='red'
        #b3['bg'] = 'yellow'
    elif (b3['text'] == '주문 목록'):
            Mbox3=messagebox.askquestion("카드결제", "결제가 정상적으로 처리되었습니까?")
            # 메시지 박스에서 yes를 누르면 table1로 초기화 시키기
            if( Mbox3 == 'yes'):
                b3['text'] = 'table3'
            #메시지 박스에서 no를 누르면 뒤로 가라는 알림창 생성
            else:
                messagebox.showinfo('결제창','back')

b3=Button(root, text="table3",command = b3event,width=20, height=7, overrelief="solid")
b3.pack()
b3.place(x=560, y=30)

# 테이블 4번
def b4event():
    if(b4['text'] == 'table4'):
        b4['text'] = '주문 목록'
        #b4['fg']='red'
        #b4['bg'] = 'yellow'
    elif (b4['text'] == '주문 목록'):
            Mbox4=messagebox.askquestion("카드결제", "결제가 정상적으로 처리되었습니까?")
            # 메시지 박스에서 yes를 누르면 table1로 초기화 시키기
            if( Mbox4 == 'yes'):
                b4['text'] = 'table4'
            #메시지 박스에서 no를 누르면 뒤로 가라는 알림창 생성
            else:
                messagebox.showinfo('결제창','back')
b4=Button(root, text="table4",command = b4event, width=20, height=7, overrelief="solid")
b4.pack()
b4.place(x=40, y=200)

# 테이블 5번

def b5event():
    if(b5['text'] == 'table5'):
        b5['text'] = '주문 목록'
        #b5['fg']='red'
        #b5['bg'] = 'yellow'
    elif (b5['text'] == '주문 목록'):
            Mbox5=messagebox.askquestion("카드결제", "결제가 정상적으로 처리되었습니까?")
            # 메시지 박스에서 yes를 누르면 table1로 초기화 시키기
            if( Mbox5 == 'yes'):
                b5['text'] = 'table5'
            #메시지 박스에서 no를 누르면 뒤로 가라는 알림창 생성
            else:
                messagebox.showinfo('결제창','back')

b5=Button(root, text="table5",command = b5event,width=20, height=7, overrelief="solid")
b5.pack()
b5.place(x=300, y=200)

def b6event():
    if(b6['text'] == 'table6'):
        b6['text'] = '주문 목록'
        #b6['fg']='red'
        #b6['bg'] = 'yellow'
    elif (b6['text'] == '주문 목록'):
            Mbox6=messagebox.askquestion("카드결제", "결제가 정상적으로 처리되었습니까?")
            # 메시지 박스에서 yes를 누르면 table1로 초기화 시키기
            if( Mbox6 == 'yes'):
                b6['text'] = 'table6'
            #메시지 박스에서 no를 누르면 뒤로 가라는 알림창 생성
            else:
                messagebox.showinfo('결제창','back')
  
b6=Button(root, text="table6",command = b6event, width=20, height=7, overrelief="solid")
b6.pack()
b6.place(x=560, y=200)


def notification():
    messagebox.showinfo("식기를 채우세요")

# tableware = Button(root, text = "식기", command= notification, width = 20, height=1)
# tableware.place(x=0, y=350)

def notification_card():
    Toplevel()

   
    # messagebox.askquestion("카드결제", "결제가 정상적으로 처리되었습니까?")
# card = Button(root, text = "카드", command= notification_card, width = 20, height=1)
# card.place(x=150, y=350)

def notification_cash():
    messagebox.askquestion("현금결제", "결제가 정상적으로 처리되었습니까?")
# cash = Button(root, text = "현금", command= notification_cash, width = 20, height=1)
# cash.place(x=300, y=350)

root.mainloop()
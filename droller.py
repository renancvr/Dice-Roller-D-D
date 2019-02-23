from tkinter import *
from random import randint

class roller(object):
	def __init__(self,i):
		self.frame0 = Frame(i)
		self.frame0.pack()
		self.frame1 = Frame(i)
		self.frame1.pack(side = LEFT)
		self.frame2 = Frame(i, bg = 'darkgray')
		self.frame2.pack(side = LEFT)
		self.frame3 = Frame(i)
		self.frame3.pack(side = LEFT)
		

		self.txt1 = Label(self.frame1, text = 'D20', bg = 'darkgray', width = 3)
		self.txt1.pack()
		self.ent1 = Entry(self.frame2, width = 5)
		self.ent1.insert(0,'0')
		self.ent1.pack()
		self.result1 = Label(self.frame3, text = '', fg = 'darkblue')
		self.result1.pack()

		self.txt2 = Label(self.frame1, text = 'D12', bg = 'darkgray',  width = 3)
		self.txt2.pack()
		self.ent2 = Entry(self.frame2, width = 5)
		self.ent2.insert(0,'0')
		self.ent2.pack()
		self.result2 = Label(self.frame3, text = '', fg = 'darkblue')
		self.result2.pack()

		self.txt3 = Label(self.frame1, text = 'D10', bg = 'darkgray',  width = 3)
		self.txt3.pack()
		self.ent3 = Entry(self.frame2, width = 5)
		self.ent3.insert(0,'0')
		self.ent3.pack()
		self.result3 = Label(self.frame3, text = '', fg = 'darkblue')
		self.result3.pack()

		self.txt4 = Label(self.frame1, text = 'D8 ', bg = 'darkgray',  width = 3)
		self.txt4.pack()
		self.ent4 = Entry(self.frame2, width = 5)
		self.ent4.insert(0,'0')
		self.ent4.pack()
		self.result4 = Label(self.frame3, text = '', fg ='darkblue')
		self.result4.pack()

		self.txt5 = Label(self.frame1, text = 'D6 ', bg = 'darkgray',  width = 3)
		self.txt5.pack()
		self.ent5 = Entry(self.frame2, width = 5)
		self.ent5.insert(0,'0')
		self.ent5.pack()
		self.result5 = Label(self.frame3, text = '', fg = 'darkblue')
		self.result5.pack()

		self.txt6 = Label(self.frame1, text = 'D4 ', bg = 'darkgray',  width = 3)
		self.txt6.pack()
		self.ent6 = Entry(self.frame2, width = 5)
		self.ent6.insert(0,'0')
		self.ent6.pack()
		self.result6 = Label(self.frame3, text = '', fg = 'darkblue')
		self.result6.pack()

		self.b1 = Button(self.frame0, text = 'Jogar!', command = self.roll, width = 12)
		self.b1.pack()
		self.total = Label(self.frame0, text = '  ', bg = 'black', fg ='green', width = 10, height = 2, font = 10)
		self.total.pack()
		self.critical = Label(self.frame0, text = '', fg = 'red')
		self.critical.pack()

	def roll(self):
		n20 = self.ent1.get()
		n12 = self.ent2.get()
		n10 = self.ent3.get()
		n8 = self.ent4.get()
		n6 = self.ent5.get()
		n4 = self.ent6.get()
		l1 = []
		l2 = []
		l3 = []
		l4 = []
		l5 = []
		l6 = []
		for i in range(int(n20)):
			x = randint(1,20)
			l1.append(x)
		d20 = sum(l1)
		self.result1['text'] = l1
		if l1.count(20) > 0:
			self.critical['text'] = 'Sucesso Crítico'
			self.critical['fg'] = 'darkgreen'
		elif l1.count(1) > 0:
			self.critical['text']  = 'Falha Crítica'
			self.critical['fg'] = 'red'
		else:
			self.critical['text'] = ''
		for i in range(int(n12)):
			x = randint(1,12)
			l2.append(x)
		d12 = sum(l2)
		self.result2['text'] = l2
		for i in range(int(n10)):
			x = randint(1,10)
			l3.append(x)
		d10 = sum(l3)
		self.result3['text'] = l3
		for i in range(int(n8)):
			x = randint(1,8)
			l4.append(x)
		d8 = sum(l4)
		self.result4['text'] = l4
		for i in range(int(n6)):
			x = randint(1,6)
			l5.append(x)
		d6 = sum(l5)
		self.result5['text'] = l5
		for i in range(int(n4)):
			x = randint(1,4)
			l6.append(x)
		d4 = sum(l6)
		self.result6['text'] = l6
		soma = d20 + d12 + d10 + d8 + d6 + d4
		self.total['text'] = soma





i = Tk()
roller(i)
i.title('Dice Roller 1.0')
i.geometry('225x225')
i.mainloop()
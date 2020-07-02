import tkinter as tk
from tkinter import font  as tkfont
from tkinter.messagebox import *
class SampleApp(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		self.title("Storage Module")
		self.geometry("800x600+300+300")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}
		for F in (StartPage, authPage, retreiveModule,storageModulePg1,retreiveModulePg1):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("StartPage")

	def show_frame(self, page_name):
		'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()


class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Select Storage or Retrieval Module", font=controller.title_font)
		
		label.grid(column=2,row=1,sticky='N')

		storageButton = tk.Button(self, text="Storage Module",
							command=lambda: controller.show_frame("authPage"))
		retreiveButton = tk.Button(self, text="Retrieval Module",
							command=lambda: controller.show_frame("retreiveModule"))
	
		storageButton.grid(column=1,row=2,sticky='E',padx = 40,pady=100)
		retreiveButton.grid(column=3,row=2,sticky = 'W',padx = 20,pady = 80)
	
		emergencyButton = tk.Button(self,text='Emergency Stop')
		emergencyButton.grid(column=2,row=3,sticky='S',pady=100)


class authPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)		
		self.controller = controller
		label = tk.Label(self, text="Login Page", font=controller.title_font)
		label.grid(column=1,row=1,sticky='N')
		enterLabel = tk.Label(self,text="Enter your User Name:")
		enterLabel.grid(column=0,row=2,sticky='E')
		self.entry = tk.Entry(self,width=40)
		self.entry.grid(column=1,row=3,sticky='E')
		enterPassLabel = tk.Label(self,text='Enter the Password:')
		enterPassLabel.grid(column=0,row=4,sticky='E')
		self.entryPass = tk.Entry(self,width=40)
		self.entryPass.grid(column=1,row=5)
		self.enterButton = tk.Button(self,text='Enter',command=self.saveVal)
		self.enterButton.grid(column=2,row=7,stick='W')
		self.backButton = tk.Button(self,text='Back',command=lambda:controller.show_frame('StartPage'))
		self.backButton.grid(column=0,row=7,sticky='E',padx=100,pady=10)
		emergencyButton = tk.Button(self,text="Emergency Stop")
		emergencyButton.grid(column=1,row=9,sticky='S',pady=100)

	def saveVal(self,arg=None):
		status = False
		resultUser = self.entry.get()
		resultPass = self.entryPass.get()
		# print(resultUser, '  ',resultPass)
		if resultUser == '123' and resultPass =='123':
			stepLabel = tk.Label(self,text="Press Accept to move to the next step")
			stepLabel.grid(column=1,row=6,sticky='E',pady=10)
			status = True
		else :
			stepLabel = tk.Label(self,text="Password or User Name does not match ")
			stepLabel.grid(column=1,row=6,sticky='E',pady=10)
		self.entry.delete(0,tk.END)
		self.entryPass.delete(0,tk.END)
		if status == True:
			button = tk.Button(self, text="Accept",
						   command=lambda: [button.destroy(),stepLabel.destroy(),
						   self.controller.show_frame("storageModulePg1")])
			button.grid(column=2,row=8,sticky='W')
		status = False

class retreiveModule(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Retrieval Page", font=controller.title_font)
		# label.pack(side="top", fill="x", pady=10)
		label.grid(column=0,row=0,sticky ='N')	
		dispatchLabel =  tk.Label(text='Enter the Unique Dispatch ID:')
		dispatchLabel.grid(column=0,row=1,sticky ='E')
		self.dispatchEntry = tk.Entry(self,width=40)
		self.dispatchEntry.grid(column=0,row=2,sticky='E')
		checkButton = tk.Button(self,text='Check',commnd = self.saveVal)	
		checkButton.grid(column=2,row=3,stciky='W',pady=10)
		backButton = tk.Button(self,text='Back',command=lambda: controller.show_frame('StartPage'))
		backButton.grid(column=0,row=3,stciky='W',padx=100,pady=10)
		emergencyButton = tk,Button(self,text='Emergency Stop')
		emergencyButton.grid(column=1,row=5,sticky='S',pady=100)

	def saveVal(self,arg=None):
		status = False
		resultDispatch = self.dispatchEntry.get()
		if resultDispatch == '123':
			resultLabel = tk.Label("Loading Your Order")
			resultLabel.grid(column=2,row=4,sticky='S')
			status = True
		else:
			resultLabel = tk.Label('Order not in the system')
			resultLabel.grid(column=2,row=4,sticky='S')
			status= False
		self.resultDispatch.delete(0,tk.END)

		if status== True:
			acceptButton = tk.Button(self,text='Next',command=lambda:[resultLabel.destroy()
				,acceptButton.destroy(),self.controller.show_frame("retreiveModulePg1")])
		status= False 

class storageModulePg1(tk.Frame):

	'''
	TODO: Add the label for invoice number,unique ID.
	'''
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Storage Module", font=controller.title_font)
		label.grid(column=1,row=1)
		button = tk.Button(self, text="Next",
						   command=lambda: controller.show_frame("StartPage"))
		button.pack()

 
class retreiveModulePg1(tk.Frame):


if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()
import tkinter
import time
from tkinter import messagebox

# Author: Alberto J. De Jesus
# E-mail:
# A class that simulates a Finite State Machine

class FSM:
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # Regular expression:
    # ($|&)((>)(a|b|c|d|e|r|o|i|f|s|g)*(:)(0|1|2|3|4|5|6|7|8|9)*)*(!)*
    __systemSyntax__ = {0: {
        0: {'$': 1, '&': 1},
        1: {'>': 2, '!': 4, ';': 4},
        2: {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'r': 2, 'i': 2, 'o': 2, 's': 2, ':': 3},
        3: {'0': 3, '1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 3, '8': 3, '9': 3, '>': 2, '!': 4, ';': 4},
        4: {'!': 4, ';': 4}
    }}
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    __mainWindow__ = None
    __inputBox__ = None

    def helpWindow(self):
        messagebox.showinfo("Help Window", "HOW TO USE THE APP:\n\n\t This application is simple, on the text "
                                           "box shown on the main window you can input any combination of symbols"
                                           " that you think might be part of the syntax and after writing it,"
                                           "press ok to check if it is. \n\nMAIN SYNTAX (Regular expression): "
                                           "\n\t($|&)((>)([a|b|c|d|e|r|o|i|f|s|g)*(:)(0|1|2|3|4|5|6|7|8|9)*)*(!)*"
                                           "\nEXAMPLES:\n\t1) $>idabc:013843!  "
                                           "\n\t2) &>idgo:1234>idrar:8027784545!)"
                                           "\n\t3) $>idcar:453223432>idbar:45432223>idccard:33224322!")

    def quitWindow(self):
        self.mainWindow.destroy()

    def __processWindow__(self):
        showWindow = tkinter.Tk()
        showWindow.title("Process......")

        stateLabel = tkinter.Label(showWindow, text="Current State: 0", font=("Arial", 25))
        stateLabel.pack(side="left", padx=20, pady=20)

        inputLabel = tkinter.Label(showWindow, text="?", font=("Arial", 25))
        inputLabel.pack(side="left", padx=5, pady=20)

        equalLabel = tkinter.Label(showWindow, text="=", font=("Arial", 25), background="white", borderwidth=2, relief="solid")
        equalLabel.pack(side="left", padx=0, pady=20)

        systemLabel = tkinter.Label(showWindow, text="?", font=("Arial", 25))
        systemLabel.pack(side="left", padx=5, pady=20)

        def analyzeText():
            textTokens = list(self.inputBox.get())
            textTokens.append(';')
            currToken = 0
            currSyntax = 0
            isPartOfSyntax = False
            while (not isPartOfSyntax) & (currSyntax < self.__systemSyntax__.__len__()):
                syntax = self.__systemSyntax__[currSyntax]
                currState = 0
                isPartOfState = True
                while isPartOfState & (currToken < textTokens.__len__()):
                    keys = list(syntax[currState].keys())
                    currKey = 0
                    isPartOfState = False
                    while (not isPartOfState) & (currKey < keys.__len__()) & (currToken < textTokens.__len__()):
                        stateLabel['text'] = "Current State: " + str(currState)
                        equalLabel['background'] = "white"
                        inputLabel['text'] = textTokens[currToken]
                        systemLabel['text'] = keys[currKey]
                        inputLabel.update()
                        systemLabel.update()
                        stateLabel.update()
                        equalLabel.update()
                        time.sleep(0.5)
                        if keys[currKey] == textTokens[currToken]:
                            equalLabel['background'] = "green"
                            equalLabel.update()
                            currState = syntax[currState][keys[currKey]]
                            currToken = currToken + 1
                            isPartOfState = True
                            time.sleep(0.8)
                        else:
                            equalLabel['background'] = "red"
                            equalLabel.update()
                            currKey = currKey + 1
                            isPartOfState = False
                            time.sleep(0.3)
                    if (currState == (syntax.__len__() - 1)) & (currToken == textTokens.__len__()):
                        isPartOfSyntax = True
                    elif not isPartOfState:
                        isPartOfSyntax = False
                currSyntax = currSyntax + 1
            if isPartOfSyntax:
                messagebox.showinfo("Correct Syntax", "Your input is part of the syntax.(TRUE)")
            else:
                messagebox.showwarning("Wrong Syntax", "Your input is not part of the syntax.(FALSE)")
            showWindow.destroy()

        showWindow.after(200, analyzeText)
        showWindow.mainloop()

    def getSyntax(self):
        return self.__systemSyntax__

    def __init__(self):
        prepWindow = tkinter.Tk()
        prepWindow.winfo_toplevel().title("Syntax Parser")
        menuBar = tkinter.Menu(prepWindow)
        menuBar.add_command(label="Help", command=self.helpWindow)
        prepWindow.config(menu=menuBar)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
        FLabel = tkinter.Label(prepWindow, text="Write an expression:", font=("Arial", 22))
        FLabel.pack(side="left", padx=1, pady=15)

        prepBox = tkinter.Entry(prepWindow, bd=5, font=("Arial", 18))
        prepBox.pack(side="left", padx=0, pady=15)
        self.inputBox = prepBox

        analyzeButton = tkinter.Button(prepWindow, text="Analyze", command=self.__processWindow__, font=("Arial", 14))
        analyzeButton.pack(side="left", padx=15, pady=15)

        quitButton = tkinter.Button(prepWindow, text="Quit", command=self.quitWindow, font=("Arial", 14))
        quitButton.pack(side="left", padx=1, pady=15)
        self.mainWindow = prepWindow
        prepWindow.mainloop()


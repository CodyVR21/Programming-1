﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Red
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(10, 210)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(195, 71)
        self._button1.TabIndex = 0
        self._button1.Text = "Calcultate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Red
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(211, 210)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(195, 71)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Red
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(409, 210)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(195, 71)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.Red
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(10, 3)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(594, 199)
        self._listBox1.TabIndex = 4
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkRed
        self.ClientSize = System.Drawing.Size(618, 293)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Cursor = System.Windows.Forms.Cursors.Default
        self.Name = "MainForm"
        self.Text = "prog 152a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e): # Calculate
 #       3223
         finalsum = 15586428
         sum = 0
         num = 0
         while (sum < final sum ):
             sum += 3 
         pass
 

    def Button2Click(self, sender, e): # Clear
        self._lisBox1.Items.Clear()

    def Button3Click(self, sender, e): # Exit
        Application.Exit()
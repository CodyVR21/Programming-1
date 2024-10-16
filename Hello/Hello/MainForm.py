﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(44, 51)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(814, 263)
        self._label1.TabIndex = 0
        self._label1.Text = "Hello world!"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(116, 382)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(121, 53)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(405, 381)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(117, 54)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(668, 382)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(132, 53)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(924, 473)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Hello"
        self.ResumeLayout(False)
        
        

    def Button1Click(self, sender, e):
        self._label1.Text = "Hello, world!"

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        
    def Button3Click(self, sender, e):
        Application.Exit()
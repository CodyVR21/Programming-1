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
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.LightSkyBlue
        self._button1.Location = System.Drawing.Point(123, 358)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(141, 44)
        self._button1.TabIndex = 0
        self._button1.Text = "Details"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.LightSkyBlue
        self._button2.Location = System.Drawing.Point(406, 358)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(131, 45)
        self._button2.TabIndex = 1
        self._button2.Text = "Start"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.LightSkyBlue
        self._button3.Location = System.Drawing.Point(690, 357)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(134, 45)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(406, 124)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(182, 39)
        self._label1.TabIndex = 3
        self._label1.Text = "Hello World!"
        # 
        # MainForm
        # 
        self.AcceptButton = self._button1
        self.BackColor = System.Drawing.Color.Blue
        self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
        self.ClientSize = System.Drawing.Size(1001, 435)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Cursor = System.Windows.Forms.Cursors.Hand
        self.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
        self.Name = "MainForm"
        self.Text = "Hello World!"
        self.ResumeLayout(False)

    def Button1Click(self, sender, e):
        self._label1.Text = "Hello World!"
           
    def Button2Click(self, sender, e):
        self._label1.Text = ""
           
    def Button3Click(self, sender, e):
        Application.Exit()
        
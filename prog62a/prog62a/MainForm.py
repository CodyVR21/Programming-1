﻿import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Red
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(0, 107)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(318, 51)
        self._label1.TabIndex = 0
        self._label1.Text = "Enter your Number!!"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.SystemColors.HotTrack
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.SystemColors.Control
        self._textBox1.Location = System.Drawing.Point(324, 114)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(218, 44)
        self._textBox1.TabIndex = 1
        self._textBox1.TextChanged += self.TextBox1TextChanged
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Red
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
        self._label2.Location = System.Drawing.Point(0, 161)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(542, 70)
        self._label2.TabIndex = 2
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(0, 234)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(153, 78)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(191, 234)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(153, 82)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(389, 234)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(153, 82)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkBlue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(35, 28)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(480, 78)
        self._label3.TabIndex = 6
        self._label3.Text = "Factorials"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Maroon
        self.ClientSize = System.Drawing.Size(546, 362)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog62a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        input = float(self._textBox1.Text)
        output = math.factorial(input)
        self._label2.Text = "The factorial for your number is"+str(output)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def TextBox1TextChanged(self, sender, e):
        pass
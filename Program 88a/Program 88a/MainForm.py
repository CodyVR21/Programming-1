﻿import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self._label16 = System.Windows.Forms.Label()
        self._label17 = System.Windows.Forms.Label()
        self._label18 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Red
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(109, 46)
        self._label1.TabIndex = 0
        self._label1.Text = "Num 1:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Red
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(7, 173)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(125, 46)
        self._label2.TabIndex = 1
        self._label2.Text = "Difference"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Red
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 127)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(109, 46)
        self._label3.TabIndex = 2
        self._label3.Text = "Sum:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Red
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(13, 68)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(109, 46)
        self._label4.TabIndex = 3
        self._label4.Text = "Num 2:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Red
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 357)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(109, 46)
        self._label5.TabIndex = 4
        self._label5.Text = "Max:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Red
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(12, 311)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(125, 46)
        self._label6.TabIndex = 5
        self._label6.Text = "Distance:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Red
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(12, 265)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(109, 46)
        self._label7.TabIndex = 6
        self._label7.Text = "Average:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Red
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(12, 219)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(109, 46)
        self._label8.TabIndex = 7
        self._label8.Text = "Product:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.Red
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(13, 403)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(109, 46)
        self._label9.TabIndex = 8
        self._label9.Text = "Min:"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Firebrick
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.Control
        self._button3.Location = System.Drawing.Point(302, 454)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(141, 61)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.Orange
        self._label12.Location = System.Drawing.Point(138, 127)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(227, 30)
        self._label12.TabIndex = 14
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.Orange
        self._label13.Location = System.Drawing.Point(143, 173)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(227, 30)
        self._label13.TabIndex = 15
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.Orange
        self._label14.Location = System.Drawing.Point(138, 219)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(227, 30)
        self._label14.TabIndex = 16
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.Orange
        self._label15.Location = System.Drawing.Point(138, 265)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(227, 30)
        self._label15.TabIndex = 17
        # 
        # label16
        # 
        self._label16.BackColor = System.Drawing.Color.Orange
        self._label16.Location = System.Drawing.Point(138, 311)
        self._label16.Name = "label16"
        self._label16.Size = System.Drawing.Size(227, 30)
        self._label16.TabIndex = 18
        # 
        # label17
        # 
        self._label17.BackColor = System.Drawing.Color.Orange
        self._label17.Location = System.Drawing.Point(138, 373)
        self._label17.Name = "label17"
        self._label17.Size = System.Drawing.Size(227, 30)
        self._label17.TabIndex = 19
        # 
        # label18
        # 
        self._label18.BackColor = System.Drawing.Color.Orange
        self._label18.Location = System.Drawing.Point(128, 419)
        self._label18.Name = "label18"
        self._label18.Size = System.Drawing.Size(227, 30)
        self._label18.TabIndex = 20
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Orange
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(138, 24)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(227, 35)
        self._textBox1.TabIndex = 21
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.Orange
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(138, 79)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(227, 35)
        self._textBox2.TabIndex = 22
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Firebrick
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(7, 452)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(141, 61)
        self._button1.TabIndex = 23
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Firebrick
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(154, 452)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(141, 61)
        self._button2.TabIndex = 24
        self._button2.Text = "Calculate"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DodgerBlue
        self.ClientSize = System.Drawing.Size(455, 518)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label18)
        self.Controls.Add(self._label17)
        self.Controls.Add(self._label16)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Program 88a"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button2Click(self, sender, e): # Calculate
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        Sum = num1 + num2
        Dif = num1 - num2
        # TODO: finish product and average 
        Abs = abs(Dif)
        Max = 0 
        Min = 0
        if num1 >= num2:
            Max = num1
            # Min = num2
        else:  # Otherwise...
           Max = num2
           
        if Max == num1: # If Max has the same value as num1 (==)
             Min = num2 
        else:
            Min = num1
            
       # TODO: put the rest of the nums in labels and finish clear btn
        self._label17.Text = str(Max)
        self._label18.Text = str(Min)
        Sum = num1 + num2 
        Dif = num1 - num2
        Product = num1 * num2 
        Average = (num1 + num2)/2
        Distance = abs(Dif)
        self._label12.Text = str(Sum)
        self._label13.Text = str(Dif)
        self._label14.Text = str(Product)
        self._label15.Text = str(Average)
        self._label16.Text = str(Distance)
        
        

    def Button1Click(self, sender, e): # Clear
         self._label12.Text = ""
         self._label13.Text = ""
         self._label14.Text = ""
         self._label15.Text = ""
         self._label16.Text = ""
         self._label17.Text = ""
         self._label18.Text = ""
         self._textBox1.Text = ""
         self._textBox2.Text = ""

    def Button3Click(self, sender, e): # Exit 
        Application.Exit()
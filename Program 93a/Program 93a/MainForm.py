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
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Blue
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(164, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(280, 50)
        self._label1.TabIndex = 0
        self._label1.Text = "The Electric Bill"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(35, 459)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(152, 62)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(399, 459)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(152, 62)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(222, 459)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(152, 62)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Blue
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.HighlightText
        self._label2.Location = System.Drawing.Point(12, 83)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(224, 39)
        self._label2.TabIndex = 5
        self._label2.Text = "Enter kWh used:"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.Blue
        self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.SystemColors.Window
        self._textBox1.Location = System.Drawing.Point(242, 83)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(224, 33)
        self._textBox1.TabIndex = 6
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.Blue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(12, 135)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(224, 32)
        self._label3.TabIndex = 7
        self._label3.Text = "Base Rate:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Blue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(12, 180)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(224, 32)
        self._label4.TabIndex = 8
        self._label4.Text = "Surcharge:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Blue
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(12, 227)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(224, 32)
        self._label5.TabIndex = 9
        self._label5.Text = "City Tax:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Blue
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(12, 382)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(224, 32)
        self._label6.TabIndex = 10
        self._label6.Text = "Total Bill:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Blue
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label7.Location = System.Drawing.Point(12, 424)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(224, 32)
        self._label7.TabIndex = 11
        self._label7.Text = "Late Bill:"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Blue
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label8.Location = System.Drawing.Point(242, 135)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(224, 32)
        self._label8.TabIndex = 12
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.Blue
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label9.Location = System.Drawing.Point(242, 180)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(224, 32)
        self._label9.TabIndex = 13
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.Blue
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label10.Location = System.Drawing.Point(242, 227)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(224, 32)
        self._label10.TabIndex = 14
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.Blue
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label11.Location = System.Drawing.Point(242, 382)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(224, 32)
        self._label11.TabIndex = 15
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.Blue
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label12.Location = System.Drawing.Point(242, 424)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(224, 32)
        self._label12.TabIndex = 16
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkRed
        self.ClientSize = System.Drawing.Size(551, 533)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Program 93a"
        self.ResumeLayout(False)
        self.PerformLayout()
    

    def Button2Click(self, sender, e):
        self._label8.Text = ""
        self._label9.Text = ""
        self._label10.Text = ""
        self._label11.Text = ""
        self._label12.Text = ""
        self._textBox1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        kwh = float(self._textBox1.Text)
        prebaserate = float(kwh) * 0.0475
        baserate = round(prebaserate, 2)
        self._label8.Text = "$" + str(baserate)
        presurcharge = float(baserate) * .1
        surcharge = round(presurcharge, 2)
        self._label9.Text = "$" + str(surcharge)
        pretax = float(baserate) * .03
        tax = round(pretax, 2)
        self._label10.Text = "$" + str(tax)
        totalbill = float(baserate) + float(surcharge) + float(tax)
        self._label11.Text = "$" + str(totalbill)
        prelatefee = float(totalbill) * .04
        latefee = round(prelatefee, 2)
        latebill = float(totalbill) + float(latefee)
        self._label12.Text = "$" + str(latebill)
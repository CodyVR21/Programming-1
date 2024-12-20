﻿import System.Drawing
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
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._button4 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(29, 19)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(131, 49)
        self._label1.TabIndex = 0
        self._label1.Text = "Length:"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(29, 91)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(131, 49)
        self._label2.TabIndex = 1
        self._label2.Text = "Width:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(29, 166)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(131, 49)
        self._label3.TabIndex = 2
        self._label3.Text = "Area:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(29, 245)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(163, 49)
        self._label4.TabIndex = 3
        self._label4.Text = "Perimeter:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.Red
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.Color.MediumBlue
        self._label5.Location = System.Drawing.Point(198, 166)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(290, 49)
        self._label5.TabIndex = 4
        self._label5.Click += self.Label5Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Red
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.Color.MediumBlue
        self._label6.Location = System.Drawing.Point(198, 245)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(290, 49)
        self._label6.TabIndex = 5
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.GhostWhite
        self._button2.Location = System.Drawing.Point(377, 353)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(187, 85)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.DarkBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.GhostWhite
        self._button1.Location = System.Drawing.Point(47, 353)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(187, 85)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(180, 19)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(398, 40)
        self._textBox1.TabIndex = 10
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(180, 91)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(398, 40)
        self._textBox2.TabIndex = 11
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.DarkBlue
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.ForeColor = System.Drawing.Color.GhostWhite
        self._button4.Location = System.Drawing.Point(741, 353)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(187, 85)
        self._button4.TabIndex = 13
        self._button4.Text = "Exit"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DodgerBlue
        self.ClientSize = System.Drawing.Size(965, 440)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._label5)
        self.Name = "MainForm"
        self.Text = "Prog52a"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width  = int(self._textBox2.Text)
        area   = length * width
        perim  = 2 * length + 2 * width 
        self._label5.Text = str(area)
        self._label6.Text = str(perim)
        # + - * / %     ** pow     // divide & round down
        # int (integer): a whole number, pos/neg
        # float (Floating-Point Number): any number w/ a decimal
        # str (string): a string of text 
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""

    def Label5Click(self, sender, e):
        pass

    def Button4Click(self, sender, e):
        Application.Exit()
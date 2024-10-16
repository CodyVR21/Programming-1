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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(67, 17)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(201, 45)
        self._label1.TabIndex = 0
        self._label1.Text = "First Number"
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(30, 70)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(201, 45)
        self._label2.TabIndex = 1
        self._label2.Text = "Second Number"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(44, 144)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(201, 45)
        self._label3.TabIndex = 2
        self._label3.Text = "Third Number"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 210)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(201, 45)
        self._label4.TabIndex = 3
        self._label4.Text = "Forth Number"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(237, 17)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(334, 40)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(237, 70)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(334, 40)
        self._textBox2.TabIndex = 5
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(237, 144)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(334, 40)
        self._textBox3.TabIndex = 6
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(237, 203)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(334, 40)
        self._textBox4.TabIndex = 7
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(252, 451)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(149, 57)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(67, 279)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(86, 29)
        self._label5.TabIndex = 10
        self._label5.Text = "Sum"
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(67, 363)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(117, 35)
        self._label6.TabIndex = 11
        self._label6.Text = "Average"
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(44, 451)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(149, 57)
        self._button2.TabIndex = 12
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(476, 451)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(149, 57)
        self._button3.TabIndex = 13
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(237, 272)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(334, 36)
        self._label7.TabIndex = 14
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(237, 350)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(334, 36)
        self._label8.TabIndex = 15
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(625, 520)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "program 54b"
        self.ResumeLayout(False)
        self.PerformLayout()
   

    def Button3Click(self, sender, e):
        Application.Exit()
        pass
    

    def Button1Click(self, sender, e):
        first = int(self._textBox1.Text)
        second = int(self._textBox2.Text)
        third = int(self._textBox3.Text)
        fourth = int(self._textBox4.Text)
        s = first + second + third + fourth 
        self._label7.Text = str(s)
        average = s / 4
        self._label8.Text = str(average)
        pass
    

    def Button2Click(self, sender, e):
        self._label7.Text = ""
        self._label8.Text = ""
        pass

    def Label5Click(self, sender, e):
        pass
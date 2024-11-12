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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(163, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(307, 49)
        self._label1.TabIndex = 0
        self._label1.Text = "British Conversion"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkRed
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(24, 93)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(173, 34)
        self._label2.TabIndex = 1
        self._label2.Text = "Pounds"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkRed
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(24, 146)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(173, 34)
        self._label3.TabIndex = 2
        self._label3.Text = "Shillings"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkRed
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(24, 206)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(173, 33)
        self._label4.TabIndex = 3
        self._label4.Text = "Pence"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.DarkRed
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(24, 308)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(173, 69)
        self._label5.TabIndex = 4
        self._label5.Text = "Modern Notation"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(37, 380)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(150, 43)
        self._button1.TabIndex = 5
        self._button1.Text = "Convert"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(229, 380)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(132, 43)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(412, 380)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(145, 43)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.DarkRed
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(244, 308)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(258, 69)
        self._label6.TabIndex = 8
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(244, 93)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(243, 38)
        self._textBox1.TabIndex = 9
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(244, 145)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(243, 38)
        self._textBox2.TabIndex = 10
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(244, 205)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(243, 38)
        self._textBox3.TabIndex = 11
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Red
        self.ClientSize = System.Drawing.Size(585, 454)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog65H"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
         # Collect data from textboxes and create variables
        lbs = float(self._textBox1.Text)
        shil = float(self._textBox2.Text)
        pence = float(self._textBox3.Text)
        # Convert shillings and old pence to new pence
        newpence = (float(shil) * 5) * .01
        oldpence = (float(pence) * 8.33333333333) * .0001
        # Adding and then printing
        prenewnotation = float(lbs) + float(newpence) + float(oldpence)
        newnotation = round(prenewnotation, 2)
        self._label6.Text = str(newnotation)

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()
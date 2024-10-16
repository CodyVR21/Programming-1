import System.Drawing
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
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self._label14 = System.Windows.Forms.Label()
        self._label15 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MediumBlue
        self._label1.Cursor = System.Windows.Forms.Cursors.Arrow
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(36, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(380, 44)
        self._label1.TabIndex = 0
        self._label1.Text = "Change Calculator"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(12, 640)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(203, 60)
        self._button1.TabIndex = 1
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(108, 587)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(277, 47)
        self._button2.TabIndex = 2
        self._button2.Text = "Calculate"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(278, 640)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(203, 60)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MediumBlue
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label2.Location = System.Drawing.Point(2, 67)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(163, 43)
        self._label2.TabIndex = 4
        self._label2.Text = "Amount Due"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumBlue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Location = System.Drawing.Point(2, 128)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(163, 43)
        self._label3.TabIndex = 5
        self._label3.Text = "Amount Given"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MediumBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label4.Location = System.Drawing.Point(2, 188)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(163, 43)
        self._label4.TabIndex = 6
        self._label4.Text = "Change Due"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MediumBlue
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label5.Location = System.Drawing.Point(2, 253)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(163, 43)
        self._label5.TabIndex = 7
        self._label5.Text = "Dollars"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MediumBlue
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label6.Location = System.Drawing.Point(2, 306)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(163, 43)
        self._label6.TabIndex = 8
        self._label6.Text = "Quarters"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.MediumBlue
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label7.Location = System.Drawing.Point(2, 368)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(163, 43)
        self._label7.TabIndex = 9
        self._label7.Text = "Dimes"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.MediumBlue
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label8.Location = System.Drawing.Point(2, 422)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(163, 43)
        self._label8.TabIndex = 10
        self._label8.Text = "Nickels"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.MediumBlue
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label9.Location = System.Drawing.Point(2, 475)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(163, 43)
        self._label9.TabIndex = 11
        self._label9.Text = "Pennies"
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.MediumBlue
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._textBox1.Location = System.Drawing.Point(180, 67)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(181, 38)
        self._textBox1.TabIndex = 12
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.MediumBlue
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._textBox2.Location = System.Drawing.Point(180, 122)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(181, 38)
        self._textBox2.TabIndex = 13
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label10.Location = System.Drawing.Point(180, 188)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(181, 32)
        self._label10.TabIndex = 14
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label11.Location = System.Drawing.Point(180, 368)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(181, 32)
        self._label11.TabIndex = 15
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label12.Location = System.Drawing.Point(180, 422)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(181, 32)
        self._label12.TabIndex = 16
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label13.Location = System.Drawing.Point(180, 475)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(181, 32)
        self._label13.TabIndex = 17
        # 
        # label14
        # 
        self._label14.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label14.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label14.Location = System.Drawing.Point(180, 306)
        self._label14.Name = "label14"
        self._label14.Size = System.Drawing.Size(181, 32)
        self._label14.TabIndex = 18
        # 
        # label15
        # 
        self._label15.BackColor = System.Drawing.Color.DeepSkyBlue
        self._label15.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label15.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label15.Location = System.Drawing.Point(180, 253)
        self._label15.Name = "label15"
        self._label15.Size = System.Drawing.Size(181, 32)
        self._label15.TabIndex = 19
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DodgerBlue
        self.ClientSize = System.Drawing.Size(493, 703)
        self.Controls.Add(self._label15)
        self.Controls.Add(self._label14)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Program58t"
        self.ResumeLayout(False)
        self.PerformLayout()
        

    def Button2Click(self, sender, e): # Calculate
        
    

    def Button3Click(self, sender, e): # Exit
        Application.Exit()
        pass
    

    def Button1Click(self, sender, e): # Clear
        
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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MediumBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(3, 15)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(180, 44)
        self._label1.TabIndex = 0
        self._label1.Text = "Pick a Car:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.MediumBlue
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(12, 167)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(109, 56)
        self._label2.TabIndex = 1
        self._label2.Text = "Miles"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.MediumBlue
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(12, 348)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(109, 56)
        self._label3.TabIndex = 2
        self._label3.Text = "MPG"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.MediumBlue
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(12, 256)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(109, 56)
        self._label4.TabIndex = 3
        self._label4.Text = "Gallons"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.MediumBlue
        self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(182, 170)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(204, 45)
        self._label5.TabIndex = 4
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.MediumBlue
        self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(182, 267)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(204, 45)
        self._label6.TabIndex = 5
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.MediumBlue
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label7.Location = System.Drawing.Point(182, 351)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(204, 45)
        self._label7.TabIndex = 6
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(147, 79)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(141, 55)
        self._button1.TabIndex = 7
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(3, 79)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(141, 55)
        self._button2.TabIndex = 8
        self._button2.Text = "Calculate"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MediumBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(294, 79)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(141, 55)
        self._button3.TabIndex = 9
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # comboBox1
        # 
        self._comboBox1.BackColor = System.Drawing.Color.DeepSkyBlue
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["1970 VW Bug",
            "1979 Firebird",
            "1980 Subaru",
            "1975 Cutlass"]))
        self._comboBox1.Location = System.Drawing.Point(216, 15)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(214, 37)
        self._comboBox1.TabIndex = 10
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DodgerBlue
        self.ClientSize = System.Drawing.Size(442, 469)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54a"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        miles = 1
        gallons = 1
        car = self._comboBox1.Text
        
        # TODO: repeat for all 4 cars 
        if car == "1970 VW Bug":
            miles = 286
            gallons = 9
        elif car == "1979 Firebird":
            miles = 412
            gallons = 40
        elif car == "1980 Subaru":
            miles = 361 
            gallons = 18
        elif car == "1975 Cutlass":
            miles = 161
            gallons = 11
        
        mpg = miles / gallons
        mpg = round(mpg, 1)
        
        self._label7.Text = str(mpg)
        
            
        self._label5.Text = str(miles)
        self._label6.Text = str(gallons)
          
        # elif car == "second car":
        # miles = ...
        # gallons = ...
        

    def Button3Click(self, sender, e):
        Application.Exit()
        

    def Button1Click(self, sender, e):
        self._label5.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""
        
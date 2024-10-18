import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.MediumBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(259, 355)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(164, 59)
        self._button1.TabIndex = 0
        self._button1.Text = "Start"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.MediumBlue
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(1, -2)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(876, 341)
        self._label1.TabIndex = 3
        self._label1.Text = "Scheldule"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.MediumBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(470, 355)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(164, 59)
        self._button2.TabIndex = 4
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.RoyalBlue
        self.ClientSize = System.Drawing.Size(880, 426)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Schedule"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = "Freshmen Seminar 8:00 - 8:47 \n"+\
        "Computer Programing 1 EM 8:52 - 9:39 \n"+\
        "Algebra 1 A 9:44 - 10:31 \n"+\
        "English 9 A 10:36 - 11:25 \n"+\
        "Freshmen Weight Traning 11:30 - 12:52 \n"+\
        "World Studies A 12:57 - 1:44\n"+"Manufacturing 1 1:49 - 2:36 \n"+\
        "Biology A 2:41 - 3:28"

    def Button2Click(self, sender, e):
        Application.Exit()
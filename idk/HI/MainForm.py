import System.Drawing
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
        self._button1.Font = System.Drawing.Font("Microsoft Yi Baiti", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(414, 323)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(157, 77)
        self._button1.TabIndex = 0
        self._button1.Text = "START"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Yi Baiti", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(141, 323)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(157, 77)
        self._button2.TabIndex = 1
        self._button2.Text = "INFO"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Yi Baiti", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(707, 323)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(149, 77)
        self._button3.TabIndex = 2
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Yi Baiti", 26.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(414, 112)
        self._label1.Name = "label1"
        self._label1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._label1.Size = System.Drawing.Size(106, 37)
        self._label1.TabIndex = 3
        self._label1.Text = "HI"
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        self._label1.Click += self.Label1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Firebrick
        self.ClientSize = System.Drawing.Size(984, 426)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "HI"
        self.ResumeLayout(False)


    def Label1Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        self._Label1.Text = "HI"        
    

    def Button2Click(self, sender, e):
        self._label1.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()